eigengdb
========

This is a pretty printer for eigen types (with some support for stan-math
types), forked from upstream eigen.

Installation
------------

It is important to use the python/pip version which corresponds to your GDB
installation. You can find out more information using the `python` command in
GDB. For example, from GDB repl, you can find where GDB python will search for
packages.

.. code-block:: bash

   (gdb) python
   >import sys
   >print(sys.path)
   >end
   [..., '/path/to/site-packages', ...]

Then install using a corresponding python/pip (usually system pip).


From PyPI
~~~~~~~~~

.. code-block:: bash

   pip install eigengdb # Make sure to use system pip which matches GDB
   eigengdb_register_printers

From Source
~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/dmillard/eigengdb
   cd eigengdb
   python setup.py install # Make sure to use system python which matches GDB
   python bin/eigengdb_register_printers

License
-------

eigengdb is licensed under MPL2.0.
