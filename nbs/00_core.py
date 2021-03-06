# ---
# jupyter:
#   jupytext:
#     formats: ipynb,md,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
# default_exp core

# %% [markdown]
# # test_nbdev
#
# > API details.

# %%
#hide
from nbdev.showdoc import *


# %% [markdown]
# ## functions

# %%
#export
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'


# %% [markdown]
# ### examples

# %% [markdown]
# #### run function

# %%
say_hello("Wilbur")

# %% [markdown]
# #### make svg

# %%
from IPython.display import display,SVG

# %%
display(SVG('<svg height="100"><circle cx="50" cy="50" r="40"/></svg>'))

# %% [markdown]
# ### tests 

# %%
assert say_hello("Jeremy")=="Hello Jeremy!"

# %%
assert say_hello("Chris")!="Hello Jeremy!"


# %% [markdown]
# ## classes

# %%
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


# %%
show_doc(HelloSayer.say)

# %% [markdown]
# ### examples

# %% [markdown]
# #### create instance

# %% [markdown]
# We can define an instance of the class `HelloSayer` by passing the appropriate parameters to the constructor (in this case a single string containing the object of prospective saying).

# %%
o = HelloSayer("Alexis")

# %% [markdown]
# It is possible to simply print the `__dict__` associated to any instance of the object as:

# %%
print(o.__dict__)

# %% [markdown]
# This works even if there is no `__str__` method defined. Otherwise, it is probably better to use the internally defined `__repr__` and `__str__` as: 

# %%
print([o])
print(o)
print(o.to)
o.say()


# %% [markdown]
# #### interrogate instance

# %% [markdown]
# If you just want a list of the methods associated to an object, you can use a list comprehension as:

# %%
def get_object_methods(object):
    return [method_name for method_name in dir(object)
                  if callable(getattr(object, method_name))]


# %%
print(get_object_methods(o))

# %% [markdown]
# If it is necessary to get a comprehensive listing of the contents of an object, use the `dir` function as:

# %%
dir(o)

# %% [markdown]
# It is also possible to use the python `inspect` module to get more detailed information about the structure of an object:

# %%
import inspect
inspect.getmembers(o)

# %% [markdown]
# You can also simply call the help function on your instance.

# %%
# ?help

# %%
help(o)

# %%
