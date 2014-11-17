import unittest
from os import system as shell
from select_py import Base

class BaseTest(unittest.TestCase):
	
	def setUp(self):
		shell("mkdir _test_dir_")
		for x in 'abcd'.split():
			shell("touch _test_dir_/{0}".format(x))

	def tearDown(self):
		shell("rm -rd _test_dir_")

	def test_shell_exec(self):
		data = Base._shell_exec("echo _test_dir/*")
		self.assertEqual(data, "a b c d")

	def test_output_summary(self):
		data = Base._output_summary("_test_dir_/a")
		self.assertEqual(data['line count'],0)

