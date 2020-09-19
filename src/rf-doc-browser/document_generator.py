#!/usr/bin/env python3


from robot.libdocpkg import LibraryDocumentation
import os
import re
from tempfile import mkstemp


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
    LibraryDocumentation(file).save(fname, "html")
    with open(fname, "r") as f:
        content = f.read()
    os.close(fd)
    os.remove(fname)
    return content

def get_keywords(file):
    doc = LibraryDocumentation(file)
    return doc.keywords

if __name__ == "__main__":
    files = recursively_find_files([".robot", ".py"], "files")
    # os.makedirs("tmp", exist_ok=True)
    # for f in files:
    f = "files\\python_library.py"
    # LibraryDocumentation(f).save("tmp\\files\\test.html", "html")
    print(generate_documentation(f))
    
    # for f in files:
    #     get_keywords(f)

