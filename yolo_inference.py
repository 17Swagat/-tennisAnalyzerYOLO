from ultralytics import YOLO
# from ultralytics import SAM

# model = YOLO("yolo11x.pt")

# 📜 Loading COLAB Pretrained Model
MODEL_PATH = "E:/@tennisAnalyzerYOLO/TRAINED_MODELS_COLAB/runs/detect/yolov11x-roboflow-10k-epochs-13/weights/last.pt"
model = YOLO(model='yolo11x.pt' )#MODEL_PATH)#"yolo11x.pt")


# Inference
# can give image/video:=>
result = model.predict(
    source="inference_inputs/vid_01.mp4",
    conf=0.1, # Confidence threshold for predictions
    save=True,
    show_labels=False,
    stream=True, # For videos, stream processes frame-by-frame
)
for r in result:
    pass # # This processes each frame and triggers saving

print("Inference complete! Check the 'runs' folder.")