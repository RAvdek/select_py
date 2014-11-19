from time import time
from os import system as shell
from base import Base

class SQLServer(Base):
	""" SQLServer(query,data_resource):
		query: SQLServer query in string format
		data_resource: Server name

	Access warning: Requires Windows authentication. Designed
	to be executed via Cygwin on a Windows machine.
	"""

	CMD = "cmd /c sqlcmd -S {resource} -i {infile} -o {outfile} -s '\t' -W"

	def _set_up(self):
		""" No setup required """
		pass

	def _clean_line(self,line):
		data = line.split('\t')
		data = '\t'.join(map(lambda z: z.strip(), data))
		if data == '' or ('--' in data) or ('rows affected' in data):
			return ''
		else: 
			return data + '\n'


	def _tear_down(self):
		""" Clean up the junk in the output """
		# move data to a buffer file
		buffer_address = "__sqlserver_buffer_{0}.tsv".format("_".join(str(time()).split(".")))
		shell("cp {0} {1}".format(self.output_file, buffer_address))
		try:
			buffer_file = open(buffer_address, mode = 'r')
			target_file = open(self.output_file, mode = 'w')
			for line in buffer_file:
				target_file.write(self._clean_line(line))
			buffer_file.close()
			target_file.close()
		finally:
			shell("rm {0}".format(buffer_address))

