#!/usr/bin/env python3

from flask import Flask, render_template, url_for, request
import os
import re

import document_generator


class RF_doc_browser:
    def __init__(self, directory):
        self.directory = directory
        self._index = None

    @property
    def index(self):
        index = document_generator.recursively_find_files(".robot", self.directory)
        print(index)
        return index
    
    def get_keyword_names(self, file):
            keywords = document_generator.get_keywords(file)
            names = []
            for keyword in keywords:
                names.append(keyword.name)
            return names

    def get_keywords(self, file):
        return document_generator.get_keywords(file)
    
    def search(self, search_input):
        matches = []
        for file in self.index:
            for keyword in self.get_keywords(file):
                if re.search(search_input, keyword.name, re.IGNORECASE):
                    matches.append(keyword)
            print("Got matches:")
            print(", ".join(keyword.name for keyword in matches))
        return matches


def create_app():
    rf_doc_browser = RF_doc_browser("files")
    app = Flask(__name__)
    
    @app.context_processor
    def context_processor():
        return dict(
            file_index=rf_doc_browser.index,
            get_keyword_names=rf_doc_browser.get_keyword_names,
            get_keyword=rf_doc_browser.get_keywords,
            search=rf_doc_browser.search
            )

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

    @app.route("/search", methods=['POST'])
    def search_redirect():
        search_input = request.form['search_input']
        print(search_input)
        return render_template("search.html", search_results=rf_doc_browser.search(search_input))
    


    app.run()
    return app


if __name__ == "__main__":
    create_app()
