# -*- coding: utf-8 -*-
import json


class IssueError(Exception):

    def __init__(self, code=500, message=u'Something Error :('):
        self.code = code
        self.message = message

    @staticmethod
    def handle(self, req, resp):
        result = dict(code=self.code, message=self.message)
        resp.body = json.loads(result)
