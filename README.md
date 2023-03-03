# sphinx-test

An example Python project with sphinx documentation to demonstrate a warning about a missing attribute.

The warning can be triggered with:

    sphinx-build -b html docs build

This produces this output:

```
Running Sphinx v5.3.0
loading pickled environment... done
[autosummary] generating autosummary for: index.rst, stubs/test_project.Base.attr.rst, stubs/test_project.Base.rst, stubs/test_project.Child.rst
WARNING: [autosummary] failed to import test_project.Child.attr.
Possible hints:
* AttributeError: type object 'Child' has no attribute 'attr'
* ModuleNotFoundError: No module named 'test_project.Child'
* ImportError:
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 0 source files that are out of date
updating environment: 0 added, 0 changed, 0 removed
looking for now-outdated files... none found
no targets are out of date.
build succeeded, 1 warning.
```

Additionally, the documentation for `Child` does not include the inherited `attr` attribute (the documentation for `Base` does include it).

The problem is that Sphinx detects the docstring on the `attr` attribute defined in `__init__` here:

```python
class Base:
    """Parent class"""
    def __init__(self):
        self.attr = 0
        """Base class attribute"""
```

but then fails to find the attribute on the class that inherits from `Base` here:

```python
class Child(Base):
    """Child class"""
    def print_attr(self):
        """Print attr value"""
        print(self.attr)
```

It seems like sphinx just imports the module and inspects the class attributes, so it does not find instance attributes defined in `__init__` (or at not ones defined in an inherited `__init__`).

The template code in `class.rst` that searches for the attribute is:

```
   {% for item in all_attributes %}
      {%- if not item.startswith('_') %}
      {{ name }}.{{ item }}
      {%- endif -%}
   {%- endfor %}
```

Replacing this with

```
{% for item in attributes %}
   .. autoattribute:: {{ item }}
{%- endfor %}
```

bypasses the warning but also does not document `attr` for `Base` or `Child`.
