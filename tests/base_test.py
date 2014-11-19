import unittest
import time
from os import system as shell
from select_py import Base

""" 
In order to run this thing, we need to execute the test 'above'
the highest directory as a module:

http://stackoverflow.com/questions/1918539/can-anyone-explain-pythons-relative-imports
https://www.python.org/dev/peps/pep-0328/#rationale-for-relative-imports

$ pwd
/cygdrive/e
$ ls select_py/
__init__.py  __init__.pyc  select_py  tests
$ python -m select_py.tests.base_test
"""

class BaseTest(unittest.TestCase):
	
	def setUp(self):
		shell("mkdir _test_dir_")
		shell("echo * > _test_dir_/_test_file_")

	def tearDown(self):
		shell("rm -rd _test_dir_")

	def test_shell_exec(self):
		base = Base('a','b')
		data = base._shell_exec("echo _test_dir_/*")
		self.assertEqual(data, "_test_dir_/_test_file_")

	def test_output_summary(self):
		base = Base('a','b')
		data = base._output_summary("_test_dir_/_test_file_")
		self.assertEqual(data['line count'],1)

if __name__ == "__main__":
	unittest.main()
