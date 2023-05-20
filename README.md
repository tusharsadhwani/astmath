# astmath

Evaluate Python arithemetic expressions safely.

This package can help evaluate Python expressions, without any risk of
code execution.

## Installation

```
pip install astmath
```

## Usage

Use it in the CLI:

```console
$ astmath '40 + 2'
42
$ astmath '"foobar" * 2'
foobarfoobar
```

Or via the API:

```pycon
>>> import astmath
>>> astmath.eval("2 + 3 * 4")
14
>>> astmath.eval("foo" * 3)
'foofoofoo'
```

## Local Development / Testing

- Create and activate a virtual environment
- Run `pip install -r requirements-dev.txt` to do an editable install
- Run `pytest` to run tests

## Type Checking

Run `mypy .`

## Create and upload a package to PyPI

Make sure to bump the version in `setup.cfg`.

Then run the following commands:

```bash
rm -rf build dist
python setup.py sdist bdist_wheel
```

Then upload it to PyPI using [twine](https://twine.readthedocs.io/en/latest/#installation):

```bash
twine upload dist/*
```
