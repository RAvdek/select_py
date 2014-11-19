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

	def _tear_down(self):
		""" Clean up the junk in the output """
		pass
		