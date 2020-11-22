---
jupyter:
  jupytext:
    formats: ipynb,md,py:percent
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.7.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
# default_exp core
```

# module name here

> API details.

```python
#hide
from nbdev.showdoc import *
```

```python
#export
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'
```

## examples


### run function

```python
say_hello("Wilbur")
```

### make svg

```python
from IPython.display import display,SVG
```

```python
display(SVG('<svg height="100"><circle cx="50" cy="50" r="40"/></svg>'))
```

## tests 

```python
assert say_hello("Jeremy")=="Hello Jeremy!"
```

```python
assert say_hello("Chris")!="Hello Jeremy!"
```

```python

```
