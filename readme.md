# Accident CCTV Detection System

The Accident CCTV Detection System is a real-time solution designed to automatically detect accidents or violence using CCTV footage. By leveraging computer vision and machine learning algorithms, the system continuously monitors traffic patterns and identifies anomalies that could indicate accidents.

## Tech Stack

### Frontend
- **Next.js**: A powerful React framework for building fast and user-friendly web applications.

### Backend
- **Object Detection**:
  - **YOLOv8 Classification**: A state-of-the-art object detection model used for identifying and classifying incidents from CCTV footage.
- **Large Language Models (LLMs)**:
  - **OpenAI GPT-4**: Used for natural language processing tasks to enhance the system's decision-making capabilities, including understanding accident reports and providing insights based on the detected incidents.


Here’s a more polished version of your `README.md`:

```markdown
# How to Use

### 1. Create a Virtual Environment
```bash
virtualenv seoulimpact
```

### 2. Activate the Virtual Environment
```bash
source seoulimpact/bin/activate
```

### 3. Download Pre-trained Weights
Download the model weights from [this link](https://drive.google.com/file/d/125SZzPj8fLLnOrbMqaaLEH3oYKN9q6sW/view?usp=sharing) and place the file at `weights/best.pt`.

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Start the API Server
Run the API on port `5002`:
```bash
python api.py
```

### 6. Process Video via API
To upload a video for processing, send a request to:
```
http://<your-server-ip>:5002/process_video
```

Replace `<your-server-ip>` with the actual server IP.
```