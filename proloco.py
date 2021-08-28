import os.path

import self as self
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
from Connect import Connect


define("port", default=8000, help="run on the given port", type=int)
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('master.xhtml')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('master.xhtml', pagina=Connect.body("", "index"),luogo="index", menu=Connect.menu(""), submenu=Connect.submnu(""))

class SanpieroHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('master.xhtml', pagina=Connect.body("", "sanpiero"),luogo="sanpiero", menu=Connect.menu(""), submenu=Connect.submnu(""))

class MugelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('master.xhtml', pagina=Connect.body("", "mugello"),luogo="mugello", menu=Connect.menu(""), submenu=Connect.submnu(""))

class ManifestaHandler(tornado.web.RequestHandler):
    def get(self):

        self.render('manifesta.xhtml', titolo="Manifestazioni", per='5%', go="more", pagina=Connect.body("", "sanpiero"), manifestazione="manifestazioni", news=Connect.manifesta(""),menu=Connect.menu(""), submenu=Connect.submnu("") )

class NewsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('news.xhtml', pagina=Connect.body("", "index"),luogo="index", menu=Connect.menu(""), submenu=Connect.submnu(""), news=Connect.news("") )

class News_oneHandler(tornado.web.RequestHandler):
    def get(self):
        titolo = self.get_argument('titolo')
        id = self.get_argument('id')
        self.render('news_one.xhtml', news=Connect.news_one("", titolo, id), pagina=Connect.body("", "sanpiero"), titolo=titolo, id=id )
    def post(self):
        titolo = self.get_argument('titolo')
        id = self.get_argument('id')

        self.render('news_one.xhtml', news=Connect.news_one("", titolo, id), pagina=Connect.body("", "sanpiero"), titolo=titolo, id=id )
class MenuHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('menu.xhtml',  pagina=Connect.body("", "menu"),luogo="index", menu=Connect.menu(""), submenu=Connect.submnu(""))
class MasterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('master.xhtml',  pagina=Connect.body("", "index"),luogo="index", menu=Connect.menu(""), submenu=Connect.submnu(""))
class SlideHandler(tornado.web.RequestHandler):
    def get(self):
        luogo = self.get_argument('luogo')
        self.render('nivo.xhtml',  pagina=Connect.body("", "index"),luogo="index", menu=Connect.menu(""), submenu=Connect.submnu(""), slider=Connect.slider("", luogo))

    def post(self):
        luogo = self.get_argument('luogo')
        id = self.get_argument('id')
        self.render('nivo.xhtml', pagina=Connect.body("", "index"), luogo=luogo, menu=Connect.menu(""),
                    submenu=Connect.submnu(""), slider=Connect.slider("", luogo))
class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,difference=noun3)

if __name__ == '__main__':

    tornado.options.parse_command_line()
    app = tornado.web.Application(
    handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler), (r'/menu', MenuHandler), (r'/master', MasterHandler),
              (r'/news', NewsHandler), (r'/news_one', News_oneHandler),(r'/sanpiero', SanpieroHandler),(r'/mugello',
            MugelloHandler), (r'/slide', SlideHandler),  (r'/manifestazioni', ManifestaHandler)],
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path = os.path.join(os.path.dirname(__file__), "static")
    )
    PORT = 8000
    ADDR = '0.0.0.0'

   # app.listen(PORT, ADDR)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(PORT, ADDR)
    tornado.ioloop.IOLoop.instance().start()
