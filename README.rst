.. footer::

   ###Page### of ###Total###


scripts — Scripting Utilities
=============================

A light-weight package with few dependencies that allows users to do 
shell-script like things relatively easily in Python.

It consists of replacements for some very common Unix utilities that interact 
with the filesystem, such as cp, mv, rm, ln, and mkdir. These tend to be less 
fussy than their command line counter parts. For example, rm deletes both files 
and directories without distinction and will not complain if the file or 
directory does not exist. Similarly mkdir will create any child directories 
needed and will not complain if the directory already exists.

Finally, it provides several ways to run external programs.

Each feature is designed to allow you to express your desires simply and 
efficiently without worrying too much about exceptions.

System Utility Functions
------------------------

Copy (cp)
~~~~~~~~~

Copy files or directories::

    cp(src, ..., dest)

Copy all source items, whether they be files or directories to dest. If there is 
more than one src item, then dest must be a directory and the copies will be 
placed in that directory.  The src arguments may be strings or lists of strings.  
The dest must be a string.

Example:

.. code-block:: python

   >>> from scripts import *
   >>> testdir = 'testdir'
   >>> rm(testdir)
   >>> mkdir(testdir)
   >>> files = all_paths(testdir, ['f1', 'f2'])
   >>> touch(files)
   >>> dirs = all_paths(testdir, ['d1', 'd2'])
   >>> mkdir(dirs)
   >>> print(sorted(ls(path=testdir)))
   ['testdir/d1', 'testdir/d2', 'testdir/f1', 'testdir/f2']

   >>> cp('testdir/f1', 'testdir/f4')
   >>> print(sorted(lsf(path=testdir)))
   ['testdir/f1', 'testdir/f2', 'testdir/f4']

   >>> dest1 = join(testdir, 'dest1')
   >>> mkdir(dest1)
   >>> cp(files, dest1)
   >>> print(sorted(lsf(path=dest1)))
   ['testdir/dest1/f1', 'testdir/dest1/f2']

   >>> cp(dirs, dest1)
   >>> print(sorted(lsd(path=dest1)))
   ['testdir/dest1/d1', 'testdir/dest1/d2']

   >>> f1, f2 = tuple(files)
   >>> dest2 = join(testdir, 'dest2')
   >>> mkdir(dest2)
   >>> cp(f1, f2, dest2)
   >>> print(sorted(lsf(path=dest2)))
   ['testdir/dest2/f1', 'testdir/dest2/f2']

   >>> dest3 = join(testdir, 'dest3')
   >>> mkdir(dest3)
   >>> cp([f1, f2], dest3)
   >>> print(sorted(lsf(path=dest3)))
   ['testdir/dest3/f1', 'testdir/dest3/f2']


Move (mv)
~~~~~~~~~

Move files or directories::

    mv(src, ..., dest)

Move all source items, whether they be files or directories to dest. If there is 
more than one src item, then dest must be a directory and everything will be 
placed in that directory.  The src arguments may be strings or lists of strings.  
The dest must be a string.

.. code-block:: python

   >>> from scripts import *
   >>> testdir = 'testdir'
   >>> rm(testdir)
   >>> mkdir(testdir)
   >>> files = all_paths(testdir, ['f1', 'f2'])
   >>> touch(files)
   >>> dirs = all_paths(testdir, ['d1', 'd2'])
   >>> mkdir(dirs)
   >>> print(sorted(ls(path=testdir)))
   ['testdir/d1', 'testdir/d2', 'testdir/f1', 'testdir/f2']

   >>> dest = join(testdir, 'dest')
   >>> mkdir(dest)
   >>> mv(files, dest)                  # move a list of files
   >>> print(sorted(lsf(path=dest)))
   ['testdir/dest/f1', 'testdir/dest/f2']

   >>> mv(dirs, dest)                   # move a list of directories
   >>> print(sorted(lsd(path=dest)))
   ['testdir/dest/d1', 'testdir/dest/d2']


Remove (rm)
~~~~~~~~~~~

Remove files or directories::

    rm(path, ...)

Delete all files and directories given as arguments. Does not complain if any of 
the items do not exist.  Each argument must be either a string or a list of 
strings.

.. code-block:: python

   >>> print(sorted(ls(path=testdir)))
   ['testdir/dest']

   >>> print(sorted(ls(path=dest)))
   ['testdir/dest/d1', 'testdir/dest/d2', 'testdir/dest/f1', 'testdir/dest/f2']

   >>> rm(lsf(path=dest))
   >>> print(sorted(ls(path=dest)))
   ['testdir/dest/d1', 'testdir/dest/d2']

   >>> rm(dest)
   >>> print(sorted(ls(path=testdir)))
   []
   
   >>> rm(testdir)

Link (ln)
~~~~~~~~~~~

Create a symbolic link::

   ln(src, link)

Creates a symbolic link *link* that points to *src*.  Each argument must be 
either a string.


Make File (touch)
~~~~~~~~~~~~~~~~~

Create a new empty file or update the timestamp on an existing file::

   touch(path, ...)

Each argument must be either a string or a list of strings.


Make Directory (mkdir)
~~~~~~~~~~~~~~~~~~~~~~

Create an empty directory::

   mkdir(path, ...)

For each argument it creates a directory and any needed parent directories.  
Returns without complaint if the directory already exists. Each argument must be 
either a string or a list of strings.


List Directory (ls, lsd, lsf)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List a directory::

   ls(glb, path)
   lsd(glb, path)
   lsf(glb, path)

The first form returns a list of all items found in a directory. The second 
returns only the directories, and the third returns only the files. The glob 
pattern (glb) can be used to restrict the items shown. If path is not given, the 
current working directory is assumed.

Examples::

   pyfiles = lsf('*.py')
   subdirs = lsd()
   tmp_mutt = lsf('mutt-*', '/tmp')

Join Path Components (join)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Combine path components to create a path::

   join(comp, ...)

Combine components into a path. If a subsequent component is an
absolute path, previous components are discarded.

Can also be used to expand the user (~) or environment variables in path.  
Whether this is done by default is controlled by script_prefs.

.. code-block:: python

   >>> from scripts import *

   >>> python = join('bin', '/usr/bin', 'python')
   >>> python
   '/usr/bin/python'

   >>> home1 = join('~', expanduser=True)
   >>> home2 = join('$HOME', expandvars=True)
   >>> home1 == home2
   True

Path Utilities
~~~~~~~~~~~~~~

===================== ===== =====================================================
name and args         ret   description
===================== ===== =====================================================
exists(path)          bool  returns true if path exists
missing(path)         bool  returns true if path does not exist
isfile(path)          bool  returns true if path exists and is a file
isdir(path)           bool  returns true if path exists and is a directory
islink(path)          bool  returns true if path exists and is a link
isreadable(path)      bool  returns true if path exists and is readable
iswritable(path)      bool  returns true if path exists and is writable
isexecutable(path)    bool  returns true if path exists and is executable
abspath(path)         str   converts path to an absolute path
relpath(path)         str   converts path to a relative path from cwd
pathfrom(path, start) str   converts path to a relative path from start
normpath(pth)         str   returns a cleaned up version of the path
head(path)            str   returns path with last component removed
tail(path)            str   returns last component of path
cleave(path)          tuple returns (head, tail) (alt split)
split(path)           tuple returns each component of path split into tuple
stem(path)            str   returns path with extension removed
extension(path)       str   returns extension
cleaveext(path)       tuple returns (root, ext)
addext(path,ext)      str   returns path with extension added
fopen(path,mode)      fd    just like normal open, but errors trigger ScriptError
===================== ===== =====================================================


Path lists
----------

Cartesian Product
~~~~~~~~~~~~~~~~~

Create a list of files from path fragments::

   all_paths(comp, ...)

Like with join(), the components are combined to form a path, but in this case 
each component may be a list. The results is the various components are combined 
in a Cartesian product to form a list. For example:

.. code-block:: python

   >>> paths = all_paths(['A', 'B'], ['a', 'b'], ['1', '2'])
   >>> for p in paths:
   ...     print(p)
   A/a/1
   A/a/2
   A/b/1
   A/b/2
   B/a/1
   B/a/2
   B/b/1
   B/b/2

This function is similar to brace expansion in the shell. For example:

.. code-block:: python

   all_paths(['a'], ['d', 'c', 'b'], ['e'])

is equivalent to the following shell brace expansion::

   a{d,c,b}e

and each produces: ade ace abe.

Globbing
~~~~~~~~

Expand glob patterns::

    expand(glb)
    dexpand(glb)
    fexpand(glb)

Expand glob pattern into all files or directories, into directories only, or 
into files only.

The all_paths iterator is different in an important way from the expand 
iterators.  The all_paths iterator will generate paths that may not currently 
exist on your filesystem, whereas the expand iterators only yield existing 
paths. In terms of shell expansions, all_paths is like {}, whereas expand is 
like \*.

Walk File Hierarchy
~~~~~~~~~~~~~~~~~~~

::

    fwalk(path, accept=None, reject=None, exclude=None)

Returns a generator that iterates through all the files contained in a
directory hierarchy.  Accept and reject criteria are glob strings, or lists
of glob strings. For a file to be returned its name must not match any of
the reject criteria if any are given, and it must match one of the accept
criteria, if any are given.  If no criteria are given, all files are
returned. Exclude is a file or directory or a list of files or directories
to exclude. Each is specified relative from the current working directory.

Filtering
~~~~~~~~~

Examine the tail of each path in a list and filter out those that match a given 
glob pattern.

    filter(glb, paths)


Executing Programs
------------------

The following classes and functions are used to execute external programs from 
within Python.

Command (Cmd)
~~~~~~~~~~~~~

A class that runs an external program::

   Cmd(cmd[, modes][, encoding])

*cmd* may be a list or a string.
*mode* is a string that specifies various options. The options are specified 
using a single letter, with upper case enabling the option and lower case 
disabling it:

   |  S, s: Use, or do not use, shell
   |  O, o: Capture, or do not capture, stdout
   |  E, e: Capture, or do not capture, stderr
   |  W, s: Wait, or do not wait, for command to terminate before proceeding

If a letter corresponding to a particular option is not specified, the default 
is used for that option.  In addition, one of the following may be given, and it 
must be given last

   |  ``*``: accept any output status code
   |  N: accept any output status code equal to or less than N
   |  M,N,...: accept status codes M, N, ...

If you do not specify the status code behavior, only 0 is accepted as normal 
termination, all other codes will be treated as errors.

For example, to run diff you might use::

   diff = Cmd('diff test ref', 'sOEW1')
   diff.run()
   differences = diff.stdout

Use of O in the modes allows access to stdout, which is needed to access the 
differences. Specifying E also allows access to stderr, which in this case is 
helpful in case something goes wrong because it allows the error handler to 
access the error message generated by diff. Specifying W indicates that run() 
should block until diff completes. Specifying 1 indicates that either 0 or 1 are 
valid output status codes; any other code output by diff would be treated as an 
error.

If you do not indicate that stdout or stderr should be captured, those streams 
remain connected to your TTY. You can specify a string to the run() method, 
which is fed to the program through stdin. If you don't specify anything the 
stdin stream for the program also remains connected to the TTY.

If you indicate that run() should return immediately without out waiting for the 
program to exit, then you can use the wait() and kill() methods to manage the 
execution. For example::

   diff = Cmd(['gvim', '-d', lfile, rfile], 'w')
   diff.run()                                                                    
   try:
       diff.wait()
   except KeyboardInterrupt:
       diff.kill()


Run and Sh
~~~~~~~~~~

Run and Sh are subclasses of Cmd. They are the same except that they both run 
the program right away (you would not explicitly run the program with the 
run()).  Run does not use a shell by default where as Sh does.

run, sh, bg, shbg
~~~~~~~~~~~~~~~~~

These are functions that run a program without capturing their output::

   run(cmd, stdin=None, accept=0, shell=False)
   sh(cmd, stdin=None, accept=0, shell=True)
   bg(cmd, stdin=None, shell=False)
   shbg(cmd, stdin=None, shell=True)

run and sh block until the program completes, whereas bg and shbg do not. run 
and bg do not use a shell by default where as sh and shbg do. accept specifies 
the exit status codes that will be accepted without being treated as being an 
error. If you specify a simple number, than any code greater than thatvalue is 
treated as an error. If you provide a collection of numbers in a tuple or list, 
then any code not found in the collection is considered an error.

which
~~~~~

Given a name, a path, and a collection of read, write, or execute flags, this 
function returns the locations along the path where a file or directory can be 
found with matching flags::

   which(name, path=None, flags=os.X_OK)
    
By default the path is specified by the PATH environment variable and the flags 
check whether you have execute permission.

fopen
~~~~~

An alternative version of *open* named *fopen* is provided::

    with fopen(<filepath>, [mode='r'], [encoding=default_encoding]) as f:
        ...

It differs from *open* in that:

1. it generates a ScriptError rather than an IOError if there is a problem 
   opening the file
2. it will use the default encoding (see script preferences below) if none is 
   specified.


Errors
------

These functions and classes all generate ScriptError. Generally, one would wrap 
an entire script in a single try/except block rather than putting them on each 
command::

   try:
       ...
   except ScriptError as err:
       sys.exit(str(err))

It is also possible to specify that a script error will always print and error 
message and then simply terminate the program without returning (see script 
preferences).

Script Preferences
------------------

The program has the following default behaviors:

   | exit_upon_error (default=False)
   | expanduser (default=True)
   | expandvars (default=False)
   | encoding (default='utf-8')
   | show_cmd_in_errors (default=True)

If you wish to change these behaviors, use the following example as guidance::

   script_prefs.set('exit_upon_error', True)

The value of *show_cmd_in_errors* may be False, True (first word only), or 
'full' (the entire command).

Alternatively, script_prefs is callable and you can set the preferences using 
keyword arguments::

   script_prefs(exit_upon_error=True, expanduser=True, expandvars=False)

To Do
-----

There are still some obvious extensions that would be useful and open issues to 
resolve. They are:

1. missing a recursive file generator that will walk an entire file hierarchy.
2. Need to review function names to assure they are the best available (short, 
   memorable, unlikely to clash).
3. Currently there is considerable inconsistency between the behavior of 
   shell-like command functions provided in this package and those provided by 
   the shell. For example, the shell version of rm will not delete a directory 
   without adding flags, whereas this one will. It would be possible to make 
   them consistent if a flags argument were added to allow the default behavior 
   to be overridden easily. The flags argument would be similar to that provided 
   by Cmd.
4. Should we switch the order of the arguments to the ls and filter functions?
5. The documentation could use some work (more examples).
