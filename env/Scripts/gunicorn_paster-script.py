#!C:\Users\lenovo\flask_heroku\env\Scripts\python2.7.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gunicorn==0.17.4','console_scripts','gunicorn_paster'
__requires__ = 'gunicorn==0.17.4'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('gunicorn==0.17.4', 'console_scripts', 'gunicorn_paster')()
    )
