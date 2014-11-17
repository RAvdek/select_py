from base import Base

class Hive(Base):

	CMD = "ssh {data_resource} hive -f {infile} > {outfile}"

	def _set_up(self):
		""" scp query file to cluster """
		_shell_exec("scp {0} {1}:"\
			.format(self._query_file, self.data_resource))

	def _tear_down(self):
		""" delect query file in cluster """
		_shell_exec("ssh {0} rm {1}"\
			.format(self.data_resource, self._query_file))