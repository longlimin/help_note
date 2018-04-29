# -*- coding:utf-8 -*-  
import datetime  
import sys  
from twisted.internet import protocol, reactor  
from twisted.protocols.basic import LineReceiver  
import struct

  
HOST = 'localhost'  
PORT = 8092  
  
class TSClntProtocol(protocol.Protocol):  
    def sendData(self):  
        data = raw_input('> ')  
        if data:  
            print '...sending %s...' % data  
            # self.transport.write(data)  
            # 正常数据包定义
            ver = 1
            body = json.dumps(dict(hello="world"))
            print(body)
            cmd = 101
            header = [body.__len__(), cmd]
            headPack = struct.pack("!3I", *header)
            sendData1 = headPack+body.encode()
            

        else:  
            self.transport.loseConnection()  
      
    def connectionMade(self):  
        self.sendData()  
          
    def dataReceived(self, data):  
        print data  
        self.sendData()  
  
  
class TSClntFactory(protocol.ClientFactory):  
    protocol = TSClntProtocol  
    clientConnectionLost = clientConnectionFailed = lambda self, connector, reason: reactor.stop()  
      
      
reactor.connectTCP(HOST, PORT, TSClntFactory())  
reactor.run()  