import cv2
from src.pose_extractor import PoseExtractor
from src.metrics_calculator import MetricsCalculator
from src.rules_engine import RulesEngine
from src.ui import UI

def main():
    extractor = PoseExtractor()
    calculator = MetricsCalculator()
    rules = RulesEngine()
    ui = UI()

    cap = cv2.VideoCapture("video.mp4")
    
    # Obtener propiedades del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Crear el video de salida
    out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = extractor.extract(frame)

        if results.pose_landmarks:
            metrics = calculator.get_elbow_angles(results.pose_landmarks)
            resultados = rules.evaluate(metrics)
            frame = ui.draw(frame, results.pose_landmarks, resultados)

        out.write(frame)
        frame_count += 1
        if frame_count % 30 == 0:
            print(f"Procesados {frame_count} frames...")

    cap.release()
    out.release()
    print("Listo. Video guardado en output.mp4")

if __name__ == "__main__":
    main()