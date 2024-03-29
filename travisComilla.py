language: python
python:
  - "3.5"
  # PyPy versions
#  - "pypy"   # currently Python 2.7.13, PyPy 7.1.1 
#  - "pypy3"  # currently Python 3.6.1,  PyPy 7.1.1-beta0
# command to install dependencies
install:
- "pip install mock==2.0"
- "pip install coverage"
# command to run tests
script:
- coverage run testing/test.py
- coverage run testing/test_sut.py
- coverage report
