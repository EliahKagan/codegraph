<!-- SPDX-License-Identifier: 0BSD -->

# codegraph - graphs in software engineering

[Graphs](https://en.wikipedia.org/wiki/Graph_theory) have many applications in
computer science and software engineering, because they are a general model of
relatedness. This repository is a collection of examples where something in
software engineering has a useful and interesting graph structure that is
straightforward—and fun—to visualize programmatically. Graphs are extremely
versatile, so these examples are necessarily incomplete in the extreme.

These [graphs](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))
should not be confused with [the other thing called a
graph](https://en.wikipedia.org/wiki/Graph_of_a_function), nor with
[plots](https://en.wikipedia.org/wiki/Plot_(graphics)) (which relate to that
other thing).

## License

[0BSD](https://spdx.org/licenses/0BSD.html). See [**`LICENSE`**](LICENSE).

## The examples

Currently all examples are in Python, with all the code in Jupyter notebooks.

- [`builtin_types.ipynb`](builtin_types.ipynb) - inheritance hierarchy of
  Python builtins
- [`exceptions.ipynb`](exceptions.ipynb) - inheritance hierarchy of Python
  exceptions
- [`fibonacci.ipynb`](fibonacci.ipynb) - relationship of Fibonacci subproblems
- [`git_graph.ipynb`](git_graph.ipynb) - source control commit graphs
- [`nested_sequences.ipynb`](nested_sequences.ipynb) - heterogeneous nested
  collections
- [`nested_tuples.ipynb`](nested_tuples.ipynb) - homogeneous nested collections

## Installation

Clone the repository and go into the cloned directory:

```sh
git clone https://github.com/EliahKagan/codegraph
cd codegraph
```

Then you can install dependencies using `conda` or using `pipenv`.

### `conda`

To use [`conda`](https://en.wikipedia.org/wiki/Conda_(package_manager)), make
sure `conda` is installed (if not, I suggest
[Miniforge](https://github.com/conda-forge/miniforge)). Then run:

```sh
conda env create
```

### `pipenv`

To use [`pipenv`](https://pipenv.pypa.io/en/latest/), make sure `pipenv` is
installed.

Also install [Graphviz](https://graphviz.org/) on your system (`conda` takes
care of that but `pipenv` doesn't). Graphviz 3.0.0 or higher is recommended, to
avoid [scaling problems](https://github.com/EliahKagan/codegraph/issues/5).
(Using `conda` instead of `pipenv` may be the easiest way to get a new version
of GraphViz on some systems.)

Then run:

```sh
pipenv install -d
```

If you already have an application for running code in Jupyter notebooks that
you want to use, such as [VS Code](https://code.visualstudio.com/) with the
[Jupyter
extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter),
then you can omit the `-d`.

As for installing Graphviz, most systems' package managers will install it, and
the package name is usually Graphviz. If you can't find it, look into what
package provides the `dot` command. On Windows, if you want to install Graphviz
via a package manager, you can use [`scoop`](https://scoop.sh/).

## Usage

### Way 1: JupyterLab

First, go to the directory where you ran `conda` or `pipenv` before and
activate the environment you created.

If you used `conda`, run:

```sh
conda activate codegraph
```

If you used `pipenv`, run:

```sh
pipenv shell
```

Then run JupyterLab:

```sh
jupyter lab
```

### Way 2: Another application

If you already have another application you prefer for opening and running code
in Jupyter notebooks, you can use that.

In particular, you can use [VS Code with the Jupyter Notebooks
extension](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
If you do, make sure the environment you created (with `conda` or `pipenv`) is
selected. If VS Code offers to install `ipykernel` or any other dependency, you
should decline and select the appropriate environment.

## A simpler version

An old, simpler version of some parts of this project is available on the
[**simple**](https://github.com/EliahKagan/codegraph/tree/simple) branch, and
may be of some interest.

## Acknowledgements

Some parts of this project were tested by, and were improved based on input
from, [**David Vassallo**](https://github.com/dmvassallo/cgrep). Furthermore,
significant parts were inspired by code I wrote for our project
[palgoviz](https://github.com/EliahKagan/palgoviz), and some code to create
nested tuple structures is derived from code there.

## See also

- [`object_graph.ipynb`](https://github.com/EliahKagan/palgoviz/blob/main/notebooks/object_graph.ipynb)
  in [palgoviz](https://github.com/EliahKagan/palgoviz).
