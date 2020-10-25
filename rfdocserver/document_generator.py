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


from robot.libdocpkg import LibraryDocumentation
import os
import sys
import re
from tempfile import mkstemp
import logging


class LibdocError(Exception):
    pass

def recursively_find_files(whitelist, blacklist, path):
    file_paths = []
    for root, dirs, files in os.walk(path):
        for f in files:
            for regex in whitelist:
                if re.search(regex, f):
                    blacklisted = False
                    for item in blacklist:
                        if re.search(item, f):
                            blacklisted = True
                            break
                    if not blacklisted:
                        file_paths.append(os.path.join(root, f))
                        break

    return file_paths

def generate_documentation(file):
    """Generate robot framework html documentation for file

    Args:
        file (filepath): filepath to robot resource/library

    Returns:
        string: html documentation for the file
    """
    # Using tempfile is required because robot libdoc wants path-like-object
    fd, fname = mkstemp()
    try:
        LibraryDocumentation(file).save(fname, "html")
    except Exception as e:
        logging.warning("Was not able to generate documentation for {}. Got error {}".format(file, e))
        raise LibdocError(str(e))
    with open(fname, "r") as f:
        content = f.read()
    os.close(fd)
    os.remove(fname)
    return content

def get_keywords(file):
    doc = LibraryDocumentation(file)
    return doc.keywords

def get_documentation(file):
    try:
        return LibraryDocumentation(file)
    except Exception as e:
        logging.warning("Was not able to generate documentation for {}. Got error {}".format(file, e))
        raise LibdocError(str(e))

