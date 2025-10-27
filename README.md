# 🌾 Real-Time Grain Detection: Wheat and Rice

## **🎯 Project Overview**
This project implements a **high-performance Real-Time Object Detection system** using the **YOLO (You Only Look Once)** framework to accurately identify and classify **Wheat** and **Rice** grains from a live webcam feed.  
It is designed for **instant analysis in quality control applications** such as grain sorting and grading.

### Workflow Highlights
- **Data Labeling:** Using *Label Studio* for pixel-accurate bounding box annotations.  
- **Model Training:** Training executed on *Google Colab* with GPU acceleration.  
- **Local Deployment:** Real-time inference using *PyCharm* and *OpenCV*.

---

## 🛠️ Technology Stack & Requirements

| Component | Tool / Technology | Role in the Project |
|------------|-------------------|---------------------|
| **Model** | YOLO (Ultralytics) | Core architecture for fast object detection |
| **Framework** | PyTorch (`torch` / `torchvision`) | Deep learning backend supporting YOLO |
| **I/O** | OpenCV (`opencv-python`) | Handles the live webcam video stream |
| **IDE** | PyCharm | Used for development and local deployment |

`requirements.txt`
Dependencies required to run the local inference script:

### Core Deep Learning Framework
torch
torchvision

### YOLO Implementation
ultralytics

### Computer Vision & Image Processing
opencv-python

### Data Handling
numpy


---

## 📁 Project Structure
Folder layout for running the project in your local PyCharm environment:

PythonProject/

├── .venv/   # Python Virtual Environment (created by PyCharm)

├── detect_grains.py         # Main script for real-time inference

├── requirements.txt         # List of Python dependencies

├── weights/

│   └── best.pt              # Final trained YOLO model weights (MANDATORY)

└── README.md                # Project documentation


---

## 🚀 Setup Instructions

1. Clone the Repository
 
 First, open your terminal or command prompt and navigate to the folder where you want to save the project.

git clone https://github.com/nithya881/Real-Time-Grain-Detection-Wheat-and-Rice
cd PythonProject

2. Configure PyCharm and Dependencies

Open Project: Open the PythonProject folder in PyCharm.

Create Environment: PyCharm will usually prompt you to create a Virtual Environment (.venv).

Install Packages:
Open the PyCharm terminal (ensure the .venv is active) and run:

pip install -r requirements.txt


3. Place Model Weights

Ensure you have downloaded the weights from your Colab training and placed them correctly:

Action: Copy your trained best.pt file

Destination: weights/best.pt



---

## 🏃 Running the Real-Time Detector

The script detect_grains.py loads the model weights and connects to the webcam.

Method 1: PyCharm Run Configuration (Recommended)

1. Open detect_grains.py


2. Go to Run → Edit Configurations...


3. In the Parameters field, enter:

--weights weights/best.pt --source 0

> Note: --source 0 connects to your default webcam. Change the number if using an external camera.




4. Click Apply → OK, and then run the script.



Method 2: Terminal Execution

Run the command directly from the active PyCharm terminal:

python detect_grains.py --weights weights/best.pt --source 0


---


## 📸 Results

Below are some sample output frames showing grain detection and tracking:

	Grains detected and highlighted with bounding box


 

## 💡 Training & Data Workflow

For reference, the model training and dataset preparation included:

Data Labeling: Using Label Studio for accurate Wheat and Rice grain bounding boxes.

Training: Model trained in Google Colab for faster GPU computation.
The resulting best.pt file is used for inference.
