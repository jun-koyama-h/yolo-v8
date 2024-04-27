from ultralytics import YOLO

# load pretrained model.
model: YOLO = YOLO(model="yolov8x.pt")

result: list = model.predict("MOT17-14-SDP-raw.mp4", save=True)