from http.server import BaseHTTPRequestHandler, HTTPServer
from routes.main import routes
from config import Config as env

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        self.responde()

    def handle_http(self):

        status = 200
        content_type = "text/html"
        response_content = ""

        if self.path in routes:
            route_content = routes[self.path]['shell-scripts']
            filepath = "{0}/{1}/{2}".format(env.STATIC_PREFIX_PATH, env.SHELL_PREFIX_PATH, route_content)

            try:
                file = open(filepath)
            except IOError as e:
                self.send_error(404, "File Non Found: {0}".format(self.path))
                response_content = 'File Not Found'
                return response_content.encode()
            else:
                with open(filepath, 'r') as file:
                    content_type = "text/html"
                    response_content = file.read()

        else:
            self.send_error(404, "File Non Found: {0}".format(self.path))
            response_content = 'File Not Found'
            return response_content.encode()

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

        return response_content.encode()

    def responde(self):
        content = self.handle_http()
        self.wfile.write(content)

if __name__ == "__main__":

    try:
        server = HTTPServer(("0.0.0.0", 5000), HttpProcessor)
        print("=====> started http server...")
        server.serve_forever()
    except KeyboardInterrupt:
        print("shutting down server...")
        server.socket.close()
        print('=====> closed http server!')
