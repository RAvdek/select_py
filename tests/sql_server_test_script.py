from os import system as shell
from select_py import SQLServer

q = "select top 10 userid, birthday from zooskods..odsusers"
r = "biods3"
o = "_sql_server_temp_file_.tsv"

job = SQLServer(q,r,o)
job.execute()

data = open(o)
for line in data:
	print line

shell("rm {0}".format(o))
