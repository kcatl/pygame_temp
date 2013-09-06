import web

urls = ( '/','index')

class index:
    def GET(self):
        return '<em>hello</em> world'

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

