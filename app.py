
import os
import sys

from flask import Flask, render_template, send_from_directory, request\
, flash, redirect, url_for

from werkzeug import secure_filename

from flask.ext.bootstrap import Bootstrap

from matapdf import clean_pdf

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/<name>')
def send_back_pdf(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=name)
    
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file.filename.split('.')[-1] == 'pdf':
        name = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], name))
        name = clean_pdf(os.path.join(app.config['UPLOAD_FOLDER'], name))
        return redirect(url_for('.send_back_pdf', name=name))
    else:
        flash('Your file does not seem valid')
        return redirect(url_for('.index'))

@app.route('/static/<folder>/<name>')
def serve(folder, name):
    '''
    Only for developing purpose
    '''
    return send_from_directory(os.path.join(sys.path[0], 'static', folder), filename=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
