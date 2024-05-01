# import ultralytics
from ultralytics import YOLO

model = YOLO('yolov8x')

# Inference
result  = model.predict(source='input_videos/image.png') #, save=True)

# TESTING:

# print(type(result)) # list
# print(len(result)) # 1
# print(type(result[0])) # <class 'ultralytics.engine.results.Results'>

# for item in result[0]:
#     print(item)
# print(result[0])

# print(result)

# print('\n==========================================\n')
# print('\n==========================================\n')

# boxes
# boxes = result[0].boxes
# for box in boxes:
#     print(box)

# print('\n==========================================\n')

# names
# print(result[0].names) 
# names = result[0].names
# for key in names:
#     print(key, names[key])

# print('\n==========================================\n')


# print(len(result[0].boxes))  # 14

for index, box in enumerate(result[0].boxes):
    if index > 0:
        break
    # 1
    # print(box)
    
    # 2
    xyxy = box.xyxy # tensor
    print(xyxy)
    x_min, y_min, x_max, y_max = xyxy[0][1], xyxy[0][1], xyxy[0][2], xyxy[0][3]
    print(x_min, y_min, x_max, y_max)