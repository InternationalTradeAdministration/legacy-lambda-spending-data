# NTTO Spending Data Lambda

This project provides an AWS Lambda that creates a single CSV document from NTTO spending data Excel documents.
It uploads that CSV file to an S3 bucket and calls the freshening Lambda for its search endpoint.

## Prerequisites

Follow instructions from [python-lambda](https://github.com/nficano/python-lambda) to ensure your basic development environment is ready,
including:

* Python
* Pip
* Virtualenv
* Virtualenvwrapper
* AWS credentials

## Getting Started

  git clone git@github.com:GovWizely/lambda-spending-data.git
  cd lambda-spending-data
  mkvirtualenv -r requirements.txt lambda-spending-data

## Configuration

* Define AWS credentials in either `config.yaml` or in the [default] section of ~/.aws/credentials.
* Edit `config.yaml` if you want to specify a different AWS region, role, and so on.
* Make sure you do not commit the AWS credentials to version control

## Invocation

  lambda invoke -v
 
## Deploy

  lambda deploy
