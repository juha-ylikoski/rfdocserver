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


from flask import Flask, render_template, url_for, request, Markup, redirect
import os
import re
import argparse
from bs4 import BeautifulSoup
from waitress import serve
import pathlib
import datetime
import logging
import hashlib

import robot.libraries as robot_libraries

from ._version import __version__, __version_info__
from . import document_generator


class RF_doc_server:
    def __init__(self, directory, include_robot_libraries=True, include=[], no_cache=False):
        if directory:
            if directory.startswith(".\\") or directory.startswith("./"):
                directory = directory[2:]
        self._include_robot_libraries = include_robot_libraries
        self.directory = directory
        self._index = None
        self.include = include
        self.no_cache = no_cache
        self.docs = {}
        self.hashes = {}

        self.search_field_content = ""

        self._error_blacklist = None

        self.error_blacklist = []

    
    @property
    def error_blacklist(self):
        return self._error_blacklist
    @error_blacklist.setter
    def error_blacklist(self, value):
        self._error_blacklist = value
        self.populate_blacklist()

    def populate_blacklist(self):
        for item in self.index:
            try:
                self.get_documentation(item)
            except document_generator.LibdocError as e:
                logging.error("Was not able to generate documentation from {}. Got error: {}. Removing {} from index".format(item, str(e).replace("\n", ""), item))
                self._error_blacklist.append(item)


    def file_changed(self, file):
        def md5(fname):
            hash_md5 = hashlib.md5()
            with open(fname, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()

        
        # If python module cannot generate hash and thus cannot determine if changed. Assume it has not changed.
        if not os.path.isfile(file):
            return False

        h = md5(file)
        if file not in self.hashes.keys():
            self.hashes[file] = h
            return True
        changed = h != self.hashes[file]
        self.hashes[file] = h
        return changed
    
    def get_documentation(self, target):
        if (self.file_changed(target) or target not in self.docs.keys()) or self.no_cache:
            logging.debug("Generated documentation for {}".format(target))
            doc = document_generator.get_documentation(target)
            doc.rf_hub_name = target
            self.docs[target] = doc
        return self.docs[target]

    @property
    def index(self):
        if self.directory:
            index = document_generator.recursively_find_files([".robot", ".resource", ".py"], [".pyc"], self.directory)
        else:
            index = []
        if self._include_robot_libraries:
            dirname = os.path.dirname(robot_libraries.__file__)
            for item in os.listdir(dirname):
                if item not in ["__init__.py", "__pycache__"] and item[0].isupper():
                    index.append(item.split(".py")[0])
        for item in self.include:
            index.append(item)
        
        index_with_no_blacklisted_items = []
        for item in index:
            if not item in self.error_blacklist:
                index_with_no_blacklisted_items.append(item)
        return index_with_no_blacklisted_items
    
    def get_keyword_names(self, file):
            keywords = self.get_documentation(file).keywords
            names = []
            for keyword in keywords:
                names.append(keyword.name)
            return names

    def get_keywords(self, file):
        return self.get_documentation(file).keywords
    
    def search(self, search_input):
        matches = []
        for file in self.index:
            for keyword in self.get_keywords(file):
                if re.search(search_input, keyword.name, re.IGNORECASE):
                    keyword.rf_hub_name = self.get_documentation(file).rf_hub_name
                    matches.append(keyword)
        return matches

    def get_libraries(self):
        libraries = []
        for file in self.index:
            doc = self.get_documentation(file)
            if doc.type == "LIBRARY":
                libraries.append(doc)
        return libraries

    def get_resource_files(self):
        libraries = []
        for file in self.index:
            doc = self.get_documentation(file)
            if doc.type == "RESOURCE":
                libraries.append(doc)
        return libraries

    @staticmethod
    def get_link_to_keyword(source_file, keyword_name):
        return "/page?file={}#{}".format(source_file, keyword_name.replace(' ', '%20'))

    @staticmethod
    def get_link_to_library(source_file):
        return "/page?file={}".format(source_file)

    @staticmethod
    def get_synopsis(documentation):
        return documentation.doc.strip().split("\n")[0].replace("``", "")

    @staticmethod
    def get_keyword_count(documentation):
        return len(documentation.keywords)


def create_app(directory, debug=False, include_robot_libraries=True, include=[], no_cache=False):
    rf_doc_server = RF_doc_server(directory, include_robot_libraries=include_robot_libraries, include=include, no_cache=no_cache)
    app = Flask(__name__)
    rf_doc_server.index
    
    @app.context_processor
    def context_processor():
        return dict(
            file_index=rf_doc_server.index,
            rf_doc_server=rf_doc_server,
            get_version=lambda: __version__,
            get_date=lambda: str(datetime.datetime.now().replace(microsecond=0).isoformat())
            )

    @app.route("/")
    def index():
        rf_doc_server.search_field_content = ""
        return render_template("index.html", files=rf_doc_server.index)
    
    @app.route("/reload")
    def reload():
        rf_doc_server.error_blacklist = []
        return redirect("/")

    @app.route("/page")
    def page():
        target_file = request.args.get("file")
        try:
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
                if not "id" in script.attrs.keys():
                    script = re.sub(re.compile(re.escape("renderTemplate('base', libdoc, $('body'));")), "renderTemplate('base', libdoc, $('.content-window'));", str(script))
                body_scripts.append(Markup(script))
        except document_generator.LibdocError:
            head_styles = []
            head_scripts = []
            body_divs = []
            body_scripts = []
        rf_doc_server.search_field_content = ""
        return render_template("page.html",
                                head_styles=head_styles,
                                head_scripts=head_scripts,
                                body_divs=body_divs,
                                body_scripts=body_scripts
                                )

    @app.route("/search", methods=['POST'])
    def search_redirect():
        search_input = request.form['search_input']
        rf_doc_server.search_field_content = search_input
        return render_template("search.html", search_results=rf_doc_server.search(search_input))
    

    if debug:
        app.run(debug=True)
    else:
        serve(app, host="0.0.0.0", port=5000)

def version():
    return "rfdocserver {}".format(__version__)

def main():
    argument_parser = argparse.ArgumentParser(usage="usage: rfdocserver.py [-h] [-v] robot_files")
    argument_parser.add_argument("--robot_files", help="Directory in which robot resource files or libraries exist.")
    argument_parser.add_argument("-v", "--version", action='version', version=version())
    argument_parser.add_argument("--debug", action='store_true', help="Start the server with debug mode.")
    argument_parser.add_argument("--no-include-robot-libraries", action='store_false', help="Does not include robot framework libraries which come with robot.libraries")
    argument_parser.add_argument("--include", help="Include extra library. Format should be python import path. Multiple can be included with ',' separating them")
    argument_parser.add_argument("--no-cache", action='store_true', help="Do not cache documentation. Note this will greatly reduce performance.")
    args = argument_parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname)s %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)-15s %(levelname)s %(message)s')

    if args.include:
        include = args.include.split(",")
    else:
        include = []
    create_app(args.robot_files, debug=args.debug, include_robot_libraries=args.no_include_robot_libraries, include=include, no_cache=args.no_cache)

if __name__ == "__main__":
    main()
