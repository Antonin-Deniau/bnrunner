BNrunner
========

This package allow you to run scripts with a binaryninja student
instance and use the API to a certain extend.

All script executed with bnrunner will have a global variable named
*bv*, the BinaryView instance of the opened binary in binaryninja.

Getting Started
---------------

-  To use it you must load a binary with binaryninja, and have the
   `scripts_runner`_ plugin installed.
-  To start the script runner your must go to *Tools->[script_runner]
   start server* with an opened binary.
-  You can now execute scripts with it.

The scripts must look like this:

.. code:: python

    #!/usr/bin/env bnrunner
    from binaryninja import HighlightStandardColor

    block = bv.get_basic_blocks_at(0x8670)[0]
    block.highlight = HighlightStandardColor.BlueHighlightColor
    print(bv)

Or on Windows:

.. code:: python

    import bnrunner
    from binaryninja import HighlightStandardColor

    def main(): 
        block = bv.get_basic_blocks_at(0x8670)[0]
        block.highlight = HighlightStandardColor.BlueHighlightColor
        print(bv)

    bnrunner.run_from_path() if __name__ == '__main__' else main()

You can also launch script with the bnrunner executable in both platform
\`\ ``bnrunner script.py``

Installing
~~~~~~~~~~

-  Run: ``pip install bnrunner``

-  Now all the python scripts that you will execute with bnrunner will
   be sent to the binaryninja instance.

License
-------

This project is licensed under the MIT License - see the `LICENSE`_ file
for details

.. _scripts_runner: http://github.com/Antonin-deniau/bn_script_runner
.. _LICENSE: LICENSE
