=================
fly.skels
=================

This package is used for quickly setup some basic namespace packages or buildout based packages.


-  create namespaced packages

    ::

        $ paster create -t fly_namespace fly.test
        $ find fly.test
        fly.test/
        fly.test/fly
        fly.test/fly/__init__.py
        fly.test/fly/test
        fly.test/fly/test/__init__.py
        fly.test/fly/__init__.pyc
        fly.test/setup.py
        fly.test/README.rst
        fly.test/fly.test.egg-info
        fly.test/setup.cfg


- create buildout based packages

    ::

        $ paster create -t fly_buildout example
        $ find example/
        example/
        example/bootstrap.py
        example/buildout.cfg
        example/example
        example/example/__init__.py
        example/example.egg-info
        example/README.rst
        example/setup.cfg
        example/setup.py

- create fully packages with namespace and buildout

    ::

        $ paster create -t fly_full fly.full
        $ find fly.full
        fly.full/
        fly.full/bootstrap.py
        fly.full/buildout.cfg
        fly.full/fly
        fly.full/fly/__init__.py
        fly.full/fly/__init__.pyc
        fly.full/fly/full
        fly.full/fly/full/__init__.py
        fly.full/fly.full.egg-info
        fly.full/README.rst
        fly.full/setup.cfg
        fly.full/setup.py


For more information, go to https://github.com/youngking/fly.skels

