"""Agente de prueba: confirma qué versión está desplegada."""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"app": "demoagent", "equipo": os.environ.get("TEAM_ID"),
                           "imagen": os.environ.get("GIT_SHA")}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("", 80), Handler).serve_forever()
