import subprocess
from flask import (
    Response, Blueprint, json, jsonify, request,flash, redirect, send_file,  url_for,  render_template, 
)
from subprocess import PIPE, Popen, check_output

import logging
from werkzeug.utils import secure_filename
from .db import get_db
from .auth import login_required



bp = Blueprint('cmd', __name__, url_prefix='/cmd')
logging.getLogger('flask_cors').level = logging.DEBUG


@bp.route('/test', methods=('GET', 'POST'))
def create_test():
    if request.method == 'POST':
        request_data = request.get_json()
        print((request_data))
        data = request_data
    return jsonify(data)    






@bp.route('/i', methods=('GET', 'POST'))
@login_required
def create_i():
    if request.method == 'POST':
        request_data = request.get_json()
        data = request_data
        command = data
        #command = request.form.get('command')
        try:
            output = subprocess.check_output(command, shell=True, text=True) # type: ignore
            print((output))
        except subprocess.CalledProcessError as e:
            output = f"Error: {e}"
    #return("2222") 
    return jsonify(output)    




@bp.route('/h', methods=('GET', 'POST'))
@login_required
def create_h():
    output = None
    if request.method == 'POST':
        #command = request.form.get('command')
        command = 'uname'
        try:
            output = subprocess.check_output(command, shell=True, text=True) # type: ignore
            jl = json.loads(output)
            print(type(output))
        except subprocess.CalledProcessError as e:
            output = f"Error: {e}"
    return render_template('index.html', output=output)









@bp.route('/', methods=('GET', 'POST'))
@login_required
def create():
    output = None
    if request.method == 'POST':
        command = request.form.get('command')
        try:
            output = subprocess.check_output(command, shell=True, text=True) # type: ignore
            print(type(output))
        except subprocess.CalledProcessError as e:
            output = f"Error: {e}"
    return render_template('cmd/index.html', output=output)


