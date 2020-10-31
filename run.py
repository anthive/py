#!/usr/bin/env python

import json
import random

try:  # For python 3
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:  # For python 2
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

ACTIONS = ["stay", "move", "eat", "take", "put"]
DIRECTIONS = ["up", "down", "right", "left"]


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        payload = self.rfile.read(int(self.headers['Content-Length']))

        # Hive object from request payload
        hive = json.loads(payload)

        # Loop through ants and give orders
        orders = []
        for ant in hive['ants']:
            order = {
                "antId": ant['id'],
                "act": ACTIONS[random.randint(0, 4)],
                "dir": DIRECTIONS[random.randint(0, 3)]
            }
            orders.append(order)

        response = json.dumps({"orders":orders})
        # json format sample:
        # {"orders": [
        #  {"antId":1,"act":"move","dir":"down"},
        #  {"antId":17,"act":"load","dir":"up"}
        # ]}

        try:  # For python 3
            out = bytes(response, "utf8")
        except TypeError:  # For python 2
            out = bytes(response)

        self.wfile.write(out)
        return


def run():
    server_address = ('0.0.0.0', 7070)
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()


run()
