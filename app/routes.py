import os
from flask import Blueprint, render_template, request, current_app
from .whisper_service import transcribe_audio

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    transcription = None

    if request.method == "POST":
        file = request.files["audio"]
        filepath = os.path.join(current_app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        transcription = transcribe_audio(filepath)

    return render_template("index.html", transcription=transcription)