# `select_py`

A simple Python interface to SQL: Launch database queries (from a remote server if needed) and dump results into a tab-delimted text file on your machine.

Typical use-cases:
- You want to do some QA by hand or debugging on the results of a SQL job. You'll have to edit your SQL a bunch of times, and inspect the results which is easier to do locally.
- You want to store the results of a Hive job on your machine, so you can load it up in Excel, iPython, etc. for analysis.

**NEW:** Support for Cloudera Impala.

## Why do you care?

- There's a standard procedure for storing Hive output on your machine: `scp` a query file to a server where the SQL can be executed, `ssh` to the server, execute job so that output is saved to file, `scp` output file to local machine, `ssh` back home. Why write code to do this more than once?
- I use the same flags every time I write a script calling the [SQL Server command line utility](http://msdn.microsoft.com/en-us/library/ms162773.aspx) or the [Impala CLI](http://www.cloudera.com/content/cloudera/en/documentation/cloudera-impala/v2-0-x/topics/impala_shell_options.html).
- Handling job error and [cleaning the output](http://stackoverflow.com/questions/2362229/how-to-supress-hyphens-in-sqlcmd) of a SQL Server job executed via command line is [annoying](http://www.experts-exchange.com/Database/MS-SQL-Server/Q_28189009.html).

## How do you use it?

`select_py.Hive`, `select_py.SQLServer`, and `select_py.Impala` take the following arguments -- all strings -- upon initialization:

|Argument|Description|
|--------|-----------|
|query|Text of the query|
|server|Server from which the SQL will be executed|
|outfile|Path of the file in which output will be stored|

They each have the following methods:

|Method|Description|
|------|-----------|
<<<<<<< HEAD
|.format(\*args,\*\*kwargs)|Format the query string, using Python's `string.format()`|
|.execute()|Execute the query|
|.output_summary()|Applies [`os.stat`](https://docs.python.org/2/library/os.html#os.stat)) to the output file|

Here's a simple example:

```
$ python
>>> import datetime as dt
>>> from select_py import Hive
>>> q = """ -- show column names in output
  set hive.cli.print.header=true;
  select *
  from some_table
  where date >= \'{date}\'
  limit 10"""
>>> r = "hadoop_server"
>>> o = "my_output_file.tsv"
>>> hive_job = Hive(q,r,o)
>>> hive_job.format(date = str(dt.date.today() - dt.timedelta(days=3)))
>>> hive_job.execute()
... Hive's stderr prints to screen ...
<<<<<<< HEAD
>>> # Let's check that the output file is non-empty
>>> hive_job.output_summary().st_size
12345
>>> # Hooray!
=======
>>>>>>> 089d4ced6d60ccb5abf19ae06d4ea6954b68ba90
```

## Want to write your own API for a different SQL engine?

Given any other SQL software which has a command line interface, it should be easy to write an associated child of `select_py.Base` providing the same API. The code for the child will need a custom...
- `cls.CMD`: A shell command in a string, which will be formatted according to `self.__init__` parameters.
<<<<<<< HEAD
- `self._set_up`: Code to be executed before the SQL executes, eg. sending temporary files to a server.
- `self._tear_down`: Code to be executed after the SQL executes, eg. deleting temporary files.
=======
- `self._set_up`: Code to be executed before the SQL executes, eg. 
- `self._tear_down`: Code to be executed after the SQL executes, eg. cleaning up files.
>>>>>>> 089d4ced6d60ccb5abf19ae06d4ea6954b68ba90

## (potential) Issues

- In order for `Hive` and `Impala` to run properly, your SSH must be configured so that the server at which you normally run Hive queries can be [accessed via SSH without a password/passphrase promt](http://www.linuxproblem.org/art_9.html).
- `SQLServer` requires Windows Authenification for access to SQL Server.
- I wrote this for myself to use with Cygwin on Windows (lol), and haven't tested it out in different environments.

## to do

- `server` arg should have a `None` option
- `outfile` option should allow writing to `STDOUT` or `None`
- Add `SQLite` implementation.
- Add a factory function allowing you to choose the SQL flavor.
- Make a [docopt](http://docopt.org/)-powered CLI
<<<<<<< HEAD
- Set headers as default in `Hive`
- Rename `resource` arg as `server` in `__init__`
- Add the usual packaging with setup tools.
=======
>>>>>>> 089d4ced6d60ccb5abf19ae06d4ea6954b68ba90
