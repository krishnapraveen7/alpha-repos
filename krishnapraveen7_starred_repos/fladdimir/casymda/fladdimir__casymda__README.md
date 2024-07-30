# BPMN-based creation of SimPy discrete event simulation models

Wouldn't it be _cool_ to combine the block-based process modeling experience of commercial discrete event simulation packages with the amenities of proper IDE-based source-code editing?
(Think Arena / Anylogic / ExtendSim / Plant Simulation / ... but with simple integration of third-party libraries, industry-standard interfaces, unit- and integration testing, dockerization, serverless execution in the cloud of your choice... and even actually working auto-completion! _:D_)

And all that not only for free, but using the worlds most popular language for data analytics and machine learning?

_Casymda_ enables you to create [SimPy3](https://simpy.readthedocs.io/en/latest/) simulation models, with help of BPMN and the battle-tested [Camunda-Modeler](<http://www.bpmn.io>).

Created BPMN process diagrams are parsed and converted to Python-code, combining visual oversight of model structure with code-based definition of model behavior.
Immediately executable, including a token-based process animation, allowing for space-discrete entity movements, and ready to be wrapped as a gym-environment to let a machine-learning algorithm find a control strategy.

Further information and sample projects:

- [https://fladdimir.github.io/](https://fladdimir.github.io/tags/simpy/)

## Installation

From [PyPI](https://pypi.org/project/casymda/):

``` l
pip install casymda
```

## Features

- connectable blocks for processing of entities
- graphical model description via camunda modeler
- process visualization browser-based or via tkinter
- space-discrete tilemap-movements of entities
- gradually typed (checkout [pyright](https://github.com/microsoft/pyright) for vscode)

Coming soon:

- automated model generation from process event-logs via [PM4Py](https://pypi.org/project/pm4py/)

## Examples

Basic features are illustrated as part of the example models (which also serve as integration tests):

- basics:
  - bpmn-based generation of a simple model file
  - run the generated model
  - process visualization via tkinter
  - browser-based visualization (served with [flask](https://palletsprojects.com/p/flask/), animated with [pixijs](https://www.pixijs.com/))
- resources:
  - seize and release a resource via graphical modeling
- tilemap:
  - entity movement along a shortest path defined by a csv-tilemap (built on networkx: <https://networkx.github.io/>)

For setup just clone the repository and install casymda ([virtual environment](https://docs.python.org/3/tutorial/venv.html) recommended). See [basics-visual-run-tkinter](exec/basics/visual_run.py) for an example of how to cope with python-path issues.

## Design

- [Model generation and execution](diagrams/model+execution.pdf)
- [Blocks and animation](diagrams/blocks+animation.pdf)

## Development

This project trusts [Black](https://black.readthedocs.io/en/stable/) for formatting, [Sonarqube](https://www.sonarqube.org/) for static code analysis, and [pytest](https://docs.pytest.org/en/latest/) for unit & integration testing. Developed and tested on Linux (Ubuntu 20.04), Python 3.8.5.
Tests can be carried out inside a docker-container, optionally including an installation from pypi to verify a successful upload.

### Sonarqube

sonarqube server (public docker image):

``` l
docker-compose up sonarqube
```

sonar-scanner (public docker image):

``` l
docker-compose up analysis
```

(run a docker-based unit-test first for coverage-reporting)  
(remember to share your drive via Docker-Desktop settings if necessary, to be re-applied after each password change)

### Tests

``` l
pytest --cov-report term --cov=src/casymda/ tests/
```

integrations tests:

``` l
python3 -m pytest examples
```

(integration-tests require tkinter, which may be installed via `sudo apt-get install python3-tk`)

For Docker-based tests see [docker-compose.yml](docker-compose.yml)

``` l
docker-compose run unit-test
docker-compose run examples-test
docker-compose run examples-test-pypi
```

### Virtual environment setup

``` l
python3 -m venv venv
```

### Editable installation

``` l
pip install -e .
```

### Publish to pypi

``` l
python setup.py sdist

twine upload dist/*
```

pip install twine if necessary,  
remember to set the version in [setup.py](setup.py) and [src/casymda](src/casymda/__init__.py) as required

### PyPy3

Tested PyPy3 (7.3.1-final). Install pypy3 pypy3-dev pypy-tk.

Runtime could be decreased by factor ~2 when using PyPy3 for longer simulations runs (e.g. from ~45s to ~25s for a [simple example model test](examples/basics/model/long_run_bpmn_example_test.py) with MAX_ENTITIES set to 40.000 on an i5 notebook).

## Contact

fladdi.mir@gmx.de

feedback / ideas / discussion / cheering / complaints welcome

MIT License

2020
