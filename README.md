# 👁️ Elevate Vision

**Elevate Vision** is an advanced object detection and inventory analysis tool powered by computer vision. It uses state-of-the-art YOLOv8 neural networks to detect objects in images, count inventory, and provide real-time analysis in a user-friendly interface.

🚀 **Live Demo:** [Click here to try the App](https://jbahulika-mselevate-object-detection-app-erj6na.streamlit.app/)

---

## 📜 Project Overview

This application was developed as part of the **Microsoft Elevate Project (2026)**. The goal was to build a robust computer vision system capable of identifying objects and generating automated inventory reports from static images.

### Key Features
* **🧠 Adjustable AI Intelligence:** Choose between three distinct model sizes based on your needs:
    * *Nano:* Fast & Lightweight (yolov8n)
    * *Medium:* Balanced performance (yolov8m)
    * *Large:* High Accuracy (yolov8l)
* **🛡️ Precision Control:** A "Strictness" slider allows users to adjust the confidence threshold (0.0 - 1.0) to filter out false positives or catch smaller, harder-to-see objects.
* **📊 Automated Inventory Report:** Instantly generates a count of all detected classes (e.g., "3 Persons, 1 Car"), making it ideal for stock counting or scene analysis.
* **🖼️ Real-Time Visualization:** Displays the original uploaded photo alongside the AI-processed version with bounding boxes and labels.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Computer Vision:** [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* **Image Processing:** * `Pillow` (PIL) for image handling
    * `OpenCV` (Headless) for underlying vision tasks
* **Analysis:** Python `collections` for inventory counting

---

## ⚙️ Installation & Run Locally

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/JBahulika/Elevate-Vision.git](https://github.com/JBahulika/Elevate-Vision.git)
    cd Elevate-Vision
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

---

## 🧠 How It Works

1.  **Upload:** Users drop a `.jpg`, `.jpeg`, or `.png` file into the upload area.
2.  **Configuration:** The user selects the Model Size and Strictness level from the sidebar.
3.  **Inference:** The app loads the selected YOLOv8 model and runs a prediction on the image.
4.  **Reporting:** * The processed image is plotted with bounding boxes.
    * The `collections.Counter` aggregates the detected class IDs to produce a text-based inventory summary.

---

## 👤 Author

**Bahulika** *Microsoft Elevate Project | 2026*

*Connect with me:* [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/j-bahulika-8b8237207/) 
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/JBahulika)
