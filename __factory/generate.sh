#!/usr/bin/bash

set -e
echo "========== Generating schemes for Dark version... =========="
python3 factory.py template/default.txt data/templateDark.json ../Dark/scheme/default.txt
python3 factory.py template/muxlaunch.txt data/templateDark.json ../Dark/scheme/muxlaunch.txt 
echo ""
echo "========== generating schemes for White version... =========="
python3 factory.py template/default.txt data/templateWhite.json ../White/scheme/default.txt
python3 factory.py template/muxlaunch.txt data/templateWhite.json ../White/scheme/muxlaunch.txt 
echo ""
echo "========== generating schemes for Indigo version... =========="
python3 factory.py template/default.txt data/templateIndigo.json ../Indigo/scheme/default.txt
python3 factory.py template/muxlaunch.txt data/templateIndigo.json ../Indigo/scheme/muxlaunch.txt 
