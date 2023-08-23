# batch-convert-todoc_aws.py v1.0
# https://github.com/ldina
# Author: Lorenzo Dina - ldina - @joecondo
# Function: This script will 
# - create a list of all file names in a specified local folder
# - use tscribe library to convert the transcribed .json files from AWS trasnscribe to word .docx files


# Prerequisites:
# - tscribe library installation  ( pip install tscribe) https://pypi.org/project/tscribe/ https://github.com/kibaffo33/aws_transcribe_to_docx

# v1.0 - "Initial Release"
# If you have a huge amount of files to convert launch multiple copies of this script on different folders

import os
import tscribe

# Variables configurations
listPath = "/home/ec2-user/OutputJson"
destPath = "/home/ec2-user/OutputDoc"




# create a list of json file names in specified folder
file_names = []  # Initialize an empty list to store file names
for f in os.listdir(listPath):
    if f.endswith(".json"):
        file_names.append (f)
 #       print(file_names)

for x in file_names:
    #Convert json files from AWS Transcribe to Word .docx
    source_file_name = os.path.join(listPath, x)  # Use os.path.join to create file paths
    dest_file_name = os.path.join(destPath, os.path.splitext(x)[0] + ".docx")  # Replace the extension with ".docx"
    print("Converting:", source_file_name, "to", dest_file_name)
    try:
        tscribe.write(source_file_name, format="docx", save_as=dest_file_name)
    except Exception as e:
        print(f"Error converting {source_file_name}: {e}")