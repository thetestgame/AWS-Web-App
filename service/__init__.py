"""
MIT License

Copyright (c) 2019 Jordan Maxwell
Written 10/18/2019

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from flask import Flask
from flask.cli import with_appcontext
import flask_restful as restful
from flask_restful.utils import cors
from flask_debugtoolbar import DebugToolbarExtension
from flask_bootstrap import Bootstrap
from flask_s3 import FlaskS3
from flask_cognito import CognitoAuth

def create_app(env='dev', services=dict()):
    """
    Creates a new flask app instance
    """

    # Create the flask app
    app = Flask(__name__)

    # Do everything in the app context
    with app.app_context():

        from flask import current_app, g
        g._env = env

        # Load the config
        current_app.config.from_object('service.config.config_%s.Config' % env)

        # Load all services
        for name, obj in services.items():
            app.config['SERVICE'].add(name, obj)

        # Configure the Applications API
        g._api = restful.Api(current_app)
        g._api.decorators = [
            cors.crossdomain(
                origin=current_app.config['CORS_ORIGIN'], 
                methods=current_app.config['CORS_METHODS'],
                headers=current_app.config['CORS_HEADERS'])
        ]

        # Configure S3
        s3 = FlaskS3(app)
        g._s3 = s3

        # Configure Cognito
        cognito = CognitoAuth(app)
        g._cognito = cognito

        # Load all further resources and services
        from .models import load_models
        from .resources import load_resources
        from .views import load_views

        # Resources
        load_models()
        load_resources()
        load_views()

        # Services
        from .aws import configure_aws
        configure_aws()

        # Load debug toolbar if enabled
        dev_toolbar = None
        if app.config.get('DEBUG_TOOLBAR', True):
            dev_toolbar = DebugToolbarExtension(app)
        g._dev_toolbar = dev_toolbar

        # Configure bootstrap
        Bootstrap(app)

        return app