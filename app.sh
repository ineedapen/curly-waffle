#!/bin/bash

#Get the file
host="Drive_URL"
gdown $Drive_URL -O "/root/flag/encrypted/"
# Set the file paths
file_path="/root/flag/encrypted/flag.txt.gpg"
password_file="/Path/to/your/password/file"

password=$(sed -n 1p $password_file)

# Decrypt the file with the password
echo $password | gpg --batch --yes --passphrase-fd 0 $file_path
