# ===============================
# Drowsiness Detection Config
# ===============================

# Eye detection (MediaPipe)
EAR_THRESHOLD = 0.25   # lower = more sensitive
CNN_THRESHOLD = EAR_THRESHOLD

# Frames threshold (how long eyes closed)
FRAME_THRESHOLD = 15

# Alert cooldown (seconds)
ALERT_COOLDOWN = 3

# YOLO model path
YOLO_MODEL = "yolov8n.pt"

# Logging
LOG_FILE = "logs/drowsy_log.txt"
