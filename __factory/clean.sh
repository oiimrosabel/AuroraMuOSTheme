#!/usr/bin/bash

set -e
echo "========== Cleaning __build folder... =========="
rm -rf ../__build
echo "Done."
echo ""
echo "========== Cleaning sheme files... =========="
rm -f ../Dark/scheme/*
rm -f ../White/scheme/*
rm -f ../Indigo/scheme/*
echo "Done."
