import os

# name = 'eqt_ext'
__import__("pkg_resources").declare_namespace(__name__)

def get_eqt_ext_static_dir():
    return os.path.join(os.path.dirname(__file__), '_static')
