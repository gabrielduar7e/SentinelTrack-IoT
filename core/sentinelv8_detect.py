from ultralytics import YOLO
import cv2

# Carrega o modelo YOLOv8
model = YOLO('yolov8n.pt')

# Abre o vídeo
video_path = 'media/motoVision.mp4'
cap = cv2.VideoCapture(video_path)

# Verifica se abriu corretamente
if not cap.isOpened():
    print(f'Erro ao abrir o vídeo: {video_path}')
    exit()

# Loop de leitura dos frames
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Roda a detecção
    results = model(frame, verbose=False)[0]

    # Percorre as detecções
    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = model.names[cls_id]

        # Só desenha se for motocicleta
        if label.lower() in ['motorcycle', 'motorbike']:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Exibe o frame com as detecções
    cv2.imshow('Detecção de Motos', frame)
    if cv2.waitKey(1) == 27:  # Pressione ESC para sair
        break

cap.release()
cv2.destroyAllWindows()
