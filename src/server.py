import json
from typing import Dict, Optional
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
from app import API
from models import Response


class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, code: int, message: Dict) -> None:
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode())

    def do_GET(self) -> None:
        query_params = parse_qs(self.path.split('?')[1]) if '?' in self.path else {}
        path = self.path.split('?')[0]
        response = self.server.api.handle_request(path, 'GET', query_params)
        self._send_response(response.status, response.to_dict())

    def do_POST(self) -> None:
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            data = {}
        path = self.path
        response = self.server.api.handle_request(path, 'POST', data)
        self._send_response(response.status, response.to_dict())


class MyHTTPServer(HTTPServer):
    def __init__(self, server_address: tuple[str, int], RequestHandlerClass: RequestHandler, api: API) -> None:
        super().__init__(server_address, RequestHandlerClass)
        self.api = api


def run_server() -> None:
    app = API()

    @app.route('/hello', methods=['GET'])
    def hello_world(query_params: Optional[dict]) -> Response:
        if query_params is None:
            query_params = {}
        name = query_params.get('name', ['World'])[0]
        return Response(status=200, message=f"Hello, {name}!")

    @app.route('/data', methods=['POST'])
    def receive_data(query_params: Optional[dict]) -> Response:
        return Response(status=200, message="Data received", data=query_params)

    server = MyHTTPServer(('localhost', 8000), RequestHandler, app)
    print("Server running at http://localhost:8000")
    server.serve_forever()

run_server()