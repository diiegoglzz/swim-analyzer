import cv2

class UI:

    def draw(self, frame, landmarks, resultados):

        # Obtener la posicion del codo izq en pixeles
        codo = landmarks.landmark[13]
        x = int(codo.x * frame.shape[1])
        y = int(codo.y * frame.shape[0])

        # Dibujar el angulo en texto encima del codo
        angulo = resultados["codo_izquierdo"]["angulo"]
        cv2.putText(frame, f'{angulo:.1f}', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Elegir el color dependiendo si es correcto o no
        correcto = resultados["codo_izquierdo"]["correcto"]
        color = (0, 255, 0) if correcto else (0, 0, 255)

        # Dibuja un rectángulo de fondo y el feedback
        feedback = resultados["codo_izquierdo"]["feedback"]
        cv2.rectangle(frame, (10, 10), (400, 60), color, -1)
        cv2.putText(frame, feedback, (20, 45),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        return frame
