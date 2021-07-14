#!/bin/bash

if python3 --version &> /dev/null; then
    python3 installer
else
    echo "No python3 installation was found!"
fi