#!/usr/bin/bash

set -e
echo "========== Generating schemes for Dark version... =========="
rm -f ../Dark/scheme/*
python3 factory.py template/default.txt data/templateDark.json ../Dark/scheme/default.txt
python3 factory.py template/muxlaunch.txt data/templateDark.json ../Dark/scheme/muxlaunch.txt 
echo ""
echo "========== Generating schemes for White version... =========="
rm -f ../White/scheme/*
python3 factory.py template/default.txt data/templateWhite.json ../White/scheme/default.txt
python3 factory.py template/muxlaunch.txt data/templateWhite.json ../White/scheme/muxlaunch.txt 
echo ""
echo "========== Generating schemes for Indigo version... =========="
rm -f ../Indigo/scheme/*
python3 factory.py template/default.txt data/templateIndigo.json ../Indigo/scheme/default.txt
python3 factory.py template/muxlaunch.txt data/templateIndigo.json ../Indigo/scheme/muxlaunch.txt 
