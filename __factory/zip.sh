#!/usr/bin/bash

set -e
mkdir -p ../__build
rm -rf ../__build/*
echo "========== Compressing Dark version... =========="
cd ../Dark/ && zip -r ../__build/RezolutionDark.zip .
echo ""
echo "========== Compressing for White version... =========="
cd ../White/ && zip -r ../__build/RezolutionWhite.zip .
echo ""
echo "========== Compressing for Indigo version... =========="
cd ../Indigo/ && zip -r ../__build/RezolutionIndigo.zip .
