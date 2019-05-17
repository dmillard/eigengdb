eigengdb
========

This is a pretty printer for eigen types (with some support for stan-math
types), forked from upstream eigen.

Installation
------------

From PyPI
~~~~~~~~~

.. code-block:: bash

   pip install eigengdb # Make sure to use system pip which matches GDB

From Source
~~~~~~~~~~~

.. code-block:: bash

   git clone https://github.com/dmillard/eigengdb
   cd eigengdb
   python setup.py install # Make sure to use system python which matches GDB
   echo -e "python\n__import__('eigengdb').register_eigen_printers(None)\nend" >> $HOME/.gdbinit

License
-------

eigengdb is licensed under MPL2.0.
