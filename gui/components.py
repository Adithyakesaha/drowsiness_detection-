import tkinter as tk
from tkinter import ttk

def create_header(parent):
    frame = tk.Frame(parent, bg="#1e1e2f", height=60)
    frame.pack(fill="x")

    title = tk.Label(frame, text="Driver Drowsiness Detection System",
                     fg="white", bg="#1e1e2f",
                     font=("Arial", 18, "bold"))
    title.pack(pady=10)

    return frame


def create_status_panel(parent):
    frame = tk.Frame(parent, bg="#2c2c3e", width=300)
    frame.pack(side="right", fill="y")

    status_label = tk.Label(frame, text="Status: Awake",
                            fg="white", bg="#2c2c3e",
                            font=("Arial", 14))
    status_label.pack(pady=20)

    score_label = tk.Label(frame, text="Score: 100",
                           fg="lightgreen", bg="#2c2c3e",
                           font=("Arial", 14))
    score_label.pack(pady=10)

    log_box = tk.Text(frame, height=15, width=35, bg="#1e1e2f",
                      fg="white", font=("Arial", 10))
    log_box.pack(pady=20)

    return status_label, score_label, log_box


def create_control_panel(parent):
    frame = tk.Frame(parent, bg="#1e1e2f", height=60)
    frame.pack(fill="x", side="bottom")

    start_btn = ttk.Button(frame, text="Start")
    start_btn.pack(side="left", padx=10, pady=10)

    stop_btn = ttk.Button(frame, text="Stop")
    stop_btn.pack(side="left", padx=10)

    exit_btn = ttk.Button(frame, text="Exit")
    exit_btn.pack(side="right", padx=10)

    return start_btn, stop_btn, exit_btn