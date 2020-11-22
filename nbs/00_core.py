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


# %%
#export
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'


# %% [markdown]
# ## examples

# %% [markdown]
# ### run function

# %%
say_hello("Wilbur")

# %% [markdown]
# ### make svg

# %%
from IPython.display import display,SVG

# %%
display(SVG('<svg height="100"><circle cx="50" cy="50" r="40"/></svg>'))

# %% [markdown]
# ## tests 

# %%
assert say_hello("Jeremy")=="Hello Jeremy!"

# %%
assert say_hello("Chris")!="Hello Jeremy!"

# %%
