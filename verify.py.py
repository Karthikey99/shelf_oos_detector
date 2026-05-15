from ultralytics import YOLO
import cv2

# This will auto-download yolov8n.pt (~6MB) on first run
model = YOLO('yolov8n.pt')

print("✓ YOLOv8 loaded successfully")
print(f"  Model type: {type(model)}")
print(f"  OpenCV version: {cv2.__version__}")
print("\nAll good! Environment is ready.")