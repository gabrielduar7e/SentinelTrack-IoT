from ultralytics import YOLO
import cv2
import numpy as np

# Carrega o modelo (use yolov8s.pt para mais precisão)
model = YOLO("yolov8s.pt")

# Caminho do vídeo de entrada
video_path = "media/motoVision.mp4"
cap = cv2.VideoCapture(video_path)

# Verifica se abriu corretamente
if not cap.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

# Parâmetros do vídeo de saída
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
# Define o FPS manualmente para o vídeo de saída (ex.: 10 FPS)
output_fps = 10.0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("media/output_detectado.mp4", fourcc, output_fps, (frame_width, frame_height))

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Processa 1 a cada 3 frames
    if frame_count % 3 != 0:
        continue

    # Faz a predição
    results = model(frame, verbose=False)[0]

    for box in results.boxes:
        cls = int(box.cls[0])
        if cls == 3:  # Classe 3 = moto (motorcycle)
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            label = f"moto {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)

cap.release()
out.release()
print("Detecção concluída. Saída salva em media/output_detectado.mp4")
