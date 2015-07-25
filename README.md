This colorscheme is based on the popular Solarized dark color scheme,
specifically the Solaron-Dark version Dave Stewart ([@we3geeks](https://github.com/we3geeks))
did [a while ago](https://github.com/we3geeks/komodo-color-schemes).

The main difference is that I toned down the heavy color use a bit, so that
your eyes can relax a little.

# Building

The colors are defined in Solarmodo.scheme, for finer grained control you edit
the Solarmodo.ksf file, which the colors get injected into via the little comments
you see, eg:

```'fore': 10002730, # :strings```

That entry would be replaced by the color value for `strings`.

To build the ksf just invoke build.py, ie. `python build.py`.

For quick testing I just change whatever I wish to change and then invoke

```python build.py && komodo Solarmodo.ksf```

Unfortunately you'll have to import it with a new scheme each time. Note to self:
*implement scheme updating*.