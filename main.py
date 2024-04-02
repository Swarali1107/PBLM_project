import cv2
from ultralytics import YOLO
import time

# Load YOLOv5 model
model = YOLO("yolov5s.pt")

# Class names for COCO dataset
class_names = model.module.names if hasattr(model, 'module') else model.names

# Open video file
cap = cv2.VideoCapture("vid.mp4")

# Variables for FPS calculation
prev_frame_time = 0
new_frame_time = 0

# Main loop
while True:
    # Read frame
    success, img = cap.read()
    if not success:
        break  # End of video
    
    # Perform object detection
    results = model(img, size=640)
    
    # Process results
    for result in results.xyxy[0]:
        x1, y1, x2, y2, conf, cls = result
        label = f'{class_names[int(cls)]} {conf:.2f}'
        
        # Draw bounding box and label
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(img, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Calculate and display FPS
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    cv2.putText(img, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    
    # Display frame
    cv2.imshow("Object Detection", img)
    
    # Check for key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
