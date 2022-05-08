import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 主页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# 上传    
@app.route('/file', methods=['GET', 'POST'])
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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
 #           return redirect(url_for('download_file', name=filename))
    All_file = os.listdir('/home/pandapirate/flask/myproject/uploads/')
    return render_template('file.html', All_file=All_file)

#下载
from flask import send_from_directory
@app.route('/uploads/<name>', methods=['POST'])
def download(name):
    return send_from_directory('/home/pandapirate/flask/myproject/uploads/',
            name, as_attachment=True)

