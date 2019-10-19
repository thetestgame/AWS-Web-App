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

class ResourceBookException(Exception):
    """
    Custom exception for the resource book system
    """

class ResourceBook(object):
    """
    Contains all registered resources
    """

    def __init__(self):
        self._resources = {}

    @property
    def resources(self):
        return self._resources

    def add_resource(self, resource_details):
        """
        Registers a new resource with the resource book
        """

        url = resource_details.url
        if url in self._resources:
            raise ResourceBookException('url %s is already assigned!' % url)

        self._resources[url] = resource_details

resource_book = ResourceBook()
        
class ResourceDetailsDecorator(object):
    """
    Custom decorator for registering resources with the ResourceBook
    """

    def __init__(self, url='/', **kwargs):
        self._url = url
        self._kwargs = kwargs
        self._resource_cls = None

    @property
    def url(self):
        return self._url

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def resource_cls(self):
        return self._resource_cls

    def __call__(self, resource_cls):
        self._resource_cls = resource_cls
        resource_book.add_resource(self)

resource_details = ResourceDetailsDecorator