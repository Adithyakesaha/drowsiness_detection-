# drowsiness_detection-
Driver Safety Monitoring System – An AI-powered driver monitoring solution that detects drowsiness, distraction, and unsafe driving behavior using computer vision and deep learning to improve road safety 
## Dataset

This project requires a dataset to train and evaluate the AI models for driver drowsiness and distraction detection. Due to GitHub's file size limitations, the dataset is **not included** in this repository.

### Supported Datasets

* Driver Drowsiness Detection Dataset
* Eye State (Open/Closed) Dataset
* Yawning Detection Dataset
* Facial Landmark Dataset

### How to Add the Dataset

1. Download the required dataset from the appropriate source.
2. Create a folder named `dataset` in the project root.
3. Copy all dataset files into the `dataset` folder.
4. Update the dataset path in the training or configuration file if necessary.
5. Run the training script before starting the application.

**Note:** The dataset is excluded from this repository because of GitHub's storage limits. Please download it separately and place it in the `dataset` directory before running the project.

## Dataset

This project requires a dataset to train and evaluate the AI models for driver drowsiness and distraction detection. Due to GitHub's file size limitations, the dataset is **not included** in this repository.

### Supported Datasets

* Driver Drowsiness Detection Dataset
* Eye State (Open/Closed) Dataset
* Yawning Detection Dataset
* Facial Landmark Dataset

### How to Add the Dataset

1. Download the required dataset from the appropriate source.
2. Create a folder named `dataset` in the project root.
3. Copy all dataset files into the `dataset` folder.
4. Update the dataset path in the training or configuration file if necessary.
5. Run the training script before starting the application.

**Note:** The dataset is excluded from this repository because of GitHub's storage limits. Please download it separately and place it in the `dataset` directory before running the project.
# How to Run the Driver Safety Project

## Prerequisites

* Python 3.10 or later
* pip
* Webcam
* Git

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/driver-safety.git
cd driver-safety
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Download the required AI models and dataset, then place them in the appropriate folders (for example, `models/` and `dataset/`).

4. Run the application:

```bash
python app.py
```

Or, if your project uses FastAPI:

```bash
uvicorn app:app --reload
```

5. Open your browser (if applicable) and visit:

```
http://127.0.0.1:8000
```

The application will access your webcam and start monitoring the driver's alertness, detecting drowsiness, distraction, and unsafe behavior in real time.

