from ultralytics import YOLO
import cv2
import time

# Load your trained model
model = YOLO("best.pt")     # path to your model file
model.to("cpu")             # ensure it runs on CPU

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Set lower resolution for smoother video
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Variables for FPS calculation
prev_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Run YOLO inference with smaller image size and higher confidence threshold
    results = model(frame, imgsz=480, conf=0.7, iou=0.5)

    # Draw boxes on the frame
    annotated_frame = results[0].plot()

    # Calculate FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Display FPS on the frame
    cv2.putText(annotated_frame, f"FPS: {int(fps)}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the output window
    cv2.imshow("Grain Detection - Realtime", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
cv2.destroyAllWindows()