#!/usr/bin/env python
#
#  XXX  Identifying information about tests here.
#
#===============
#  This is based on a skeleton test file, more information at:
#
#     https://github.com/linsomniac/python-unittest-skeleton

raise NotImplementedError(
        'To customize, remove this line and customize where it says XXX')

import unittest

import sys
sys.path.append('..')      # XXX Probably needed to import your code


class test_XXX_Test_Group_Name(unittest.TestCase):
    def test_XXX_Simulate_TCP_Failures(self):
        from faketcpserver import RECEIVE, CommandServer
        import memcached2

        immediately_disconnect_server = CommandServer([])
        sc = memcached2.ServerConnection(
                'memcached://127.0.0.1:{0}/'
                .format(immediately_disconnect_server.port))
        sc.set('foo', 'bar')

        receive_then_disconnect_server = CommandServer([RECEIVE])
        sc = memcached2.ServerConnection(
                'memcached://127.0.0.1:{0}/'
                .format(receive_then_disconnect_server.port))
        sc.set('foo', 'bar')

        disconnect_after_second_read_server = CommandServer(
            [RECEIVE, 'STORED\r\n', RECEIVE])
        sc = memcached2.ServerConnection(
                'memcached://127.0.0.1:{0}/'
                .format(disconnect_after_second_read_server.port))
        sc.set('foo', 'bar')

unittest.main()
