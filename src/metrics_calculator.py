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

        hombro_der = landmarks.landmark[12]
        codo_der = landmarks.landmark[14]
        muneca_der = landmarks.landmark[16]

        ang_izq = self.calculate_angle(hombro_izq, codo_izq, munñca_izq)
        angulo_der = self.calculate_angle(hombro_der, codo_der, muneca_der)

        return {"codo_izquierdo": ang_izq,
                "codo_derecho": angulo_der}