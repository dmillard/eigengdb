eigengdb
========

This is a pretty printer for eigen types (with some support for stan-math
types). Much of the logic comes from upstream eigen.

Motivation
----------

Your debugging output shouldn't look like this:

.. code-block::

   (gdb) p mat
   $1 = {<Eigen::PlainObjectBase<Eigen::Matrix<double, 4, 4, 0, 4, 4> >> = {<Eigen::MatrixBase<Eigen::Matrix<double, 4, 4, 0, 4, 4> >> = {<Eigen::DenseBase<Eigen::Matrix<double, 4, 4, 0, 4, 4> >> = {<Eigen::DenseCoeffsBase<Eigen::Matrix<double, 4, 4, 0, 4, 4>, 3>> = {<Eigen::DenseCoeffsBase<Eigen::Matrix<double, 4, 4, 0, 4, 4>, 1>> = {<Eigen::DenseCoeffsBase<Eigen::Matrix<double, 4, 4, 0, 4, 4>, 0>> = {<Eigen::EigenBase<Eigen::Matrix<double, 4, 4, 0, 4, 4> >> = {<No data fields>}, <No data fields>}, <No data fields>}, <No data fields>}, <No data fields>}, <No data fields>}, m_storage = {m_data = {array = {
             0.68037543430941905, -0.21123414636181392, 0.56619844751721171, 0.59688006695214657,
             0.82329471587356862, -0.60489726141323208, -0.32955448857022196, 0.53645918962380801,
             -0.44445057839362445, 0.10793991159086103, -0.045205896275679502, 0.25774184952384882,
             -0.27043105441631332, 0.026801820391231024, 0.90445945034942565,
             0.8323901360074013}}}}, <No data fields>}

But rather like this!

.. code-block::

   (gdb) p mat
   $1 = Eigen::Matrix<double,4,4,ColMajor> (data ptr: 0x7fffffffdde0)
   [[ 0.68037543  0.82329472 -0.44445058 -0.27043105]
    [-0.21123415 -0.60489726  0.10793991  0.02680182]
    [ 0.56619845 -0.32955449 -0.0452059   0.90445945]
    [ 0.59688007  0.53645919  0.25774185  0.83239014]]


Installation
------------

It is important to use the python/pip version which corresponds to your GDB
installation. You can find out more information using the :code:`python` command in
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

Test
----

There is an example program you can play with in the :code:`examples/` directory.

.. code-block:: bash

   cd examples
   make
   make debug

License
-------

eigengdb is licensed under MPL2.0.
