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

from logging.config import dictConfig

class ServiceContainer(object):
    _services = dict()

    def add(self, name, obj):
        """Add a to the service container
        Keyword arguments:
        name -- name of the service
        obj -- the service itself
        """
        self._services[name] = obj

    def get(self, name):
        """Get a service from the service container
        Keyword arguments:
        name -- name of the service
        """
        if name in self._services:
            return self._services[name]
        return None

class Config(object):
    """
    Base service configuration object
    """

    # Key used for salting or other stuff
    SECRET_KEY = 'SOME_SECRET_KEY_HERE'

    # Application
    APP_NAME = 'Flask'

    # CORS settings for XHR-calls from browsers
    CORS_ORIGIN = ['*']
    CORS_METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
    CORS_HEADERS = ['origin', 'accept', 'content-type']

    # If the access token given in a Authorization header should be verified
    OAUTH_ENDPOINT = None

    # Keys for signing auth
    NODE_KEY_ALLOWED = []
    NODE_KEY_CACHE_DIR = "../keycache/"

    # Debug Toolbar
    DEBUG_TOOLBAR = False
    DEBUG_TB_PANELS = (
        'flask_debugtoolbar.panels.versions.VersionDebugPanel',
        'flask_debugtoolbar.panels.timer.TimerDebugPanel',
        'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
        'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
        'flask_debugtoolbar.panels.template.TemplateDebugPanel',
        'flask_debugtoolbar.panels.logger.LoggingPanel'
    )
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Exception handling
    TRAP_HTTP_EXCEPTIONS = True

    # Logging 
    LOG_CONFIG = dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s][%(levelname)s][%(module)s]: %(message)s',
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default'
            },
            'watchtower': {
                'formatter': 'default',
                'class': 'watchtower.CloudWatchLogHandler',
                'log_group': APP_NAME,
                'stream_name':  'Website',
                'send_interval': 1
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi', 'watchtower']
        },
        'requests': {
            'level': 'INFO',
            'handlers': ['wsgi', 'watchtower']
        },
        'werkzeug': {
            'level': 'INFO',
            'handlers': ['wsgi', 'watchtower']            
        }   
    })

    # Cognito
    COGNITO_REGION = 'us-east-1'
    COGNITO_USERPOOL_ID = 'us-east-1c3fea2'
    COGNITO_APP_CLIENT_ID = 'abcdef123456'
    COGNITO_CHECK_TOKEN_EXPIRATION = False

    # Cloudwatch
    LOG_METRICS = False

    # Dynamodb
    DYNAMO_CREATE_TABLES = False

    # Boto3
    BOTO3_SERVICES = []

    # DO NOT CHANGE
    SERVICE = ServiceContainer()