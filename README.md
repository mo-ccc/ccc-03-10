This is a fully functional crud api for a postgresql database built in python using flask.
It implements the mvc pattern and schemas.

# installation instructions
- clone this repository
- ensure u have python3 on your local machine
- change directory into this repository
- create a python3 virtual environment: python -m venv venv
- activate the virtual environment: venv/bin/activate on linux 
- pip install -r requirements.txt
- rename .env.example to .env and edit the fields
- fill in the fields with the required info
- set the FLASK-APP environment variable: FLASK_APP=main.py on linux
- run the flask app: flask run