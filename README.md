<img src=".github/aws-logo.jpg" align="right" width="200">

AWS Web Application Template
============================
This repository contains a basic template for developing a flask based website on AWS. It is cappable of deploying as serverless or as a dedicated host on EC2.

## Dependencies
Not all dependencies are required to operate. This list is to use every feature available in the template.
* Python 3
* zappa
* tornado
* arrow
* watchtower
* flask
* Flask-Script
* flask-restful
* flask-debugtoolbar
* flask-bootstrap
* flask-s3
* flask_cognito
* flask-boto3
* flask_pynamodb_resource
* cloudwatch-fluent-metrics

## Setup
To setup a new environment to work from run the the respective ``create-env`` script for your operating system. This will create a Python virtual environment for the other scripts to use. To run a development server run the ``dev-server`` script. This will create a hot reloading flask environment that will reload once a change is made.

## Deployment
The template supports three different production forms of deployment. WSGI, Tornado, and Serverless. The documation for each can be found below.

### WSGI
TODO

### Tornado
TODO

### Serverless
TODO

## License
The AWS Web Application Template is licensed under the MIT license.