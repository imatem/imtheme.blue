Using the development buildout
==============================

Create a virtualenv in the package::

    $ virtualenv-2.7 --no-setuptools --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout::

    $ ./bin/buildout

Start Plone in foreground:

    $ ./bin/instance fg


Running tests
-------------

    $ tox

list all tox environments:

    $ tox -l
    py27-Plone43
    build_instance
    code-analysis
    lint-py27
    coverage-report

run a specific tox env:

    $ tox -e py27-Plone43
