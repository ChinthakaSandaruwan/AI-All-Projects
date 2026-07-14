import mediapipe as mp
import cv2

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the image mode:
options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path='gesture_recognizer.task'),
    running_mode=VisionRunningMode.IMAGE)


with GestureRecognizer.create_from_options(options) as recognizer:

    connection = [
    (0,1),(1,2),(2,3),(3,4),         # Thumb
    (0,5),(5,6),(6,7),(7,8),         # Index
    (5,9),(9,10),(10,11),(11,12),    # Middle
    (9,13),(13,14),(14,15),(15,16),  # Ring
    (13,17),(17,18),(18,19),(19,20), # Pinky
    (0,17)                           # Palm
    ] 

    webCam = cv2.VideoCapture(0)

    while True:
        b,frame = webCam.read()

        rgbframe =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgbframe)

        result = recognizer.recognize(image)
        
        gestureName = "None"
        if result.gestures and len(result.gestures) > 0:
            gestureName = result.gestures[0][0].category_name

        
        if result.hand_landmarks:
            # Get image height and width
            h, w, _ = frame.shape
            # Get the first detected hand
            hand = result.hand_landmarks[0]
            # Draw every landmark as a green circle
            for lm in hand:
                x = int(lm.x * w)
                y = int(lm.y * h)
                cv2.circle(frame, (x, y), 5, (0,255,0), -1)
            # Draw the skeleton
            for start, end in connection:
                # Get the two landmarks to connect
                p1 = hand[start]
                p2 = hand[end]
                # Convert to pixel coordinates
                x1 = int(p1.x * w)
                y1 = int(p1.y * h)
                x2 = int(p2.x * w)
                y2 = int(p2.y * h)
                # Draw a blue line
                cv2.line(frame, (x1, y1), (x2, y2), (255,0,0), 2)
        

                cv2.putText(frame,gestureName,(20,50),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
        
        cv2.imshow("AI Mediapipe Gesture Recognition",frame)
        cv2.waitKey(1)

   



    
