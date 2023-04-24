import cv2
import time
from blazeface import BlazeFace, BlazeFaceError

# Load the BlazeFace detector
detector = BlazeFace()

# Load the video file
cap = cv2.VideoCapture('path/to/your/video')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

# Loop over the frames from the video stream
while True:
    # Read the frame from the video stream
    ret, frame = cap.read()
    
    # If the frame was not read successfully, break from the loop
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    try:
        # Detect faces in the frame using BlazeFace
        faces = detector.detect(gray)

        # Draw a rectangle around each detected face
        for face in faces:
            x, y, w, h = face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    except BlazeFaceError as e:
        print(str(e))
    
    # Display the resulting frame
    cv2.imshow('Frame', frame)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
