from flask import request, render_template, redirect, url_for, flash
from core.plagiarism_checker import check_plagiarism
from core.utils import save_uploaded_files
import os


def init_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            if "files" not in request.files:
                flash("No file part in the request.", "error")
                return redirect(request.url)

            files = request.files.getlist("files")
            uploaded_files = save_uploaded_files(
                files,
                app.config["UPLOAD_FOLDER"],
                app.config["ALLOWED_EXTENSIONS"],
            )

            if not uploaded_files:
                flash(
                    "No valid files uploaded. Please upload valid text files.", "error"
                )
                return redirect(request.url)

            results = check_plagiarism(uploaded_files)

            return render_template("results.html", results=results)

        return render_template("index.html")

    @app.errorhandler(413)
    def request_entity_too_large(error):
        flash("Uploaded files exceed the maximum size limit.", "error")
        return redirect(url_for("index"))
