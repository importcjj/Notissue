# -*- coding: utf-8 -*-

import json


class JSONTranslator(object):

    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return

        body = req.stream.read()

        try:
            req.context['doc'] = json.dumps(body)
        except (ValueError, UnicodeDecodeError):
            # TODO: raise a custom error
            pass

    def process_response(self, req, resp, resource):
        if 'result' not in req.context:
            return

        resp.body = json.dumps(req.context['result'])
