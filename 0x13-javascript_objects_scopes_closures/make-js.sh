#!/bin/bash

# Make all .js files executable in the current directory
find . -maxdepth 1 -type f -name "*.js" -exec chmod +x {} \;
