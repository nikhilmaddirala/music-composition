#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status.

echo "Updating package lists..."
sudo add-apt-repository ppa:mscore-ubuntu/mscore-stable -y
sudo apt-get update

echo "Installing apt requirements..."
sudo xargs -a setup/apt-requirements.txt apt install -y

echo "Checking if pip is installed..."
if ! command -v pip &> /dev/null
then
    echo "pip could not be found, installing pip..."
    sudo apt-get install -y python3-pip
fi

echo "Upgrading pip..."
pip install --upgrade pip
echo "Installing pip requirements..."
pip install -r setup/requirements.txt