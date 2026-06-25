import cv2

from src.metrics_calculator import MetricsCalculator
from src.pose_extractor import PoseExtractor
from src.rules_engine import RulesEngine
from src.ui import UI

def main():
    # Crear cada cosa
    extractor = PoseExtractor()
    calculator = MetricsCalculator()
    rules = RulesEngine()
    ui = UI()

    # Abrir el video
    cap = cv2.VideoCapture("video.mp4")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # 1- Extraer los landmarks
        results = extractor.extract(frame)

        # 2- Si hay landmarks, calcular metricas y evaluar
        if results.pose_landmarks:
            metrics = calculator.get_elbow_angles(results.pose_landmarks)
            resultados = rules.evaluate(metrics)
            frame = ui.draw(frame, results.pose_landmarks, resultados)

        # Mostrar el frame
        cv2.imshow("Swim analyzer", frame)

        # Salir si se pulsa q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()