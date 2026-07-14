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

   image = mp.Image.create_from_file('hand.jpg')
   
   result = recognizer.recognize(image)
   
   gestureName = result.gestures[0][0].category_name
   print(gestureName)

   i = cv2.imread("hand.jpg")
   resized_i = cv2.resize(i, (800, 600), interpolation=cv2.INTER_LINEAR)

   cv2.putText(resized_i,gestureName,(20,50),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
   cv2.imshow("AI Mediapipe Gesture Recognition",resized_i)
   cv2.waitKey(0)

   



    
