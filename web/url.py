import web

urls = ('/static/?', 'static',
        '/static/post/?','post')
app = web.application(urls, globals())

class static:
    def GET(self):
        return 'static'
    class post:
         def GET(self):
            return 'post'
if __name__ == '__main__':
    app.run()


