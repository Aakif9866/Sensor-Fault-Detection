# entry for everything

# this code just copy pasted
from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging as lg
import os, sys

from src.pipeline.train_pipeline import TrainingPipeline
from src.pipeline.predict_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Application</h1>
    <p>This is a Machine Learning web application. Follow the steps below:</p>
    <ol>
        <li><strong>Step 1:</strong> <a href="/train">Click here to train the model</a>. Wait for training to complete.</li>
        <li><strong>Step 2:</strong> <a href="/predict">Click here to go to the prediction page</a>. Upload your CSV file to get predictions.</li>
    </ol>
    """

@app.route("/train")
def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return "Training Completed."
    except Exception as e:
        raise CustomException(e, sys)

@app.route('/predict', methods=['POST', 'GET'])
def upload():
    try:
        if request.method == 'POST':
            prediction_pipeline = PredictionPipeline(request)
            prediction_file_detail = prediction_pipeline.run_pipeline()

            lg.info("Prediction completed. Downloading prediction file.")
            return send_file(prediction_file_detail.prediction_file_path,
                             download_name=prediction_file_detail.prediction_file_name,
                             as_attachment=True)
        else:
            return render_template('upload_file.html')
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)

    

# Imports and Setup:

# Flask is used to create the web application.
# CustomException and logging (lg) handle errors and logs.
# TrainingPipeline and PredictionPipeline handle training and prediction workflows.
# Flask App Initialization:

# app = Flask(__name__): Initializes the Flask app.
# Routes:

# / (Home):
# Returns a welcome message.
# /train:
# Executes the TrainingPipeline to train the model.
# Returns "Training Completed." if successful.
# /predict:
# Supports file uploads for predictions.
# POST: Runs the PredictionPipeline, downloads the prediction results as a file.
# GET: Displays an upload form (upload_file.html).
# Error Handling:

# Wraps the logic in try-except blocks to handle errors with CustomException.
# App Execution:

# Runs on localhost (or any host) at port 5000 in debug mode.