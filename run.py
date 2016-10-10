#!/home/ec2-user/eb-virt/local/lib/python2.7/site-packages/flask
from app import app
import logging
from logging.handlers import RotatingFileHandler
handler = RotatingFileHandler("record.log", maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)
app.run(debug=True)