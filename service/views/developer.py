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

from flask import render_template
from flask.views import MethodView

from service.decorators import view

@view.view_details(url='/_dev/helloworld', view_name='helloworld')
class HelloWorld(MethodView):
    """
    Basic view that returns "Hello World!"
    """

    def get(self):
        """
        Handles all GET requests 
        """

        return render_template('developer/hello.html')

@view.view_details(url='/_dev/error', view_name='error')
class Error(MethodView):
    """
    Simulates a page error
    """

    def get(self):
        """
        Handles all GET requests 
        """

        raise Exception('Simulated Exception')