# import ultralytics
from ultralytics import YOLO
# from ultralytics import SAM

model = YOLO('yolov8x')

# Inference
# can give image/video:=>
result  = model.predict(source='input_videos/input_video.mp4', 
                        save=True,)
                        # stream=True)

print(result)