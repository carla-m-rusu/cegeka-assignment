import os
from flask import json

SECTION_NOT_FOUND = 'Section not in CV. Valid values are: about, personal, experience, education, skills and languages.'
FILE_NOT_FOUND = 'The CV file could not be located.'
INDEX = 'Pages you can navigate to: about, personal, experience, education, skills and languages.'


def load_cv(section=None):
    basedir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(basedir, "static/data", "cv.json")

    try:
        with open(file) as cv_file:
            cv = json.load(cv_file)
            return cv if not section else cv.get(section) if cv.get(section) else (SECTION_NOT_FOUND, 404)
    except FileNotFoundError:
        return FILE_NOT_FOUND, 500
