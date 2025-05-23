# SentinelTrack-IoT

O SentinelTrack-IoT é um projeto de visão computacional que utiliza a arquitetura YOLOv8 para detectar motocicletas em tempo real em imagens ou vídeos. O objetivo é aplicar técnicas modernas de inteligência artificial para rastrear o tráfego de veículos com foco em segurança e monitoramento.

## 🎯 Objetivo

Desenvolver um sistema de detecção de motocicletas que funcione de maneira eficaz utilizando modelos pré-treinados de deep learning (YOLOv8) e que possa ser utilizado como base para projetos de IoT e Smart Cities.

## ⚙️ Tecnologias Utilizadas

- Python
- OpenCV
- Ultralytics YOLOv8
- PyTorch
- Docker e Docker Compose (para ambiente controlado, se necessário)

## 📂 Estrutura do Projeto

- /core – Código principal de detecção.
- /docs – Documentações do projeto.
- /media – Vídeos ou imagens utilizados para testes.
- /models – Pesos do modelo treinado (por exemplo, yolov8n.pt).
- /venv – Ambiente virtual (não incluído no GitHub).
- requirements.txt – Lista de dependências Python.
- yolov8n.pt – Modelo pré-treinado da Ultralytics.

⚠️ A pasta venv deve ser adicionada ao .gitignore, pois não deve ser versionada.

## 🚀 Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/gabrielduar7e/SentinelTrack-IoT.git
   cd SentinelTrack-IoT
