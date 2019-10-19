"""
 * Written by Jordan Maxwell <jordan.maxwell@nxt-games.com>, June 4th, 2019
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

    # Name for logger
    LOGGER_NAME = 'aws-web-app'

    # CORS settings for XHR-calls from browsers
    CORS_ORIGIN = ['*']
    CORS_METHODS = ['POST', 'GET', 'PUT', 'DELETE', 'OPTIONS', 'HEAD']
    CORS_HEADERS = ['origin', 'accept', 'content-type']

    # If the access token given in a Authorization header should be verified
    OAUTH_ENDPOINT = None

    # Keys for signing auth
    NODE_KEY_ALLOWED = [
        # Test frontend
        "d7c86080232a7f61598cb55c5bcae63967421d33",
        # Another frontend
        "e7c86080262e7f61598cb5c5b1ae9396d421d483"
    ]

    NODE_KEY_CACHE_DIR = "../keycache/"

    # Debug Toolbar
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
    #LOG_CONFIG = dictConfig({
    #    'version': 1,
    #    'formatters': {'default': {
    #        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    #    }},
    #    'handlers': {'wsgi': {
    #        'class': 'logging.StreamHandler',
    #        'stream': 'ext://flask.logging.wsgi_errors_stream',
    #        'formatter': 'default'
    #    }},
    #    'root': {
    #        'level': 'INFO',
    #        'handlers': ['wsgi']
    #    },
    #    LOGGER_NAME: {
    #        'level': 'INFO',
    #        'handlers': ['wsgi']          
    #    }    
    #})

    # DO NOT CHANGE
    SERVICE = ServiceContainer()