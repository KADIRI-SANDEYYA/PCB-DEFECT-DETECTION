<<<<<<< HEAD
<<<<<<< HEAD
# 🔍 Automated PCB Defect Detection using YOLOv8

An AI-powered system for **real-time detection of defects in Printed Circuit Boards (PCBs)** using the **YOLOv8** deep learning architecture.  
The system automatically identifies faults such as missing holes, open circuits, mouse bites, and solder bridges via a **user-friendly Streamlit interface**.

---

## 🎯 Project Objectives
- Develop a **real-time PCB defect detection system** with YOLOv8.
- Eliminate manual inspection errors and reduce production costs.
- Provide a **streamlined web interface** for quick defect visualization.
- Support industrial-scale deployment with **high accuracy** and **fast inference**.

---

## ❓ Problem Statement
Traditional PCB inspection methods are:
- Time-consuming
- Error-prone
- Inconsistent across varying layouts and lighting conditions  

This project replaces manual inspection with an **AI-powered solution** for **accurate, consistent, and efficient defect detection**.

---

## ⚙️ Methodology

1. **Data Acquisition**  
   Collected PCB images from industrial datasets and online sources.

2. **Annotation**  
   Labeled defects (missing holes, solder faults, cracks, shorts) using **LabelImg** / **Roboflow**.

3. **Preprocessing**  
   Applied normalization, noise removal, and contrast enhancement using **OpenCV**.

4. **Model Training**  
   Trained **YOLOv8** for object detection of PCB defects.

5. **Visualization**  
   Built a **Streamlit app** for image upload and **real-time defect visualization**.

---

## 📊 Model Performance

| Metric          | Value  |
|-----------------|--------|
| Precision       | 96.0%  |
| Recall          | 93.9%  |
| mAP@50          | 0.97   |
| Inference (GPU) | Fast   |
| Inference (CPU) | Moderate |

---

## 🧩 Tech Stack
- **Deep Learning:** YOLOv8 (Ultralytics)  
- **Programming Language:** Python 3.x  
- **Libraries:** OpenCV, NumPy, Pandas, Matplotlib, Seaborn, Streamlit  
- **Framework:** PyTorch  
- **Tools:** LabelImg / Roboflow, Git, GitHub  

---

## 🛠️ Installation & Usage

### Clone the Repository

git clone https://github.com/your-username/PCB-Defect-Detection-YOLOv8.git
cd PCB-Defect-Detection-YOLOv8

# Create a Python virtual environment
python -m venv pcb

# Activate the virtual environment
# Windows
pcb\Scripts\activate
# Linux/Mac
source pcb/bin/activate

# Install required Python packages
pip install -r requirements.txt

# Run the Streamlit application
streamlit run app2.py

---
## 🧠 System Architecture
PCB Image → Preprocessing (OpenCV) → YOLOv8 Model → Defect Detection → Streamlit Visualization

---

## 📷 App Preview

### Home / Landing Page  
![Home](https://github.com/KADIRI-SANDEYYA/PCB-DEFECT-DETECTION/blob/main/screenshots/Home.png)

### Upload PCB Image / Preprocessing  
![Upload PCB](https://github.com/KADIRI-SANDEYYA/PCB-DEFECT-DETECTION/blob/main/screenshots/Upload_PCB.png)

### YOLOv8 Model / Defect Detection  
![Defect Detection](https://github.com/KADIRI-SANDEYYA/PCB-DEFECT-DETECTION/blob/main/screenshots/YOLOv8_Detection.png)

### Results / Streamlit Visualization  
![Results](https://github.com/KADIRI-SANDEYYA/PCB-DEFECT-DETECTION/blob/main/screenshots/Results.png)

---

## ⚙️ Key Features
- Real-time detection of multiple PCB defect types
- Interactive Streamlit interface for visualization
- High precision and inference speed
- GPU acceleration for industrial deployment
- Reduces manual inspection dependency by >80%

---

## 🌟 Results
- Accurately detected single and multiple defects including missing holes, open circuits, and mouse bites.
- Demonstrated industrial-grade reliability with high precision and recall.
- Significantly reduces human inspection errors and time.

---

## 🔮 Future Enhancements
- Detection of overlapping and micro-defects
- Support for multispectral PCB inspection
- Deploy the model as a REST API for seamless manufacturing integration
- Implement feedback learning from user inputs

---

## 👤 Author
**Kadiri Sandeyya**  
- 📧 **Email**: kadirisamson81@gmail.com
- 💼 **LinkedIn**: [My Linkedin Profile](https://www.linkedin.com/in/kadirisandeyya)
=======
# PCB-DEFECT-DETECTION
AI-powered system for real-time detection of PCB defects (missing holes, solder bridges, open circuits) using YOLOv8. Features high-precision, GPU-accelerated inference and an interactive Streamlit interface, reducing manual inspection and enabling scalable industrial deployment.
>>>>>>> e885703 (Initial commit)
=======
# PCB-DEFECT-DETECTION
=======
# PCB-DEFECT-DETECTION
AI-powered system for real-time detection of PCB defects (missing holes, solder bridges, open circuits) using YOLOv8. Features high-precision, GPU-accelerated inference and an interactive Streamlit interface, reducing manual inspection and enabling scalable industrial deployment.
>>>>>>> e885703f90809fcaeacb6a0501cfb3ed82ec9523
>>>>>>> c5e7b077c8ec5e6da748dcbee31dedd23d968455
