__author__ = 'Michael Kern'

# use flask for server
import flask
from .gene_processor_service import *

# create Flask app for hosting namespace
app = flask.Flask(__name__)

# at route/test web request, return string
@app.route('/test/<dataset_id>')
def _test_print(dataset_id):
  test_data(dataset_id)
  #print request
  #data = array_debug()
  #return flask.jsonify(array_debug())
  #return print_test()
  #return _test_debug('Michael')

#def _test_debug(name):
  #return '\n'.join(print_debug(name))

# std convection for creating the service
# must returns the plugin implementation
def create():
  return app
