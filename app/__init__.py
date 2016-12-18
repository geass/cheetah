# -*- coding: utf-8 -*-
__version__ = '0.1'

# Import flask and template operators
from flask import Flask, render_template

# Define the WSGI application object
app = Flask('cheetah')

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_ec2.controllers import mod_ec2 as ec2_module

# Register blueprint(s)
app.register_blueprint(ec2_module)
# app.register_blueprint(xyz_module)
# ..
# 



