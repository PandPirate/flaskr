import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
@app.route('/')
def download_file():
    All_file = os.listdir('/home/pandapirate/flask/myproject/uploads/')
    return render_template('download.html', All_file=All_file)
@app.route('/uploads/<name>')
def download(name):
    return send_from_directory('/home/pandapirate/flask/myproject/uploads/',
            name, as_attachment=True)
