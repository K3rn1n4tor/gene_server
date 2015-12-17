__author__ = 'Michael Kern'

def print_test():
  return 'This is a test!'

# def print_debug(message):
#   # import plugin module
#   import caleydo_server.plugin
#
#   impls = []
#   plugins = caleydo_server.plugin.list('gene_type')
#
#   for p in plugins:
#     impl = p.load().factory()
#     impls.append(impl(message))
#
#   return impls

def test_data(dataset_id):
  import caleydo_server.dataset as dt
  test = dt.get(dataset_id)

  print test._loaded['data']



def array_debug():
  # import plugin module
  import caleydo_server.plugin
  plugins = caleydo_server.plugin.list('gene_type')
  data = []

  for p in plugins:
    impl = p.load().factory()
    data = impl()

  return data

