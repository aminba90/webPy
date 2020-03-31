import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return '<h1>Hello, ' + name + '!</h1>'

if __name__ == "__main__":
    app.run()