#!/usr/bin/env python

import os

# Update the system
os.system("sudo apt-get update")

# Check if curl is installed
if os.system("command -v curl &> /dev/null") != 0:
    print("curl not found. Installing...")
    os.system("sudo apt-get install curl -y")
else:
    print("curl is already installed.")

# Check if wget is installed
if os.system("command -v wget &> /dev/null") != 0:
    print("wget not found. Installing...")
    os.system("sudo apt-get install wget -y")
else:
    print("wget is already installed.")

# Check if git is installed
if os.system("command -v git &> /dev/null") != 0:
    print("git not found. Installing...")
    os.system("sudo apt-get install git -y")
else:
    print("git is already installed.")

# Check if aws-cli is installed
if os.system("command -v aws &> /dev/null") != 0:
    print("aws-cli not found. Installing...")
    os.system("sudo apt-get install awscli -y")
else:
    print("aws-cli is already installed.")
