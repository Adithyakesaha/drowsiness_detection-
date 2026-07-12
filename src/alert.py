import os
from playsound import playsound
import threading

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ALERT_SOUND = os.path.join(BASE_DIR, "..", "assets", "alert.wav")

# Control flag
is_playing = False

def play_sound():
    global is_playing
    try:
        if os.path.exists(ALERT_SOUND):
            playsound(ALERT_SOUND)
        else:
            print("❌ alert.wav not found:", ALERT_SOUND)
    except Exception as e:
        print(f"⚠️ Sound error: {e}")
    finally:
        is_playing = False


def trigger_alert():
    global is_playing

    # Prevent multiple sounds at once
    if not is_playing:
        is_playing = True
        threading.Thread(target=play_sound, daemon=True).start()
