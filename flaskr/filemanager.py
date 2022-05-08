import os, functools
from flask import Flask, flash, request, redirect, url_for, render_template, Blueprint
from werkzeug.utils import secure_filename

bp = Blueprint('file', __name__, url_prefix='/filemanager')

 # UPLOAD_FOLDER = '../file'
DOWNLOAD_FOLDER = '/home/pandapirate/flask/myproject/file/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
'''
# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
'''
# 上传    
@bp.route('/file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            file.save(os.path.join(DOWNLOAD_FOLDER, file.filename))
 #           return redirect(url_for('download_file', name=filename))
    All_file = os.listdir(DOWNLOAD_FOLDER)
    return render_template('file.html', All_file=All_file)

#下载
from flask import send_from_directory
@bp.route('/file/<name>', methods=['GET', 'POST'])
def download(name):
    return send_from_directory(DOWNLOAD_FOLDER, name, as_attachment=True)
#app.run(host='0.0.0.0',port=5000,debug=True)

