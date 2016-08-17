SymUnit
========

SymUnit is a symbolic unitest framework.

Documentation
   http://symunit.github.io
Mailing List
   https://groups.google.com/d/forum/symunit-discuss
Development
   https://github.com/symunit/symunit

   .. image:: https://api.travis-ci.org/symunit/symunit.svg?branch=master
            :target: https://travis-ci.org/symunit/symunit

   .. image:: https://readthedocs.org/projects/symunit/badge/?version=latest
            :target: https://readthedocs.org/projects/symunit/?badge=latest
      :alt: Documentation Status

   .. image:: https://coveralls.io/repos/symunit/symunit/badge.svg?branch=master
            :target: https://coveralls.io/r/symunit/symunit?branch=master


Download
--------

T.B.D.
[//]: # Get the latest version of Danata from
[//]: # https://pypi.python.org/pypi/danata/

::

    $ pip install symunit

To get the git version do

::

    $ git clone git://github.com/symunit/symunit.git

Decorator package is required for SymUnit.

::

    $ pip install decorator

Usage
-----

A quick example that finds the shortest path between two nodes in an undirected graph::

   >>> import networkx as nx
   >>> G = nx.Graph()
   >>> G.add_edge('A', 'B', weight=4)
   >>> G.add_edge('B', 'D', weight=2)
   >>> G.add_edge('A', 'C', weight=3)
   >>> G.add_edge('C', 'D', weight=4)
   >>> nx.shortest_path(G, 'A', 'D', weight='weight')
   ['A', 'B', 'D']


Bugs
----

Our issue tracker is at https://github.com/symunit/symunit/issues.
Please report any bugs that you find.  Or, even better, fork the repository on
GitHub and create a pull request.  We welcome all changes, big or small, and we
will help you make the pull request if you are new to git
(just ask on the issue).

License
-------

T.B.D.
[//]: # Distributed with a ... license; see LICENSE.txt::
[//]: #
[//]: #   Copyright (C) 2016 SymUnit Developers
[//]: #   Youngsung Kim<grnydawn@gmail.com>
