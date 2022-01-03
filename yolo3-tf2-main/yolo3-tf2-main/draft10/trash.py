# import numpy
# import draft

# if __name__ == "__main__":
#     num=[]
#     num , l= draft.test.ADD(num,"nihao")
#     print("The str is:"+str(num))
#     print("The length is:"+ str(l))

import tornado.ioloop
import tornado.web
import tornado.httpserver
import time
 
DATA=[{'data':(95, 45)}, {'data':(80, 60)}]

 
class MainPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('calibrate.html',data_coll=DATA,time_coll=time.asctime())

        
'''
主路由
'''
app = tornado.web.Application(
        [
            (r'/',MainPageHandler)#r为取消转译,/ 为首页,MainPageHandler为首页视图，这个需要在上面自己定义
    ]
    )

if __name__ == '__main__':  #前端主入口
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(18081)
    tornado.ioloop.IOLoop.current().start()