Bottle Scaffold
===============
Files structure skeleton for web apps in bottle microframework

Structure
=========
  - db            - SQLite files
  - lib           - external libraries and application code
  - static        - assets (js, css, img)
  - static/js/lib - external js libraries (for development purpose)
  - views         - templates go there

Makefile
========
Contains two targets:
  - run to actually run the code on localhost
  - lint to run pychecker and jslint

Dependencies
============
pychecker
node.js
jslint
make

License
=======
The code is published under BSD 3-clause license.
