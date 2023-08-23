#
# batch-transcribe_param.py v1.0
# https://github.com/ldina
# Author: Lorenzo Dina - ldina - @joecondo
# Function: This script will 
# - create a list of all file names in the specified local folder
# - use AWS CLI to create AWS Transcrive job requests for matching files from the local list that are present in a specified source S3 bucket  
# - use AWS CLI to save the resulting trasnscribed json files in a destination S3 bucket / folder using settings 

# Prerequisites:
# - IAM configuration for user, group, policy and Access Key to access AWS S3 Buckets and Transcribe from the aws-cli
# - An S3 Source Bucket pre-configured with uploaded .wav files to be transcribed
# - An S3 Destinatin Bucket pre-configured for the .json files coming from the transcription process

# v1.0 - "Initial Release"
# v1.1 - Parameters tweaking for paths and folders
# credits to  where I got inspirations and code snippets to improve and complete my code
# TO DO: 
# -code refactor to use AWS SDK instead of AWS CLI
# -generate the file list from the S3 bucket instead of the local file system
# -implement a mechanism that can stop the process once you realize that you made some typo in the paramters


import os
from os import listdir
from os.path import isfile, join

# Variables configurations
# AWS configurations
region = "eu-west-1"
mediaFormat = "wav"
languageCode = "it-IT"
# Local path for list building of file to be processed
listPath = "/localPathForAudio"
#Source path on a S3 bucket containing the audio files to be transcribed
sourceS3BucketURI = "s3://SourceBucketName/"
#Destionation S3 bucket
destinationsS3Bucket = "destinationBucket"
#Destionation folder on the S3 bucket
destinationsFolder = "destinationFolder/"
# batch identifier for the Aws Trasncribe service to ensure trancription job names are unique
identifier = "_transcriptionIdentifier"

# create a list of all file names in specified folder
file_names = [f for f in listdir(listPath) if 
              isfile(join(listPath, f))]

for x in file_names:
    
    # AWS CLI  create job request to Transcribe and specify settings 
    command= "aws transcribe start-transcription-job --region {region} --media-format {mediaFormat} --transcription-job-name {job_name} --media MediaFileUri={sourceS3BucketURI}{file_name} --output-bucket-name {destinationsS3Bucket} --output-key {destinationsFolder} --language-code {languageCode} --settings ShowSpeakerLabels=true,MaxSpeakerLabels=2 > /dev/null".format(region=region, mediaFormat=mediaFormat, sourceS3BucketURI=sourceS3BucketURI, destinationsS3Bucket=destinationsS3Bucket, destinationsFolder=destinationsFolder, languageCode=languageCode, job_name=x+identifier, file_name=x)
    #print (command)
    os.system(command)