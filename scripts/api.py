from flask import (
    Response, Blueprint, request, redirect, send_file,  url_for,  render_template, 
)
from flask import flash
import os
import logging
from werkzeug.utils import secure_filename



bp = Blueprint('api', __name__, url_prefix='/api')
ALLOWED_EXTENSIONS = {'mp4', 'png', 'jpg', 'jpeg', 'gif'}
logging.getLogger('flask_cors').level = logging.DEBUG

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route("/")
def hello():
    return "Hello, World!"



@bp.route('/uploads', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # type: ignore
            file.save(os.path.join( 'flaskr/static/uploads',filename))
            alpr_file = (os.path.join('flaskr/static/uploads', filename))
            return redirect(url_for('api.upload_file'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''