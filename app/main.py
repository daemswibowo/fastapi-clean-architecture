from .commons.server import Server

server = Server()
app = server.app
db = server.db
container = server.container
