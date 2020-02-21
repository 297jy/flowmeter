# coding=utf-8

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from flowmeter.modbus.api import frame

clients = []


class ModBus(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            "欢迎来到Spread Site, 你是第%s个客户端用户!\n" % self.factory.numProtocols
        )
        print("new connect: %d" % self.factory.numProtocols)
        clients.append(self)

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1
        clients.remove(self)
        print("lost connect: %d" % self.factory.numProtocols)

    def dataReceived(self, data):
        if data == "close":
            self.transport.loseConnection()
            for client in clients:
                if client != self:
                    client.transport.write(data)
        else:
            pass


class ModBusFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return ModBus(self)

