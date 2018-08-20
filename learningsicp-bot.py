from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import request, parse
import json

groups = ["Learning-SICP", "Learning-SICP（2群）"]

class MojoPostHandler(BaseHTTPRequestHandler):

    def _send_text(self, gname, text):
        url = "http://127.0.0.1:9292/openqq/send_group_message"

        data = {"name": gname, "content": text, "async": 1}
        req =  request.Request(url, data=parse.urlencode(data).encode())
        resp = request.urlopen(req)

    def _handle_group_message(self, content):
        forward_text = "{}:\n{}".format(content["sender"], content["content"])

        for g in groups:
            if (g != content["group"]):
                self._send_text(g, forward_text)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content = json.loads(self.rfile.read(content_length).decode("utf-8"))

        print(content)

        if content["post_type"] == "receive_message":
            print("Received message:", content["type"])

            if content["type"] == "group_message":
                self._handle_group_message(content)

        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

def main():
    ip = "127.0.0.1"
    port = 2929
    print("Serving on {}:{} ...".format(ip, port))
    server = HTTPServer(("127.0.0.1", 2929), MojoPostHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()