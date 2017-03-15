SkelePrint UI - G Code Generator
########################################

The SkelePrint user interface allows you to generate g code for the SkelePrint 3D printer.  


.. class:: no-web

    .. image:: https://github.com/shubhjagani/skeleprint_ui/blob/master/screen_shot.png
        :alt: SkelePrint UI
        :width: 100%
        :align: center


.. class:: no-web no-pdf

.. contents::

.. section-numbering::
    



Installation
============


Installing Python
------------------


SkelePrint UI relies on python for processing. If you already have Python installed, you can skip ahead to the next step. 

Mac OSX:

.. code-block:: bash

    sudo brew install python

You may be asked to enter your password

If you do not have homebrew installed, open up terminal and type:

.. code-block:: bash
	ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


Windows

Download and install the Python IDE using the link below:

`Python IDE`_


Installing pip
--------------

Download and save `get-pip.py`_ into any folder 

Open up Python IDE or Terminal, cd into the folder with the downloaded file and run the following command:

.. code-block:: bash

    cd ./Downloads/ 

    sudo python get-pip.py

You can also open the get-pip.py using Python IDE and run the script  


Installing SkelePrint UI
------------------------

A universal installation method (that works on Windows, Mac OS X, Linux, …,
and always provides the latest version) is to use `pip`_. All you have to do now is open terminal or command prompt and type: 


.. code-block:: bash

    # Make sure we have an up-to-date version of pip and setuptools:
    $ pip install --upgrade skeleprint_ui


Running SkelePrint UI
----------------------

After having successfully installed skeleprint_ui package simply open up terminal or command prompt and type:

.. code-block:: bash

    $ python

    $ import skeleprint_ui

A shortcut will be created on your desktop with the filename : SkelePrint_UI.pyc 

You can now execute this file to run the tool path generator. 

Meta
====

Interface design
----------------

The interface was designed using tkinter for Python. 


Authors
-------

`SkelePrint`_


.. _pip: https://pip.pypa.io/en/stable/installing/
.. _Python IDE: https://www.python.org/downloads/release/python-2713/
.. _get-pip.py: https://bootstrap.pypa.io/get-pip.py
.. _SkelePrint: http://skeleprint.ca




