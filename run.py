#!/usr/bin/env python

import json
import random

try:  # For python 3
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:  # For python 2
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# available actions and directions
ACTIONS = ["stay", "move", "eat", "take", "put"]
DIRECTIONS = ["up", "down", "right", "left"]

class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        # your bot respons should be json object
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # sim will make http post request to your bot
    def do_POST(self):
        self._set_headers()
        payload = self.rfile.read(int(self.headers['Content-Length']))

        # hive object from request payload
        hive = json.loads(payload)

        # loop through ants and give orders
        orders = []
        for ant in hive["ants"]:
            order = {
                "antId": ant["id"],
                "act": "move",
                "dir": DIRECTIONS[random.randint(0, 3)] # pick random direction from array on line 13
            }
            # add order to your response object from line 20
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
    # starting listen for http calls on port :7070
    server_address = ('0.0.0.0', 7070) 
    httpd = HTTPServer(server_address, Handler)
    httpd.serve_forever()

run()

# this code available at https://github.com/anthive/python
# to test it localy, submit post request with payload.json using postman or curl
# curl -X 'POST' -d @payload.json http://localhost:7070

# have fun!

