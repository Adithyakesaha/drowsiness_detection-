import tkinter as tk
from PIL import Image, ImageTk
import cv2

from gui.components import create_header, create_status_panel, create_control_panel

from src.detector_yolo import detect_faces
from src.eye_cnn import predict_eye_state
from src.alert import trigger_alert
from src.utils import log_event
from src.config import *

class DriverApp:

    def __init__(self, root):
        self.root = root
        self.root.title("AI Driver Monitoring")
        self.root.geometry("1000x600")
        self.root.configure(bg="#121212")

        # Header
        create_header(root)

        # Video Frame
        self.video_label = tk.Label(root)
        self.video_label.pack(side="left", padx=10, pady=10)

        # Status Panel
        self.status_label, self.score_label, self.log_box = create_status_panel(root)

        # Controls
        self.start_btn, self.stop_btn, self.exit_btn = create_control_panel(root)

        self.start_btn.config(command=self.start_camera)
        self.stop_btn.config(command=self.stop_camera)
        self.exit_btn.config(command=self.exit_app)

        # Variables
        self.cap = None
        self.running = False
        self.counter = 0
        self.drowsy_events = 0

    def start_camera(self):
        self.cap = cv2.VideoCapture(0)
        self.running = True
        self.update_frame()

    def stop_camera(self):
        self.running = False
        if self.cap:
            self.cap.release()

    def exit_app(self):
        self.stop_camera()
        self.root.destroy()

    def update_frame(self):
        if not self.running:
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        faces = detect_faces(frame)
        status = "Awake"

        for (x1, y1, x2, y2) in faces:
            face = frame[y1:y2, x1:x2]

            if face.size == 0:
                continue

            pred = predict_eye_state(face)

            if pred < CNN_THRESHOLD:
                self.counter += 1
            else:
                self.counter = 0

            if self.counter >= FRAME_THRESHOLD:
                status = "DROWSY!"
                trigger_alert()

                if self.counter == FRAME_THRESHOLD:
                    self.drowsy_events += 1
                    log_event("Drowsiness detected")
                    self.log_box.insert(tk.END, "⚠ Drowsiness detected\n")
                    self.log_box.see(tk.END)

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

        # Update UI
        score = max(100 - self.drowsy_events * 2, 0)

        self.status_label.config(text=f"Status: {status}")
        self.score_label.config(text=f"Score: {score}")

        # Convert frame for Tkinter
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)

        self.video_label.imgtk = imgtk
        self.video_label.configure(image=imgtk)

        self.video_label.after(10, self.update_frame)


if __name__ == "__main__":
    root = tk.Tk()
    app = DriverApp(root)
    root.mainloop()