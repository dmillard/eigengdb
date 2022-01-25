eigengdb
========

This is a pretty printer for eigen types (with some support for stan-math
types). Much of the logic comes from upstream eigen. Formatting is handled
by `numpy`.

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

In Linux, you can also find the python used by checking the libraries linked to GDB.

.. code-block:: bash

   $ ldd $(which gdb) | grep python


Once you find the python interpreter used by GDB, install :code:`eigengdb` using a corresponding python/pip (usually system pip).


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
   
In the resulting gdb prompt that shows up, add your breakpoint and run the file

.. code-block:: bash

   b 7
   run # run until breakpoint
   p mat # shows eigengdb formatting

Customizing the printer
-----------------------
Since NumPy is used to render the matrix, you can adjust `NumPy's printing options <https://numpy.org/doc/stable/reference/generated/numpy.set_printoptions.html>`_ in your gdb session to tweak the appearance, for example:

.. code-block:: bash

   (gdb) p lin_invar_pref
   $11 = Eigen::Matrix<double,4,12,ColMajor> (data ptr: 0x613000001380)
   [[ 1.00000000e+00  3.16292670e-01  1.05028445e+00  5.02844469e-02
      1.31629267e+00 -2.19900950e-01 -1.69616503e-01 -1.19332056e-01
     -6.90476092e-02 -1.87631623e-02  3.15212845e-02  1.92783441e-01]
    [ 0.00000000e+00  1.00000000e+00  1.88824955e-01  1.88824955e-01
      1.00000000e+00 -8.36652088e-01 -6.47827133e-01 -4.59002178e-01
     -2.70177223e-01 -8.13522683e-02  1.07472687e-01  3.26695824e-01]
    [ 0.00000000e+00  0.00000000e+00  1.00000000e+00  1.00000000e+00
      6.83197897e-16 -2.18264785e-01  7.81735215e-01  1.78173522e+00
      2.78173522e+00  3.78173522e+00  4.78173522e+00 -4.36529569e-01]
    [ 0.00000000e+00  0.00000000e+00  0.00000000e+00  0.00000000e+00
      0.00000000e+00  3.97719125e-01  3.97719125e-01  3.97719125e-01
      3.97719125e-01  3.97719125e-01  3.97719125e-01  7.95438250e-01]]
   
   (gdb) python
   >import numpy as np
   >np.set_printoptions(linewidth=200, formatter={'float': lambda x: "{:5.2f}".format(x) if x !=0 else "     "})
   >end
   (gdb) p lin_invar_pref
   $12 = Eigen::Matrix<double,4,12,ColMajor> (data ptr: 0x613000001380)
   [[ 1.00  0.32  1.05  0.05  1.32 -0.22 -0.17 -0.12 -0.07 -0.02  0.03  0.19]
    [       1.00  0.19  0.19  1.00 -0.84 -0.65 -0.46 -0.27 -0.08  0.11  0.33]
    [             1.00  1.00  0.00 -0.22  0.78  1.78  2.78  3.78  4.78 -0.44]
    [                               0.40  0.40  0.40  0.40  0.40  0.40  0.80]]


License
-------

eigengdb is licensed under MPL2.0.
