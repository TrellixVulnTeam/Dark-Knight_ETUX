# This file is generated by numpy's setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]


import os
import sys

extra_dll_dir = os.path.join(os.path.dirname(__file__), '.libs')

if sys.platform == 'win32' and os.path.isdir(extra_dll_dir):
    if sys.version_info >= (3, 8):
        os.add_dll_directory(extra_dll_dir)
    else:
        os.environ.setdefault('PATH', '')
        os.environ['PATH'] += os.pathsep + extra_dll_dir

blas_mkl_info={}
blis_info={}
openblas_info={'library_dirs': ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas'], 'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)]}
blas_opt_info={'library_dirs': ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas'], 'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)]}
lapack_mkl_info={}
openblas_lapack_info={'library_dirs': ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas'], 'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)]}
lapack_opt_info={'library_dirs': ['C:\\projects\\numpy-wheels\\numpy\\build\\openblas'], 'libraries': ['openblas'], 'language': 'f77', 'define_macros': [('HAVE_CBLAS', None)]}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
