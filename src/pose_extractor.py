import cv2
import mediapipe as mp

class Poseextractor:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            min_detection_confidence = 0.5,
            min_trackin_confidence = 0.5
        )

        self.mp_draw = mp.solutions.drawing_utils

    
    def extract(self, frame):
        """ Recibe un frame de OpenCV y devuelve los alndmarks destectados."""
        rgb = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
        results = self.pose.process(rgb)
        return results
    
    def draw(self, frame, results):
        """ Dibuja el esqueleto sobre el frame"""
        if results.pose_landmarks:
            self.mp_draw.draw_landsmarks(
                frame,
                results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )

        return frame