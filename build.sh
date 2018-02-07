#!/bin/sh

# This script builds the SCSS, Typescript, and other static files from source.

clear

echo "CuteKitchen build started..."

echo "  Building stylesheets..."

if  [ ! -d static/css/bin ]
then
    mkdir -p static/css/bin
fi

sass src/scss/bulma.scss static/css/bin/bulma.css
sass src/scss/cutekitchen.scss static/css/bin/cutekitchen.css

echo "-----------------------------------------------------------------------------------"
echo "Build complete - run 'python3 cute-kitchen.py' to start the server."
echo "-----------------------------------------------------------------------------------"
