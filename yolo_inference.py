from ultralytics import YOLO
# from ultralytics import SAM

model = YOLO("yolo11x.pt")


# Inference
# can give image/video:=>
result = model(
    source="inference_inputs/vid_01.mp4",
    save=True,
    stream=True,
)

# print(result)

for r in result:
    pass
