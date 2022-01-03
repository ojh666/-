# import numpy

# class test():
#     def ADD(obj,str):
#         obj.append("nihao")
#         L = len(obj)
#         return obj , L
import tornado.ioloop
import tornado.web
import tornado.httpserver
import time
import test_tornado

obj=['APPLE']
DATA=[{'data':(95, 45)}, {'data':(80, 60)}]
file_name = 'calibrate.html'

test = test_tornado.MainPageHandler()
# test_tornado.MainPageHandler.get(tornado.web.RequestHandler,obj,file_name)
test.get(tornado.web.RequestHandler,obj,file_name)
# test_tornado.main_tor()
test.main_tor()

# test_tornado.MainPageHandler.get(tornado.web.RequestHandler)
# test_tornado.MainPageHandler.wri(tornado.web.RequestHandler,obj)
# test_tornado.main_tor()