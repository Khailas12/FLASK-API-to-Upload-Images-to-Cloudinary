from flask import Flask, render_template, request, jsonify
import cloudinary
import cloudinary.uploader
import cloudinary.api
import logging
from cloudinary.utils import cloudinary_url
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import os


load_dotenv()   # Loading API keys etc...
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)
app.logger.info("%s", os.getenv("CLOUD_NAME"))


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
@cross_origin()
def upload_file():
    app.logger.info("in upload route")
    cloudinary.config(cloud_name = os.getenv("CLOUD_NAME"), api_key=os.getenv("API_KEY"), api_secret=os.getenv("API_SECRET"))
    upload_result = None
    
    if request.method == "POST":
        file_to_upload = request.files["file"]
        app.logger.info("%s file_to_upload", file_to_upload)
        if request.method == "POST":
            file_to_upload = request.files["file"]
            app.logger.info("%s file_to_upload", file_to_upload)
            if file_to_upload:
                upload_result = cloudinary.uploader.upload(file_to_upload)
                app.logger.info(upload_result)
                return jsonify(upload_result)


@app.route("/cld_optimize", methods=["POST"])
@cross_origin()
def cld_optimize():
    app.logger.info("in optmize route")
    
    cloudinary.config(cloud_name = os.getenv("CLOUD_NAME"), api_key=os.getenv("API_KEY"), api_secret=os.getenv("API_SECRET"))
    if request.method == "POST":
        public_id = request.form["public_id"]
        app.logger.info("%s public id", public_id)
        if public_id:
            cloud_url = cloudinary_url(public_id, fetch_format="auto", quality="auto", secure=True)
            upl = app.logger.info(cloud_url)

            return jsonify(cloud_url)



if __name__ == "__main__":
    app.run(debug=True, port=5000)