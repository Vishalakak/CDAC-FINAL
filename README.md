# 🏭 Smart Manufacturing: Machine Efficiency Prediction

This project uses Machine Learning to predict the efficiency of manufacturing machines (High, Medium, Low) based on operational data. It is designed to support smart factories with real-time insights for optimizing production and maintenance.

---

## 🚀 Features

- Predict machine efficiency: **High**, **Medium**, **Low**
- Web-based UI built using **HTML**, **CSS**, **Flask**, and **Django**
- Trained using **Random Forest Classifier**
- Modular architecture for easy updates and scaling
- Docker support for deployment

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python, Flask, Django
- **ML Framework**: Scikit-learn, Pandas, NumPy
- **Deployment**: Docker (optional)

---

## 📁 Project Structure
CDAC-FINAL/
├── templates/ # HTML templates for Flask/Django
├── static/ # CSS files and static assets
├── app.py # Flask app entry point

├── model
│ └── model.pkl # Trained Random Forest model
├── data/
│ └── machine_data.csv # Dataset used for training
├── requirements.txt # Required Python packages
├── Dockerfile # Docker configuration
├── README.md # Project overview (you are here)



---

## 📊 Dataset

The dataset includes features like:
- Machine type
- Operation time
- Output rate
- Maintenance logs

### Labels:
- `High` — Optimal performance
- `Medium` — Acceptable but can be improved
- `Low` — Needs attention/maintenance

---

## 🧠 Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Accuracy**: ~93% on test data
- **Reason for selection**:
  - Robust with noisy data
  - Good for both classification and feature importance analysis

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Vishalakak/CDAC-FINAL.git
cd CDAC-FINAL

Contributions
Feel free to fork the project, make enhancements, and submit a pull request.

📬 Contact
Vishal
📧 vishalkumarsksk123@gmail.com




