from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-Type", "text/plain")
		self.end_headers()
		self.wfile.write(bytes(f"MyApp", "utf-8"))

if __name__ == "__main__":
	host = "0.0.0.0"
	port = 8080
	server = HTTPServer((host, port), Handler)
	print(f"Server listening on {host}:{port}")

	try:
		server.serve_forever()
	except KeyboardInterrupt:
		pass

	server.server_close()
