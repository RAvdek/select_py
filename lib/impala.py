from base import Base

class Impala(Base):
    """ Impala(query, data_resource, output_file) """

    CMD = "ssh {resource} impala-shell -f {infile} -B --print_header -o {outfile}"

    def _set_up(self):
        """ scp query file to cluster """
        self._shel_exec("scp {0} {1}:"\
            .format(self._query_file, self.data_resource))

    def _tear_down(self):
        """ delete query from file in cluster """
        self._shell_exec("ssh {0} rm {1}"\
            .format(self.data_resource, self._query_file))