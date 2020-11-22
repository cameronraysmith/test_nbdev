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

# test_nbdev

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

## classes

```python
#export
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): 
        "Define the object of the prospective saying"
        self.to = to
        
    def __repr__(self):
        "Represent instances for debugging"
        repr = "to: %s" % (self.to)
        return repr
    
    def __str__(self):
        "Represent instances when printed (see https://stackoverflow.com/a/49282111/446907)"
        return  str(self.__class__) + '\n' + '\n'.join((str(item) + ' = ' + str(self.__dict__[item]) for item in sorted(self.__dict__)))
    
    def say(self):
        "Do the saying"
        return say_hello(self.to)
```

```python
show_doc(HelloSayer.say)
```

### examples


We can define an instance of the class `HelloSayer` by passing the appropriate parameters to the constructor (in this case a single string containing the object of prospective saying).

```python
o = HelloSayer("Alexis")
```

It is possible to simply print the `__dict__` associated to any instance of the object as:

```python
print(o.__dict__)
```

This works even if there is no `__str__` method defined. Otherwise, it is probably better to use the internally defined `__repr__` and `__str__` as: 

```python
print([o])
print(o)
print(o.to)
o.say()
```
