# 🚨 SentinelTrack-IoT

Um sistema de monitoramento inteligente com detecção de motocicletas em vídeos via visão computacional utilizando YOLOv8. Desenvolvido como parte de um projeto acadêmico, o SentinelTrack-IoT oferece uma solução eficiente para análise de tráfego e segurança.

## 👥 Equipe

- Gabriel Duarte Pinto - RM556972  
- Thomaz Oliveira Vilas Boas Bartol - RM555323  
- Vinicius Souza Carvalho - RM556089

---

## 📦 Pré-requisitos

Antes de iniciar, verifique se você possui os seguintes itens instalados:

- Python 3.10 ou superior  
- Git (opcional, mas recomendado)  
- pip atualizado

---

## 🛠️ Instalação

1. Clone o repositório ou baixe o ZIP:
```bash
git clone https://github.com/seu-usuario/SentinelTrack-IoT.git
cd SentinelTrack-IoT
Crie um ambiente virtual:

bash
Copiar
Editar
python -m venv venv
Ative o ambiente virtual:

No Windows:

bash
Copiar
Editar
venv\Scripts\activate
No Linux/Mac:

bash
Copiar
Editar
source venv/bin/activate
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
📂 Estrutura do Projeto
Copiar
Editar
SentinelTrack-IoT/
├── core/
│   └── sentinelv8_detect.py
├── media/
│   ├── motoVision.mp4
│   └── output_detectado.mp4
├── models/
│   └── yolov8s.pt
├── docs/
│   └── OVERVIEW.md
├── requirements.txt
└── README.md
▶️ Como Rodar o Projeto
Certifique-se de ter um vídeo no diretório media/ com o nome motoVision.mp4.

Execute o script principal:

bash
Copiar
Editar
python core/sentinelv8_detect.py
Ao final, o vídeo de saída será gerado em:

bash
Copiar
Editar
media/output_detectado.mp4
🎯 Objetivo do Projeto
Detectar motocicletas em vídeos utilizando o modelo YOLOv8 da biblioteca Ultralytics. O objetivo é oferecer suporte à análise de tráfego e ações de segurança em ambientes monitorados.

🤖 Tecnologias Utilizadas
Python 3.10+

OpenCV

Ultralytics YOLOv8

NumPy

📽️ Resultados Esperados
O sistema processa o vídeo frame a frame, detecta motocicletas e destaca com uma caixa verde e a confiança da detecção. O vídeo final é exportado para posterior análise.

❗ Problemas Conhecidos
O modelo pode apresentar dificuldade para detectar motos pequenas ou distantes.

Processamento pode ser lento em máquinas sem GPU.

💡 Sugestões Futuras
Integração com sensores IoT para acionamento de alertas.

Uso de modelos mais robustos (YOLOv8m ou v8l).

Interface gráfica web para facilitar o uso.
