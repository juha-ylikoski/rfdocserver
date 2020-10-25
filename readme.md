# rfdocserver

This python modules goal is to make browsing robot framework keyword documentation easier by generating browseable documentation with robot framework libdoc and host it with flask web server.

## Installation

You can install this package with pip:

`pip3 install rfdocserver`


## Running

This project should be run as python3 module.

`python3 -m rfdocserver --robot_files <path to robot file root>`


## Features

- Robot framework keyword documentation generation
- Displaying documentation on web server
- Keyword search
- Input files can be python modules or path to them
  - Will recursively find files suitable for document creation if path is given
- Can detect changes and regenerate documentation for files which are included via path
  - No need to reload this program to apply changes to your documentation
