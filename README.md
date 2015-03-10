select_py
=========

A simple Python interface to SQL: Run database queries *locally* and dump results into a tab-delimted text file.

Why?
----

<ul>
  <li>There's a standard procedure for storing Hive output on my machine (scp a query file to remote server, execute job piping output to text file, scp output file to local machine).</li>
  <li>I use the same flags every time I write scripts calling the <a href="http://msdn.microsoft.com/en-us/library/ms162773.aspx">the SQL Server command line utility</a>.</li>
  <li>Handling job error and <a href="http://stackoverflow.com/questions/2362229/how-to-supress-hyphens-in-sqlcmd">cleaning the output</a> of a SQL Server job executed via command line is <a href="http://www.experts-exchange.com/Database/MS-SQL-Server/Q_28189009.html">annoying</a>.</li>
</ul>

Lastly, given any other SQL software which has a command line interface, it should be easy to write an associated child of `select_py.Base` providing the same API as `select_py.Hive` and `select_py.SQLServer`.

Usage
-----

`select_py.Hive` and `select_py.SQLServer` take the following arguments -- all strings -- upon initialization:

<table>
  <tr>
    <th>Argument</th><th>Description</th>
  </tr>
  <tr>
    <td><em>query</em></td><td>Text of query to run</td>
  </tr>
  <tr>
    <td><em>data_resource</em></td><td>Name of the server handling DB access</td>
  </tr>
  <tr>
    <td><em>outfile</em></td><td>Name of the output file</td>
  </tr>
</table>

They have the following methods:

<table>
  <tr>
    <th>Method</th><th>Description</th>
  <tr>
    <td><em>.format(\*args,\*\*kwargs)</em></td><td>Format the query string, using Python's string.format()</td>
  </tr>
  <tr>
    <td><em>.execute()</em></td><td>Execute the query</td>
  </tr>
  <tr>
    <td><em>.output_summary()</em></td><td>Returns a dictionary containing meta-data of the ouptut</td>
  </tr>
<table>
select_py.Hive
==============

Use `select_py.Hive` to run a `Hive` query from a remote machine and return the results in a text file. Here's a typical use-case:

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


Warning: *In order for `select_py.Hive` to run properly, your SSH must be configured so that the remote location at which you normally run Hive queries can be <a href="http://www.linuxproblem.org/art_9.html">accessed via SSH without a password/passphrase promt</a>.*

select_py.SQLServer
===================

Warning: *Requires Windows Authenification for access to SQL Server*
