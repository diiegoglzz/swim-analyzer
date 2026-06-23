import numpy as np

class MetricsCalculator:

    def calculate_angle(self, a, b, c):
       # Convertir cada punto en una array 
        A = np.array([a.x, a.y])
        B = np.array([b.x, b.y])
        C = np.array([c.x, c.y])

        # Calcular el angulo
        angulo = np.degrees(
            np.arctan2(C[1] - B[1], C[0] - B[0]) -
            np.arctan2(A[1] - B[1], A[0] - B[0])
        )

        return abs(angulo)
    
    def get_elbow_angles(self, landmarks):
        # Extraer los puntos necesarios
        hombro_izq = landmarks.landmark[11] #12
        codo_izq = landmarks.landmark[13] #14
        munñca_izq = landmarks.landmark[15] #16 si fueran del lado derecho

        ang_izq = self.calculate_angle(hombro_izq, codo_izq, munñca_izq)

        return {"codo_izquierdo": ang_izq}