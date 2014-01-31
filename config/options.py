import tornado.options
import torndb
from tornado.options import define,options

define('port', default = 8888, help = 'port', type = int)
db = torndb.Connection(host='localhost', database='todo', user='root', password='aaaaaa')
