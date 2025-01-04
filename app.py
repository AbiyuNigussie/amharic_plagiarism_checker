from flask import Flask, request, render_template, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from main import check_plagiarism

UPLOAD_FOLDER = "./uploaded_docs"
ALLOWED_EXTENSIONS = {"txt"}

app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "files" not in request.files:
            flash("No file part")
            return redirect(request.url)

        files = request.files.getlist("files")
        uploaded_files = []

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                file.save(filepath)
                uploaded_files.append(filepath)

        if not uploaded_files:
            flash("No valid files were uploaded.")
            return redirect(request.url)

        results = check_plagiarism(uploaded_files)

        return render_template("results.html", results=results)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
