#!/bin/sh

find . -maxdepth 1 -name "*.ui" -exec sh -c 'pyuic5 "$1" > "${1%.ui}.py"' _ {} \;
