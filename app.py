from flask import Flask, render_template, jsonify, request, send_file
from src.exception import CustomException
from src.logger import logging
import os,sys
from src.pipeline.train_pipeline import TrainingPipeline

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my application"

@app.route("/train")
def train_route():
    try:
        train_pipeline=TrainingPipeline()
        train_pipeline.run_pipeline()
        
        return "Training Complete"
    
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)