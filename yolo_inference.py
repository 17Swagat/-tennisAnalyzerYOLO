# import ultralytics
from ultralytics import YOLO

model = YOLO('yolov8x')

# Inference
model.predict(source='input_videos/image.png', save=True)