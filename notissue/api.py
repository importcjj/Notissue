# -*- coding: utf-8 -*-

import falcon


class GitHubHook:

    def __init__(self):
        pass

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        req.context['result'] = '200 OK'
