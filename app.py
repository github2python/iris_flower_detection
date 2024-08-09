from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
CORS(app)  # This will allow all origins

model = load_model('iris_dt.keras')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        predicted_class = np.argmax(prediction, axis=1)[0]
        return jsonify({'prediction': int(predicted_class)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
