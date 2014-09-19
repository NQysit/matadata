
import os
import sys
import time

from flask import Flask, render_template, send_from_directory, request\
, flash, redirect, url_for, make_response, session

from werkzeug import secure_filename

from flask.ext.bootstrap import Bootstrap

from matapdf import clean_pdf

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def index():
    if 'ready' in session:
        ready = session['ready']
        del session['ready']
    else:
        ready = False
    return render_template('index.html', ready=ready)

@app.route('/your_pdf_is_ready')
def download_pdf():
    if 'path' in session:
        path, name = os.path.split(session['path'])
        response = make_response(send_from_directory(path, filename=name))
        os.remove(session['path'])
        del session['path']
        return response
    return redirect(url_for('.index'))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    name = secure_filename(file.filename)
    if name.endswith('.pdf'):
        path = os.path.join(app.config['UPLOAD_FOLDER'], name)
        file.save(path)
        session['path']  = clean_pdf(path)
        session['ready'] = True
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
