from ultralytics import YOLO
from src.config import YOLO_MODEL

model = YOLO(YOLO_MODEL)

def detect_faces(frame):
    results = model(frame, verbose=False)
    boxes = []

    for r in results:
        for b in r.boxes:
            x1, y1, x2, y2 = map(int, b.xyxy[0])
            boxes.append((x1, y1, x2, y2))

    return boxes