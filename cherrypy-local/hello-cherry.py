import cherrypy

class HelloWorld(object):
    def index(self):
        return "Hello Pi!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())