import datetime
import cv2
from src.config import LOG_FILE

def log_event(msg):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time_now}] {msg}\n")

def draw_box(frame, box):
    x1, y1, x2, y2 = box
    cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

def draw_status(frame, status, score):
    cv2.putText(frame, f"Status: {status}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.putText(frame, f"Score: {score}", (10,60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)