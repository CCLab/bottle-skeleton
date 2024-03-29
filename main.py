#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

from app.lib.bottle import install, route, run, template, request, static_file
from app.lib.bottle_sqlite import SQLitePlugin

DEBUG = True


# -- routes
@route('/')
def index():
    return template( 'index', {'title': 'CCLab scaffold'} )



@route('/static/<path:path>')
def serve_files( path ):
    return static_file( path , root='./static/' )


# -- run the app
if __name__ == '__main__':
    cur_path = os.path.dirname( __file__ )
    if DEBUG:
        db_path = os.path.join( cur_path, 'db', 'dev.db' )
    else:
        db_path = os.path.join( cur_path, 'db', 'production.db' )

    install( SQLitePlugin(dbfile=db_path) )

    if len( sys.argv ) == 2:
        if sys.argv[1] == 'dev':
            run( host='localhost', port=8080 )
        else:
            print 'python main.py <dev>'
