# batch-download.py v1.0
# https://github.com/ldina
# Author: Lorenzo Dina - ldina - @joecondo
# Function: This script will 
# - create a list of all file names in specified local folder
# - use AWS CLI to download the transcribed .json files from the destination S3 bucket  


# Prerequisites:
# - IAM configuration for user, group, policy and Access Key to access AWS S3 Buckets and Transcribe
# - An S3 Bucket pre-configured as a destionation for the .json files coming from the transcription process

# v1.0 - "Initial Release"
# credits to  where I got inspirations and code snippets to improve and complete my code
#
# TO DO: 
# -code refactor to use AWS SDK instead of AWS CLI
# -generate the file list from S3 bucket instead of local

import os
from os import listdir
from os.path import isfile, join

# Variables configurations
listPath = "/localPathForAudioFiles"
destionationsS3Bucket = "bucketName"


# create a list of all file names in the specified folder
file_names = [f for f in listdir(listPath) if 
              isfile(join(listPath, f))]

# batch identifier to select transcription jobs to download
identifier="_trial_2"

for x in file_names:
    
    # AWS CLI request to download objects from specified S3 bucket
    command = "aws s3api get-object --bucket {destionationsS3Bucket} --key {job_name}.json > /dev/null".format(job_name=x+identifier, file_name=x, destionationsS3Bucket=destionationsS3Bucket)

    os.system(command)
