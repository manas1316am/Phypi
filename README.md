# phypi

This is a physics python library

## Installation

Run the following command to install phypi

```python
pip install phypi
```

## Usage

This Code doesnt work now

```python
    from phypi.test import test
    # Testing the code
    test.say_hello()
    # Generate "Hello, user"
    test.say_hello("user")
```

## Constants used in phypi

To work with physics, we have to define a lot of constants initially, because many discoveries and formulas are based on that theorem.<br/><br/>We added maximum number of constants in physics available to us under <b>constant.py</b><br/><br/>You can easilt use it by calling it.

```python
    import constant
    # Printing speed of light
    print(constant.c)
```

## Develop with phypi

To install phypi, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
    $ pip install -e .[dev]
```
