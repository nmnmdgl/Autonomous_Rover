import cv2
import numpy as np

def detect_red(img):
  # Convert BGR to HSV color space
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  # Define lower and upper bounds for red color (adjust as needed)
  lower_red = np.array([0, 100, 100], dtype="uint8")
  upper_red = np.array([10, 255, 255], dtype="uint8")

  # Create a mask to isolate red color pixels
  mask = cv2.inRange(hsv, lower_red, upper_red)

  # Find contours around red objects
  contours= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # Find the largest contour (assuming the object of interest is the largest)
  if len(contours) > 0:
    largest_contour = max(contours, key=cv2.contourArea)

    # Get bounding rectangle coordinates
    x, y, w, h = cv2.boundingRect(largest_contour)
    return (x, y, w, h)
  else:
    return None  # No red object detected

def drawBox(img, bbox):
    if bbox is not None:  # Check if a red object was detected
        x, y, w, h = bbox
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 0, 255), 2, 1)  # Red color

while True:
    cap = cv2.VideoCapture(1)  # Capture from webcam (change index for external camera)
    success, img = cap.read()

    # Detect red object and get bounding box (if any)
    bbox = detect_red(img.copy())  # Make a copy of the image for processing

    # Draw bounding box and display live feed
    drawBox(img, bbox)
    cv2.imshow("Tracking", img)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
