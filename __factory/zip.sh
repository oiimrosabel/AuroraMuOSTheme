#!/usr/bin/bash

set -e
mkdir -p ../__build
rm -rf ../__build/*
echo "========== Compressing Rezolution Dark variant... =========="
cd ../Dark/ && zip -r ../__build/RezolutionDark.zip .
echo ""
echo "========== Compressing Rezolution White variant... =========="
cd ../White/ && zip -r ../__build/RezolutionWhite.zip .
echo ""
echo "========== Compressing Rezolution Indigo variant... =========="
cd ../Indigo/ && zip -r ../__build/RezolutionIndigo.zip .
echo ""
echo "========== Compressing Rezolution system icons... =========="
cd ../__icons/ && zip -r ../__build/SystemIcons.zip . # -x "CREDITS.md"
