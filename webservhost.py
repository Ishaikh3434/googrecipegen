from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import subprocess

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            file = open("output.txt", "r")
            text_content = "".join(file.readlines())  # The content to dynamically update
            file.close()
        except:
            text_content = "<h1>Initialising...</h1>"

        if self.path == "/content":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"content": text_content}
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        elif self.path == "/run-script":
            # Run the external Python script
            subprocess.Popen(['python', 'main.py'])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Listening...')
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(
                "<html>"
                "<head>"
                "<style>"
                "body { font-family: Arial, sans-serif; background-color: #f0f0f5; margin: 0; padding: 20px; }"
                "#dynamic-html { background: #ffffff; border-radius: 10px; padding: 20px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }"
                "button { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; }"
                "button:hover { background-color: #45a049; }"
                "</style>"
                "<script>"
                "async function fetchContent() {"
                "const response = await fetch('/content');"
                "const data = await response.json();"
                "document.getElementById('dynamic-html').innerHTML = data.content;"
                "}"
                "setInterval(fetchContent, 5000);"
                "</script>"
                "</head>"
                "<body>"
                
                "<div id='dynamic-html'>Loading...</div>"
                "<button onclick=\"fetch('/run-script').then(response => response.text()).then(alert);\">Run Script</button>"
                "</body>"
                "</html>",
                "utf-8"
            ))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Server started at http://localhost:8000")
    server.serve_forever()