#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request
import os

import document_generator

class RF_doc_browser:
    def __init__(self, directory):
        self.directory = directory
        self._index = None

    @property
    def index(self):
        return document_generator.recursively_find_files(".robot", self.directory)

def create_app():
    rf_doc_browser = RF_doc_browser("files")
    app = Flask(__name__)
    
    @app.context_processor
    def context_processor():
        return dict(file_index=rf_doc_browser.index)

    @app.route("/")
    def index():
        return render_template("index.html", files=rf_doc_browser.index)

    @app.route("/page")
    def page():
        target_file = request.args.get("file")
        return render_template("page.html", iframe="/documentation?file={}".format(target_file))

    @app.route("/documentation")
    def documentation():
        target_file = request.args.get("file")
        document_generator.generate_documentation(target_file, "tmp/files/test.html")
        with open("tmp/files/test.html") as f:
            return f.read()

    app.run()
    return app


if __name__ == "__main__":
    create_app()
