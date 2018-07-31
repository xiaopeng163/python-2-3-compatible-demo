# python-2-3-compatible-demo

This repo is used to demo python 2-3 compatible code, and the `master` branch only support python 2,
the branch `py23` support both python 2 and 3.

Please use tox to do the test

on `master` branch:

```bash
tox
py27 installed: astroid==1.6.5,backports.functools-lru-cache==1.5,configparser==3.5.0,coverage==4.0.3,discover==0.4.0,enum34==1.1.6,flake8==3.5.0,flake8-import-order==0.13,funcsigs==1.0.2,futures==3.2.0,isort==4.3.4,lazy-object-proxy==1.3.1,mccabe==0.6.1,mock==2.0.0,nose==1.3.7,pbr==4.2.0,pycodestyle==2.3.1,pyflakes==1.6.0,pylint==1.7.2,singledispatch==3.4.0.3,six==1.11.0,wrapt==1.10.11
py27 runtests: PYTHONHASHSEED='1340649021'
py27 runtests: commands[0] | coverage run run_test.py
test_binary_search_find (py23.tests.algorithms.test_binary_search.TestBinarySearch) ... ok
test_binary_search_not_find (py23.tests.algorithms.test_binary_search.TestBinarySearch) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
py27 runtests: commands[1] | coverage report -m
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
py23/algorithms/binary_search.py      11      0   100%
___________________________________________________________________________________________ summary ____________________________________________________________________________________________
  py27: commands succeeded
  congratulations :)
```

on `py23` branch:

```bash
py27 installed: astroid==1.6.5,backports.functools-lru-cache==1.5,configparser==3.5.0,coverage==4.5.1,discover==0.4.0,enum34==1.1.6,flake8==3.5.0,flake8-import-order==0.18,funcsigs==1.0.2,futures==3.2.0,isort==4.3.4,lazy-object-proxy==1.3.1,mccabe==0.6.1,mock==2.0.0,nose==1.3.7,pbr==4.2.0,pycodestyle==2.4.0,pyflakes==1.6.0,pylint==1.9.3,singledispatch==3.4.0.3,six==1.11.0,wrapt==1.10.11
py27 runtests: PYTHONHASHSEED='1477191945'
py27 runtests: commands[0] | coverage erase
py27 runtests: commands[1] | coverage run run_test.py
test_binary_search_find (py23.tests.algorithms.test_binary_search.TestBinarySearch) ... ok
test_binary_search_not_find (py23.tests.algorithms.test_binary_search.TestBinarySearch) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK
py27 runtests: commands[2] | coverage report -m
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
py23/algorithms/binary_search.py      12      0   100%
py36 create: /Users/penxiao/Documents/VSProjects/github/python-2-3-compatible-demo/.tox/py36
py36 installdeps: -r/Users/penxiao/Documents/VSProjects/github/python-2-3-compatible-demo/test-requirements.txt, -r/Users/penxiao/Documents/VSProjects/github/python-2-3-compatible-demo/requirements.txt
py36 installed: astroid==2.0.1,coverage==4.5.1,discover==0.4.0,flake8==3.5.0,flake8-import-order==0.18,isort==4.3.4,lazy-object-proxy==1.3.1,mccabe==0.6.1,mock==2.0.0,nose==1.3.7,pbr==4.2.0,pycodestyle==2.4.0,pyflakes==1.6.0,pylint==2.0.1,six==1.11.0,typed-ast==1.1.0,wrapt==1.10.11
py36 runtests: PYTHONHASHSEED='1477191945'
py36 runtests: commands[0] | coverage erase
py36 runtests: commands[1] | coverage run run_test.py
test_binary_search_find (py23.tests.algorithms.test_binary_search.TestBinarySearch) ... ok
test_binary_search_not_find (py23.tests.algorithms.test_binary_search.TestBinarySearch) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
py36 runtests: commands[2] | coverage report -m
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
py23/algorithms/binary_search.py      12      0   100%
___________________________________________________________________________________________ summary ____________________________________________________________________________________________
  py27: commands succeeded
  py36: commands succeeded
  congratulations :)
```