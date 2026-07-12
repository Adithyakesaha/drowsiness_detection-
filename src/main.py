import cv2
from src.detector_yolo import detect_faces
from src.eye_cnn import predict_eye_state
from src.alert import trigger_alert
from src.utils import log_event, draw_box, draw_status
from src.config import CNN_THRESHOLD, FRAME_THRESHOLD

counter = 0
drowsy_events = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not detected")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = detect_faces(frame)
    status = "Awake"

    for box in faces:
        x1, y1, x2, y2 = box
        face = frame[y1:y2, x1:x2]

        if face.size == 0:
            continue

        pred = predict_eye_state(face)

        if pred < CNN_THRESHOLD:
            counter += 1
        else:
            counter = 0

        if counter >= FRAME_THRESHOLD:
            status = "DROWSY!"
            trigger_alert()

            if counter == FRAME_THRESHOLD:
                drowsy_events += 1
                log_event("Drowsiness detected")

        draw_box(frame, box)

    score = max(100 - drowsy_events * 2, 0)
    draw_status(frame, status, score)

    cv2.imshow("Driver Monitoring System", frame)

    # ESC key to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()