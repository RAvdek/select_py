from time import time
from os import system as shell
<<<<<<< HEAD
import os
=======
>>>>>>> eab978c74baf0b0df48faa1b6514af4029cf3b57
from base import Base

class SQLServer(Base):
	""" SQLServer(query,data_resource):
		query: SQLServer query in string format
		data_resource: Server name

	Access warning: Requires Windows authentication. Designed
	to be executed via Cygwin on a Windows machine.
	"""

<<<<<<< HEAD
	CMD = "cmd /c sqlcmd -S {resource} -i {infile} -s '\t' -W -o {outfile}"
=======
	CMD = "cmd /c sqlcmd -S {resource} -i {infile} -o {outfile} -s '\t' -W"
>>>>>>> eab978c74baf0b0df48faa1b6514af4029cf3b57

	def _set_up(self):
		""" No setup required """
		pass

	def _clean_line(self,line):
		data = line.split('\t')
		data = '\t'.join(map(lambda z: z.strip(), data))
		if data == '' or ('--' in data) or ('rows affected' in data):
			return ''
<<<<<<< HEAD
		elif "Changed database context to" in line:
			return ''
		else: 
			return data + '\n'

=======
		else: 
			return data + '\n'


>>>>>>> eab978c74baf0b0df48faa1b6514af4029cf3b57
	def _tear_down(self):
		""" Clean up the junk in the output """
		# move data to a buffer file
		buffer_address = "__sqlserver_buffer_{0}.tsv".format("_".join(str(time()).split(".")))
<<<<<<< HEAD
		os.rename(self.output_file, buffer_address)
		job_failed = False
		try:
			buffer_file = open(buffer_address, mode = 'r')
			target_file = open(self.output_file, mode = 'w')
			# Hacky workaround to catch bugs in SQL
			for line in buffer_file:
				if ("Msg " in line) & ("Level " in line) & ("State " in line):
					job_failed = True
					error_msg = line
					raise Exception("SQL script contains the following error:\n{0}"\
					.format(error_msg))
				else: 
					target_file.write(self._clean_line(line))
		finally:
			buffer_file.close()
			target_file.close()
			os.remove(buffer_address)
			if job_failed == True:
				os.remove(self.target_file)
=======
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
>>>>>>> eab978c74baf0b0df48faa1b6514af4029cf3b57

