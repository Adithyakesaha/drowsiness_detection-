import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

def eye_aspect_ratio(eye_points):
    A = np.linalg.norm(eye_points[1] - eye_points[5])
    B = np.linalg.norm(eye_points[2] - eye_points[4])
    C = np.linalg.norm(eye_points[0] - eye_points[3])
    return (A + B) / (2.0 * C)


def predict_eye_state(face_img):
    rgb = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return 1  # assume open

    landmarks = results.multi_face_landmarks[0].landmark
    h, w, _ = face_img.shape

    left_eye = np.array([(landmarks[i].x * w, landmarks[i].y * h) for i in LEFT_EYE])
    right_eye = np.array([(landmarks[i].x * w, landmarks[i].y * h) for i in RIGHT_EYE])

    left_ear = eye_aspect_ratio(left_eye)
    right_ear = eye_aspect_ratio(right_eye)

    ear = (left_ear + right_ear) / 2.0

    # Threshold
    if ear < 0.25:
        return 0  # closed
    else:
        return 1  # open