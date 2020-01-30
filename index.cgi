#!/home/medalmarket/.pyenv/versions/3.6.4-flask/bin/python

import cgitb 
cgitb.enable()

from wsgiref.handlers import CGIHandler
from app import app 
CGIHandler().run(app)
