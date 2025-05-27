from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import re

# Lista em memória para armazenar os livros
books = [
    { "id": 1, "title": "1984", "author": "George Orwell" },
    { "id": 2, "title": "Brave New World", "author": "Aldous Huxley" }
]
next_id = 3

class BookAPIHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, data=None, content_type="application/json"):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()
        if data:
            self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        global books
        # Rota /books
        if self.path == "/books":
            self._send_response(200, books)
        # Rota /books/<id>
        elif re.match(r"^/books/(\d+)$", self.path):
            book_id = int(re.match(r"^/books/(\d+)$", self.path).group(1))
            book = next((b for b in books if b["id"] == book_id), None)
            if book:
                self._send_response(200, book)
            else:
                self._send_response(404, {"error": "Book not found"})
        else:
            self._send_response(404, {"error": "Not Found"})

    def do_POST(self):
        global books, next_id
        if self.path == "/books":
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            try:
                new_book_data = json.loads(post_data.decode("utf-8"))
                if "title" not in new_book_data or "author" not in new_book_data:
                    self._send_response(400, {"error": "Missing title or author"})
                    return

                new_book = {
                    "id": next_id,
                    "title": new_book_data["title"],
                    "author": new_book_data["author"],
                }
                books.append(new_book)
                next_id += 1
                self._send_response(201, new_book)
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Invalid JSON"})
            except Exception as e:
                 self._send_response(500, {"error": f"Internal server error: {str(e)}"}) # Adicionado para depuração
        else:
            self._send_response(404, {"error": "Not Found"})

def run(server_class=HTTPServer, handler_class=BookAPIHandler, port=8000):
    server_address = ("", port) # Escuta em todas as interfaces
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

