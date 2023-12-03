import cv2
import numpy as np
import os
import shutil
from pynput.mouse import Listener

root = os.path.join('/Users', 'axelcasas', 'Documents', '1_Projects', '2-data-science', 'machine-learning', 'neurotechx', 'data')

# Normalize
def normalize(x):
  minn, maxx = x.min(), x.max()
  return (x - minn) / (maxx - minn)

# Eye cropping (it takes photos from your eyes)
def scan(image_size=(32, 32)):
  _, frame = video_capture.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  boxes = cascade.detectMultiScale(gray, 1.3, 10)
  if len(boxes) == 2:
    eyes = []
    for box in boxes:
      x, y, w, h = box
      eye = frame[y:y + h, x:x + w]
      eye = cv2.resize(eye, image_size)
      eye = normalize(eye)
      eye = eye[10:-10, 5:-5]
      eyes.append(eye)
    return (np.hstack(eyes) * 255).astype(np.uint8)
  else:
    return None
  
# When you click, you get photos  
def on_click(x, y, button, pressed):
  # If the action was a mouse PRESS (not a RELEASE)
  if pressed:
    # Crop the eyes
    eyes = scan()
    # If the function returned None, something went wrong
    if not eyes is None:
      # Save the image
      filename = os.path.join(root, "{}_{}_{}.jpeg".format(x, y, button))
      cv2.imwrite(filename, eyes)

# Harcascade class for this particular objective      
cascade = cv2.CascadeClassifier("Class/haarcascade_eye.xml")
video_capture = cv2.VideoCapture(0)

with Listener(on_click = on_click) as listener:
  listener.join()