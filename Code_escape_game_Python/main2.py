import http.server
import socketserver

# Port sur lequel le serveur va écouter
PORT = 3000

# Spécifier le répertoire où se trouve le fichier HTML
DIRECTORY = "C:/Users/nojut/Desktop/NSI/"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Lancer le serveur
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serveur lancé sur http://localhost:{PORT}")
    print(f"Les fichiers du répertoire {DIRECTORY} sont accessibles.")
    httpd.serve_forever()
