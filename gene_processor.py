__author__ = 'Michael Kern'

# module to load own configurations
import caleydo_server.config

# request config
#config = caleydo_server.config.view('gene_server')

class GeneProcessor(object):
  def __init__(self):
    print('GeneProcessor.__init__ invoked ...')
    pass

  def __call__(self):
    print('GeneProcessor.__call__ invoked ...')
    return {'data': [1, 2, 3, 4]}


def _plugin_initialize():
  pass


def create():
  return GeneProcessor()
