eigengdb
========

This is a pretty printer for eigen types (with some support for stan-math
types), forked from upstream eigen.

Installation
------------

.. code-block:: bash

   git clone https://github.com/dmillard/eigengdb
   cd eigengdb
   python setup.py install # Make sure to use system python (which matches the GDB python version)
   echo -e "python\n__import__('eigengdb').register_eigen_printers()\nend" >> $HOME/.gdbinit

License
-------

eigengdb is licensed under MPL2.0.
