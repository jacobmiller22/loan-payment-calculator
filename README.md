Get deps with pipenv `pipenv sync`. See [pipenv docs](https://pipenv.pypa.io/en/latest/)

Activate virtual environment with `pipenv shell`

Run directly with `python3 calculator.py 5888 "[[5000, 0.06],[10000, 0.05],[8000, 0.07]]"`

First argument is the amount we can pay, second argument is a string representation of a 2xN matrix where column 1 is the principal remaining on the loan and column 2 is the annual percentage rate of the loan

Or run tests with `python3 -m pytest . -vrP`
