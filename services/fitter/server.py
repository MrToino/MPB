from http.server import SimpleHTTPRequestHandler, HTTPServer
from service import service

hostName = "localhost"
serverPort = 8080


class FitterHandler(SimpleHTTPRequestHandler):
    def _set_headers(self, content_length):
        self.send_header('Content-type', 'text/html')
        self.send_header("Content-Length", content_length)
        self.end_headers()
        
    def do_GET(self):
        self.send_response(200)
        self._set_headers("0")

    def do_POST(self):
        content_length = int(self.headers.get("content-length", "0"))
        length = int(content_length) if content_length else 0
        request = self.rfile.read(length)

        response = service(request)

        self.send_response(200)
        self._set_headers(str(len(response)))
        self.wfile.write(response)
    
    do_PUT = do_POST
    do_DELETE = do_GET


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), FitterHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
