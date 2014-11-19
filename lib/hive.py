from base import Base

class Hive(Base):
	""" Hive(query,data_resource):
		query: Hive query in string format
		data_resource: remote machine you SSH to when executing queries

	Access warning: SSH must be configured for scripting access
	"""

	CMD = "ssh {resource} hive -f {infile} > {outfile}"

	def _set_up(self):
		""" scp query file to cluster """
		self._shell_exec("scp {0} {1}:"\
			.format(self._query_file, self.data_resource))

	def _tear_down(self):
		""" delect query file in cluster """
		self._shell_exec("ssh {0} rm {1}"\
			.format(self.data_resource, self._query_file))