# -*- coding: utf-8 -*-


import falcon
from .middleware import JSONTranslator
from .api import GitHubHook
from .error import IssueError

app = falcon.API(middleware=[
    JSONTranslator()
])

issuehook = GitHubHook()

app.add_route('/hook', issuehook)
app.add_error_handler(IssueError, IssueError.handle)
