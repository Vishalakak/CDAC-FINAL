from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
with open("model.pkl", "rb") as f1:
    model = pickle.load(f1)

with open("scaler.pkl", "rb") as f2:
    scaler = pickle.load(f2)
    
FEATURES = [
                'Operation_Mode', 'Temperature_C', 'Vibration_Hz',
                'Power_Consumption_kW', 'Network_Latency_ms', 'Packet_Loss_%',
                'Quality_Control_Defect_Rate_%', 'Production_Speed_units_per_hr',
                'Predictive_Maintenance_Score', 'Error_Rate_%'
            ]

LABELS = {
    0:"High",
    1:"Low",
    2:"Medium"
}
# Dictionary of placeholders for each feature
placeholders = {
    'Operation_Mode': 'low-1,med-2,high-3',
    'Temperature_C': 'Enter the temprature',
    'Vibration_Hz': 'Enter in range(0.1-5)',
    'Power_Consumption_kW': 'Enter in range(1-10)',
    'Network_Latency_ms': 'Enter in range(1-50)',
    'Packet_Loss_%': 'e.g., 0.5....to 5',
    'Quality_Control_Defect_Rate_%': 'Enter in range(1-10)',
    'Production_Speed_units_per_hr': 'e.g., 1000',
    'Predictive_Maintenance_Score': 'e.g., 85',
    'Error_Rate_%': 'e.g., 1.2',
    
}


@app.route("/" , methods=["GET" , "POST"])
def index():
    prediction = None

    if request.method=="POST":
        try:
            input_data = [float(request.form[feature]) for feature in FEATURES]
            input_array = np.array(input_data).reshape(1,-1)

            scaled_array = scaler.transform(input_array)

            pred = model.predict(scaled_array)[0]
            prediction = LABELS.get(pred , "Unknown")

        except Exception as e:
            prediction = f"Error : {e}"

    return render_template('index.html', features=FEATURES, placeholders=placeholders, prediction=prediction)


if __name__=="__main__":
    app.run(debug=True , host="0.0.0.0" , port=5000)