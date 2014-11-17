""" Parent class for queries """
from time import time
from subprocess import Popen, PIPE
from os import system as _shell

class Base(object):
	""" Constructor takes the following arguments:
		query: string containing query to be executed
		data_resource: place to access data. For SQL Server,
			this will be a data base.  For Hive, it will be
			an ssh alias.
		output_file: destination of query output on local machine
	"""

	CMD = '{infile} {resource} {outfile}'

	def _query_file_name():
		""" Provides a unique addres for a temporary file """
		return "__QUERY__{0}.sql".format('_'.join(str(time()).split('.')))

	def _set_up(self):
		""" Set up the environment for querying"""
		pass

	def _tear_down(self):
		""" Tear down environment for querying """
		pass

	def _shell_exec(cmd):
		""" Executes a shell command, cmd. Return output """
				# execute cmd using subprocess
		shell_job = Popen(cmd, shell=True)
		# wait for execution completion and check status
		if shell_job.wait() != 0:
			stdout_msg, stderr_msg = shell_job.communicate()
			raise Exception("""Command failed with status {0}
				Command: {1}
				Stdout:\n{2}"""\
				.format(shell_job.returncode,cmd, error_msg))
		return stdout_msg

	def _output_summary(file_path):
		""" Inspects a file """
		output = dict()
		# Check some conditions with stat and wc ...
		output['line count'] = int(_shell_exec("wc -l {0}".format(file_path)))
		return output

	def __init__(self, query, data_resource):
		self.query = query
		self.data_resource = data_resource
		self._query_file = _query_file_name()

	def format(self, **kwargs):
		""" Formats the input string """
		self.query = self.query.format(**kwargs)

	def output_summary(self):
		""" Returns a dictionary with attributes of the query results """
		return _output_summary(self.output_file)

	def execute(self, output_file):
		""" Executes sends the query to data resource and executes.
		Output is stored to output_file"""
		self.output_file = output_file
		# set up querying environment
		self._set_up()
		# Put contents of query in temporary file
		temp_query_file = open(self._query_file,'w')
		temp_query_file.write(self.query)
		temp_query_file.close()
		# format command with input and output file paths
		cmd = _CMD.format(infile = self.query_file, \
			resource = self.data_resource, outfile = output_file)
		# execute cmd via shell
		self._shell_exec(cmd)
		# clean up environment
		_shell_exec("rm {0}".format(self._query_file))
		self._tear_down()