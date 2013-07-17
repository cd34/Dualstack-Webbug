#!/var/www/dualstack/bin/python

import json

import ipaddr

import tornado.ioloop
import tornado.web

url = '<a href=\\"http://www9.colo-cation.com/daviesinc,cc,cd34.html\\">Colo-cation.com</a>'

class DualStackHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "text/javascript; charset=UTF-8")
        self.write('var v4=false;')
        self.write('var v6=false;')
        self.write('c=document.getElementById("dualstack_widget");')
        html = '<div class=\\"dualstack_widget header\\">DualStack @ %s</div>' % url
        self.write('c.innerHTML="%s";' % html )
        self.write("""var ds = document.createElement('script'); ds.type = 'text/javascript'; ds.async = true; ds.src = 'http://ipv4.colo-cation.com:81/';c.parentNode.insertBefore(ds, c);""");
        self.write("""var ds = document.createElement('script'); ds.type = 'text/javascript'; ds.async = true; ds.src = 'http://ipv6.colo-cation.com/';c.parentNode.insertBefore(ds, c);""");
        self.write('new_className=" ipv%spref";' % \
            ipaddr.IPNetwork(self.request.headers['X-Real-IP'])._version)
        self.write('if ( new_className==" ipv4pref" && !v6 ) { new_className=" ipv4only";};')
        self.write('c.className+=new_className;')

class IPHandler(tornado.web.RequestHandler):
    def get(self):
        ip_version = ipaddr.IPNetwork(self.request.headers['X-Real-IP']). \
            _version
        self.set_header("Content-Type", "text/javascript; charset=UTF-8")
        self.write('c.innerHTML+="IPv%d: %s<br/>";' % \
            (ip_version, self.request.headers['X-Real-IP']))
        self.write('v%d=true;' % ip_version)

application = tornado.web.Application([])
application.add_handlers(r"dualstack\.colo-cation\.com", [
    (r"/", DualStackHandler),
])
application.add_handlers(r"ipv[46]\.colo-cation\.com", [
    (r"/", IPHandler),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
