#!/usr/bin/env python
#
#  python-unittest-skeleton helper which allows for creating TCP
#  servers that misbehave in certain ways, for testing code.
#
#===============
#  This is based on a skeleton test file, more information at:
#
#     https://github.com/linsomniac/python-unittest-skeleton

import sys

PY3 = sys.version > '3'

class FakeTCPServer:
    '''A simple socket server so that specific error conditions can be tested.
    This must be subclassed and implment the "server()" method.

    The server() method would be implemented to do :py:func:`socket.send` and
    :py:func:`socket.recv` calls to communicate with the client process.
    '''

    def __init__(self):
        import socket
        import os
        import signal

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.listen(1)
        self.port = self.s.getsockname()[1]
        self.pid = os.fork()

        if self.pid != 0:
            self.s.close()
            del self.s
        else:
            def alarm(signum, frame):
                os._exit(0)

            count = 0
            signal.signal(signal.SIGALRM, alarm)
            signal.alarm(5)
            while True:
                connection, addr = self.s.accept()
                self.server(self.s, connection, count)
                count += 1


RECEIVE = None          #  Instruct the server to read data


class CommandServer(FakeTCPServer):
    '''A convenience class that allows you to specify a set of TCP
    interactions that will be performed, providing a generic "server()"
    method for FakeTCPServer().

    For example, if you want to test what happens when your code sends some
    data, receives a "STORED" response, sends some more data and then the
    connection is closed:

    >>> fake_server = CommandServer(
    >>>     [RECEIVE, 'STORED\r\n', RECEIVE])
    >>> sc = memcached2.ServerConnection('memcached://127.0.0.1:{0}/'
    >>>         .format(fake_server.port))
    '''

    def __init__(self, commands):
        self.commands = commands
        FakeTCPServer.__init__(self)

    def server(self, sock, conn, count):
        for command in self.commands:
            if command == RECEIVE:
                conn.recv(1000)
            else:
                if PY3:
                    conn.send(bytes(command, 'ascii'))
                else:
                    conn.send(bytes(command))
        conn.close()
