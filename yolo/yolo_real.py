from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model(0 , show=True) 
for i in enumerate(results):
    print(i)
    