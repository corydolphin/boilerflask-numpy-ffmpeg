from flask import Flask, render_template, request
#from boilerflask.models import User
#from boilerflask.forms import (LoginForm)
from boilerflask import app #, loginManager, crypt, db, cache
import utils
from numpy import *
import subprocess

@app.route('/', methods=['GET'] )
def index():
    return render_template('index.html')

@app.route('/test')
def testffmpeg():
	which_res = subprocess.check_output("which ffmpeg", shell=True)
	help_res  = subprocess.check_output("ffmpeg", shell=True)
	numpy_res = "Numpy Version is %s" % numpy.__version__
	return render_template('index.html', messages=[res,help_res])



@app.errorhandler(404)
def page_not_found(error):
    return 'Cory should really handle this page_not_found'


@app.errorhandler(403)
def forbidden(error):
    return 'Cory should really handle this forbidden'


@app.errorhandler(500)
def internal_server_error(error):
    return 'Cory should really handle this internal server error'
