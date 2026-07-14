import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import os
from pycaw.pycaw import AudioUtilities

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# ── Volume setup (pycaw) ──────────────────────────────────────────────────────
def get_volume_object():
    devices = AudioUtilities.GetSpeakers()
    return devices.EndpointVolume

volume = get_volume_object()
vol_range = volume.GetVolumeRange()
MIN_VOL, MAX_VOL = vol_range[0], vol_range[1]

# Map 0-5 fingers → 0.0-1.0 scalar volume
FINGER_TO_SCALAR = {0: 0.0, 1: 0.2, 2: 0.4, 3: 0.6, 4: 0.8, 5: 1.0}

# Fingertip & MCP landmark indices
TIPS = [4, 8, 12, 16, 20]
MCPS = [2, 5,  9, 13, 17]

MARGIN = 10
FONT_SIZE = 1
FONT_THICKNESS = 1
HANDEDNESS_TEXT_COLOR = (88, 205, 54)
VOL_BAR_COLOR  = (0, 215, 255)
VOL_TEXT_COLOR = (255, 255, 255)

# MediaPipe drawing utilities for tasks API
mp_hands = mp.tasks.vision.HandLandmarksConnections
mp_drawing = mp.tasks.vision.drawing_utils
mp_drawing_styles = mp.tasks.vision.drawing_styles


def count_fingers(hand_landmarks, handedness_label):
    lm = hand_landmarks
    count = 0

    # Thumb: use X-axis comparison
    tip_x = lm[TIPS[0]].x
    mcp_x = lm[MCPS[0]].x
    if handedness_label == "Right":
        if tip_x < mcp_x:
            count += 1
    else:
        if tip_x > mcp_x:
            count += 1

    # Other 4 fingers: use Y-axis comparison
    for i in range(1, 5):
        if lm[TIPS[i]].y < lm[TIPS[i] - 2].y:
            count += 1

    return count


# _to_proto is no longer needed since the tasks API drawing utilities take hand landmarks list directly.


def draw_ui(image, detection_result):
    hand_landmarks_list = detection_result.hand_landmarks
    handedness_list     = detection_result.handedness
    annotated           = np.copy(image)
    h, w, _             = annotated.shape
    finger_count        = 0

    for idx in range(len(hand_landmarks_list)):
        lm         = hand_landmarks_list[idx]
        handedness = handedness_list[idx]
        label      = handedness[0].category_name

        # Draw skeleton using modern tasks drawing utilities
        mp_drawing.draw_landmarks(
            annotated,
            lm,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style(),
        )

        finger_count = count_fingers(lm, label)

        # Label above hand
        xs = [l.x for l in lm]; ys = [l.y for l in lm]
        tx = int(min(xs) * w);   ty = int(min(ys) * h) - MARGIN
        cv2.putText(annotated, f"{label}  Fingers: {finger_count}",
                    (tx, ty), cv2.FONT_HERSHEY_DUPLEX,
                    FONT_SIZE, HANDEDNESS_TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

    # ── Volume bar ────────────────────────────────────────────────────────────
    bar_x1, bar_y1 = w - 60, 50
    bar_x2, bar_y2 = w - 30, h - 50
    bar_h = bar_y2 - bar_y1

    scalar   = FINGER_TO_SCALAR.get(finger_count, 0.0)
    fill_top = int(bar_y2 - scalar * bar_h)

    cv2.rectangle(annotated, (bar_x1, bar_y1), (bar_x2, bar_y2), (80, 80, 80), 2)
    cv2.rectangle(annotated, (bar_x1, fill_top), (bar_x2, bar_y2), VOL_BAR_COLOR, -1)

    cv2.putText(annotated, f"{int(scalar * 100)}%",
                (bar_x1 - 10, bar_y2 + 25), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, VOL_TEXT_COLOR, 2, cv2.LINE_AA)
    cv2.putText(annotated, "VOL",
                (bar_x1, bar_y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, VOL_TEXT_COLOR, 2, cv2.LINE_AA)

    return annotated, finger_count


# ── Main ──────────────────────────────────────────────────────────────────────
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options      = vision.HandLandmarkerOptions(base_options=base_options, num_hands=1)
detector     = vision.HandLandmarker.create_from_options(options)

cap          = cv2.VideoCapture(0)
prev_fingers = -1

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame    = cv2.resize(frame, (640, 480))
    frame    = cv2.flip(frame, 1)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    result   = detector.detect(mp_image)

    annotated, finger_count = draw_ui(mp_image.numpy_view(), result)

    # Update volume only when finger count changes
    if finger_count != prev_fingers and result.hand_landmarks:
        scalar     = FINGER_TO_SCALAR[finger_count]
        target_vol = MIN_VOL + scalar * (MAX_VOL - MIN_VOL)
        volume.SetMasterVolumeLevel(target_vol, None)
        prev_fingers = finger_count

    cv2.imshow('Hand Volume Control  |  ESC to quit', annotated)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()