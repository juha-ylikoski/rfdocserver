#!/usr/bin/env python3


from robot.libdocpkg import LibraryDocumentation
import os
import re
from io import StringIO


def recursively_find_files(regexs, path):
    file_paths = []
    for root, dirs, files in os.walk(path):
        for f in files:
            for regex in regexs:
                if re.search(regex, f):
                    file_paths.append(os.path.join(root, f))
                    break

    return file_paths

def generate_documentation(file, out):
    LibraryDocumentation(file).save(out, "html")

def get_keywords(file):
    doc = LibraryDocumentation(file)
    return doc.keywords

if __name__ == "__main__":
    files = recursively_find_files([".robot", ".py"], "files")
    # os.makedirs("tmp", exist_ok=True)
    # for f in files:
    f = "files\\test_copy.robot"
    LibraryDocumentation(f).save("tmp\\files\\test.html", "html")
    # for f in files:
    #     get_keywords(f)

