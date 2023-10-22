import logging
from logging.handlers import SocketHandler
from pythonjsonlogger import jsonlogger


format = '%(asctime)s [%(levelname)s] %(funcName)s %(process)d %(message)s'
logger = logging.getLogger("module_name")


formatter = jsonlogger.JsonFormatter(format)



class FluentBitHandler(SocketHandler):
    def emit(self, record):
        try:
            self.send((self.format(record)).encode())
        except Exception:
            self.handleError(record)




socket_handler = FluentBitHandler("localhost", 3130)
socket_handler.setFormatter(formatter)
logger.addHandler(socket_handler)



logger.error("Hello Log!")
