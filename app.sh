#!/bin/bash

#Get the file
gdown https://drive.google.com/uc?id=1YCKctjZ64XUaKS9VFYdfG-BqSWxU1Ubu -O "/root/flag/encrypted/"
# Set the file paths
file_path="/root/flag/encrypted/flag.txt.gpg"
password_file=".password"

password=$(sed -n 1p $password_file)

# Decrypt the file with the password
echo $password | gpg --batch --yes --passphrase-fd 0 $file_path
