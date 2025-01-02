import subprocess
from flask import (
    Response, Blueprint, json, request, redirect, send_file,  url_for,  render_template, 
)
import logging
from werkzeug.utils import secure_filename
from .db import get_db



bp = Blueprint('api', __name__, url_prefix='/api')
logging.getLogger('flask_cors').level = logging.DEBUG



@bp.route('/', methods=('GET', 'POST'))
def create():
    output = None
    if request.method == 'POST':
        command = request.form.get('command')
        try:
            output = subprocess.check_output(command, shell=True, text=True) # type: ignore
        except subprocess.CalledProcessError as e:
            output = f"Error: {e}"
    return render_template('proc/index.html', output=output)
