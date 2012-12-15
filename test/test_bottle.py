#!/usr/bin/env python
#
#  XXX  Identifying information about tests here.
#
#===============
#  Tests for the Bottle web framework
#  This is based on a skeleton test file, more information at:
#
#     https://github.com/linsomniac/python-unittest-skeleton

raise NotImplementedError('To customize, remove this line and '
		'customize where it says XXX')


import sys
import unittest
import XXX_mywebapp


class Test(unittest.TestCase):
	def setUp(self):
		###  XXX code to do setup
		pass

	def tearDown(self):
		###  XXX code to do tear down
		pass

	def test_cgi_XXX_Test_Name(self):
		'''Test of web interface using CGI.'''

		def test_bottle(path, method='GET', form={}):
			from bottle import TEMPLATE_PATH
			TEMPLATE_PATH.insert(0, '../views')
			TEMPLATE_PATH.insert(0, 'views')

			app = XXX_mywebapp.XXX_setup_web_interface()

			data = '&'.join(['%s=%s' % (k, v) for k, v in form.items()])

			from bottle import run, CGIServer
			from StringIO import StringIO
			import os
			os.environ['REQUEST_METHOD'] = method
			os.environ['PATH_INFO'] = path
			os.environ['SCRIPT_NAME'] = path
			os.environ['QUERY_STRING'] = ''
			os.environ['SERVER_PROTOCOL'] = 'HTTP/1.1'
			os.environ['CONTENT_LENGTH'] = str(len(data))

			old_stdout = sys.stdout
			sys.stdout = new_stdout = StringIO()

			old_stdin = sys.stdin
			sys.stdin = new_stdin = StringIO(data)
			new_stdin.seek(0)

			run(app, server=CGIServer)

			sys.stdin = old_stdin
			sys.stdout = old_stdout

			return new_stdout.getvalue()

		raise NotImplementedError('Insert test code here.')
		#self.assertIn('Result Data', test_bottle('/'))
		#self.assertIn('href="username', test_bottle('/users'))
		#self.assertIn('Location: http://127.0.0.1/destination',
		#		test_bottle('/update/id1', method='POST',
		#			form={'name': 'Sean', 'score': '2.3'}))

	def test_wsgi_XXX_Test_Name(self):
		'''Test of web interface via WSGI interface'''

		from webtest import TestApp
		from bottle import TEMPLATE_PATH
		TEMPLATE_PATH.insert(0, '../views')
		TEMPLATE_PATH.insert(0, 'views')
		app = XXX_mywebapp.XXX_setup_web_interface()
		harness = TestApp(app)

		#results = harness.get('/')
		#self.assertEqual(results.status, '200 OK')
		#self.assertIn('href="username', results.body)

		#results = harness.get('/users/testuser1@example.org')
		#self.assertEqual(results.status, '200 OK')
		#self.assertIn('10.1.1.1', results.body)

		#results = harness.get('/rbls')
		#self.assertEqual(results.status, '200 OK')
		#self.assertIn('value="zen.spamhause.org"', results.body)
		#self.assertTrue('2.3' not in results.body)
		#self.assertTrue('sbl-xbl.spamhaus.org' not in results.body)

		#results = harness.post('/rblupdate/%s' % self.rbl_zen.id,
		#		{'address': 'zen.spamhaus.org', 'score': '2.3'})
		#self.assertEqual(results.status, '302 Found')
		#self.assertTrue(results.location.endswith('/rbls'))

		#results = harness.get('/rbls')
		#self.assertEqual(results.status, '200 OK')
		#self.assertIn('2.3', results.body)


if __name__ == '__main__':
	print unittest.main()
