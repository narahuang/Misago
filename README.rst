======
Misago
======

.. image:: https://travis-ci.org/rafalp/Misago.png?branch=future
  :target: https://travis-ci.org/rafalp/Misago

.. image:: https://coveralls.io/repos/rafalp/Misago/badge.png?branch=future
  :target: https://coveralls.io/r/rafalp/Misago?branch=future

.. image:: https://landscape.io/github/rafalp/Misago/future/landscape.png
  :target: https://landscape.io/github/rafalp/Misago/future


**Development Status: Pre-Alpha**

Misago aims to be complete, featured and modern forum solution that has no fear to say 'NO' to common and outdated opinions about how forum software should be made and what it should do.

If you can run Python apps on your hosting and you are looking for modern solution using latest paradigms in web development, or you are Django developer and forum is going to be core component of your next project then Misago is option for you!

* **Homepage:** http://misago-project.org/
* **Documentation:** http://misago.readthedocs.org/en/latest/
* **Code & BugTracker:** https://github.com/rafalp/Misago/


Installing and updating
-----------------------

Please note that branch *future* is used for project's codebase cleanup and is not functional at the time of this writing. If you want to give Misago a spin, feel free to play with one of `previous releases <https://github.com/rafalp/Misago/releases>`_.

To install Misago setup and activate virtual environment and then fire following commands::

    python setup.py install
    misago-start.py testforum

Those commands will install Misago in your virtual environment and make pre-configured Misago site for you named "testforum" using "misago-start.py" script available successfull installation.

Now cd test forum and initialize database by using syncdb and migrate commands using manage.py::

    cd testforum
    python manage.py syncdb
    python manage.py migrate

Finally start development server using runserver command::

    python manage.py runserver


If server starts, you should be able to visit 127.0.0.1:8000 in your browser and see simple placeholder response from Misago, however as work on this branch is underway revisions may frequently introduce changes that will break runserver.


Bug reports, features and feedback
----------------------------------

If you have found bug, please report it on `issue tracker <https://github.com/rafalp/Misago/issues>`_.

For feature or support requests as well as general feedback please use `official forum <http://misago-project.org>`_ instead. Your feedback means much to the project so please do share your thoughts!


Contributing
------------

If you have fixed spelling mistake, wrote new tests or fixed a bug, feel free to open pull request.

Many issues are open for takes. If you've found one you feel you could take care of, please announce your intent in issue discussion before you start working. That way situations when more than one person works on solving same issue can be avoided.


Authors
-------

**Rafał Pitoń**

* http://rpiton.com
* http://github.com/rafalp
* https://twitter.com/RafalPiton


Copyright and license
---------------------

**Misago** - Copyright © 2014 `Rafał Pitoń <http://github.com/ralfp>`_
This program comes with ABSOLUTELY NO WARRANTY.

This is free software and you are welcome to modify and redistribute it under the conditions described in the license.
For the complete license, refer to LICENSE.rst