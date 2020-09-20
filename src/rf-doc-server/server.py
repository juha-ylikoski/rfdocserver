#!/usr/bin/env python3
# Copyright (C) 2020 -  Juha Ylikoski

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from flask import Flask, render_template, url_for, request, Markup
import os
import re
import argparse
from bs4 import BeautifulSoup


from . import document_generator


class RF_doc_server:
    def __init__(self, directory):
        self.directory = directory
        self._index = None

    @property
    def index(self):
        index = document_generator.recursively_find_files([".robot", ".py"], [".pyc"], self.directory)
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
        return matches


def create_app(directory):
    rf_doc_server = RF_doc_server(directory)
    app = Flask(__name__)
    rf_doc_server.index
    
    @app.context_processor
    def context_processor():
        return dict(
            file_index=rf_doc_server.index,
            get_keyword_names=rf_doc_server.get_keyword_names,
            get_keyword=rf_doc_server.get_keywords,
            search=rf_doc_server.search
            )

    @app.route("/")
    def index():
        return render_template("index.html", files=rf_doc_server.index)

    @app.route("/page")
    def page():
        target_file = request.args.get("file")
        documentation = document_generator.generate_documentation(target_file)
        soup = BeautifulSoup(documentation, features="html.parser")
        head = soup.head
        head_styles = []
        for style in head.find_all("style"):
            head_styles.append(Markup(style))

        head_scripts = []
        for script in head.find_all("script"):
            head_scripts.append(Markup(script))

        body = soup.body
        body_divs = [Markup(soup.body.find_all("div", id="javascript-disabled")[0])]
        
        body_scripts = []
        for script in body.find_all("script"):
            if "id" in script.attrs.keys():
                if script.attrs["id"] == "base-template":
                    script = str(script).split("\n")
                    script = [script[0]] + ['<div class="content">', '<div class="content-window">'] + script[1:-1] + ["</div>", "</div>"] + [script[-1]]
                    script = "\n".join(script)
            body_scripts.append(Markup(script))

        return render_template("page.html",
                                head_styles=head_styles,
                                head_scripts=head_scripts,
                                body_divs=body_divs,
                                body_scripts=body_scripts
                                )

    @app.route("/documentation")
    def documentation():
        target_file = request.args.get("file")
        return document_generator.generate_documentation(target_file)

    @app.route("/search", methods=['POST'])
    def search_redirect():
        search_input = request.form['search_input']
        return render_template("search.html", search_results=rf_doc_server.search(search_input))
    


    app.run()
    return app

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("robot_files")
    args = argument_parser.parse_args()
    create_app(args.robot_files)

if __name__ == "__main__":
    main()
