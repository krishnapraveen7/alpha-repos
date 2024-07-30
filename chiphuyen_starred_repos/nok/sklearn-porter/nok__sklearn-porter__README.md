# [sklearn-porter](https://github.com/nok/sklearn-porter)


# sklearn-porter

[![Build Status stable branch](https://img.shields.io/travis/nok/sklearn-porter/stable.svg)](https://travis-ci.org/nok/sklearn-porter)
[![codecov](https://codecov.io/gh/nok/sklearn-porter/branch/stable/graph/badge.svg)](https://codecov.io/gh/nok/sklearn-porter)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nok/sklearn-porter/release/1.0.0?filepath=examples/basics/index.pct.ipynb)
[![PyPI](https://img.shields.io/pypi/v/sklearn-porter.svg?color=blue)](https://pypi.python.org/pypi/sklearn-porter)
[![PyPI](https://img.shields.io/pypi/pyversions/sklearn-porter.svg)](https://pypi.python.org/pypi/sklearn-porter)
[![GitHub license](https://img.shields.io/pypi/l/sklearn-porter.svg?color=blue)](https://raw.githubusercontent.com/nok/sklearn-porter/main/LICENSE)

Transpile trained [scikit-learn](https://github.com/scikit-learn/scikit-learn) estimators to C, Java, JavaScript and others.<br>It's recommended for limited embedded systems and critical applications where performance matters most.

Navigation: [Estimators](#estimators) • [Installation](#installation) • [Usage](#usage) • [Known Issues](#known-issues) • [Development](#development) • [Citation](#citation) • [License](#license)


## Estimators

This table gives an overview over all supported combinations of estimators, programming languages and templates.

<table>
  <tr>
    <th rowspan="2"></th>
    <th colspan="18">Programming language</th>
  </tr>
  <tr align="center">
    <th colspan="3">C</th>
    <th colspan="3">Go</th>
    <th colspan="3">Java</th>
    <th colspan="3">JS</th>
    <th colspan="3">PHP</th>
    <th colspan="3">Ruby</th>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html">svm.SVC</a>
    </td>
    <td>✓</td>
    <td></td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html">svm.NuSVC</a>
    </td>
    <td>✓</td>
    <td></td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html">svm.LinearSVC</a>
    </td>
    <td>✓</td>
    <td></td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html">tree.DecisionTreeClassifier</a>
    </td>
    <td>✓ᴾ</td>
    <td></td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html">ensemble.RandomForestClassifier</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html">ensemble.ExtraTreesClassifier</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html">ensemble.AdaBoostClassifier</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html">neighbors.KNeighborsClassifier</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html#sklearn.naive_bayes.BernoulliNB">naive_bayes.BernoulliNB</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html#sklearn.naive_bayes.GaussianNB">naive_bayes.GaussianNB</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html">neural_network.MLPClassifier</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td>✓ᴾ</td>
    <td>✓ᴾ</td>
    <td>×</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr align="center">
    <td align="left">
      <a href="http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html">neural_network.MLPRegressor</a>
    </td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>✓</td>
    <td>✓</td>
    <td>×</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr align="center">
    <td rowspan="2"></td>
    <td>ᴀ</td>
    <td>ᴇ</td>
    <td>ᴄ</td>
    <td>ᴀ</td>
    <td>ᴇ</td>
    <td>ᴄ</td>
    <td>ᴀ</td>
    <td>ᴇ</td>
    <td>ᴄ</td>
    <td>ᴀ</td>
    <td>ᴇ</td>
    <td>ᴄ</td>
    <td>ᴀ</td>
    <td>ᴇ</td>
    <td>ᴄ</td>
    <td>ᴀ</td>
    <td>ᴇ</td>
    <td>ᴄ</td>
  </tr>
  <tr>
    <th colspan="18">Template</th>
  </tr>
</table>

✓ = support of `predict`,　ᴾ = support of `predict_proba`,　× = not supported or feasible<br>
ᴀ = attached model data,　ᴇ = exported model data (JSON),　ᴄ = combined model data


## Installation

<table>
  <tr>
    <th align="left">Purpose</th>
    <th align="left">Version</th>
    <th align="left">Branch</th>
    <th align="left">Build</th>
    <th align="left">Command</th>
  </tr>
  <tr>
    <td>Production</td>
    <td>v0.7.4</td>
    <td><a href="https://github.com/nok/sklearn-porter/tree/stable">stable</a></td>
    <td><a href="https://travis-ci.org/nok/sklearn-porter"><img src="https://img.shields.io/travis/nok/sklearn-porter/stable.svg"></a></td>
    <td><code>pip install sklearn-porter</code></td>
  </tr>
  <tr>
    <td>Development</td>
    <td>v1.0.0</td>
    <td><a href="https://github.com/nok/sklearn-porter/tree/main">main</a></td>
    <td><a href="https://travis-ci.org/nok/sklearn-porter"><img src="https://img.shields.io/travis/nok/sklearn-porter/main.svg"></a></td>
    <td><code>pip install https://github.com/nok/sklearn-porter/zipball/main</code></td>
  </tr>
</table>

In both environments the only prerequisite is `scikit-learn >= 0.17, <= 0.22`.


## Usage

### Binder

Try it out yourself by starting an interactive notebook with Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nok/sklearn-porter/release/1.0.0?filepath=examples/basics/index.pct.ipynb)

### Basics

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from sklearn_porter import port, save, make, test

# 1. Load data and train a dummy classifier:
X, y = load_iris(return_X_y=True)
clf = DecisionTreeClassifier()
clf.fit(X, y)

# 2. Port or transpile an estimator:
output = port(clf, language='js', template='attached')
print(output)

# 3. Save the ported estimator:
src_path, json_path = save(clf, language='js', template='exported', directory='/tmp')
print(src_path, json_path)

# 4. Make predictions with the ported estimator:
y_classes, y_probas = make(clf, X[:10], language='js', template='exported')
print(y_classes, y_probas)

# 5. Test always the ported estimator by making an integrity check:
score = test(clf, X[:10], language='js', template='exported')
print(score)
```

### OOP

```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

from sklearn_porter import Estimator

# 1. Load data and train a dummy classifier:
X, y = load_iris(return_X_y=True)
clf = DecisionTreeClassifier()
clf.fit(X, y)

# 2. Port or transpile an estimator:
est = Estimator(clf, language='js', template='attached')
output = est.port()
print(output)

# 3. Save the ported estimator:
est.template = 'exported'
src_path, json_path = est.save(directory='/tmp')
print(src_path, json_path)

# 4. Make predictions with the ported estimator:
y_classes, y_probas = est.make(X[:10])
print(y_classes, y_probas)

# 5. Test always the ported estimator by making an integrity check:
score = est.test(X[:10])
print(score)
```

### CLI

In addition you can use the sklearn-porter on the command line. The command calls `porter` and is available after the installation.

```
porter {show,port,save} [-h] [-v]

porter show [-l {c,go,java,js,php,ruby}] [-h]

porter port <estimator> [-l {c,go,java,js,php,ruby}]
                        [-t {attached,combined,exported}]
                        [--skip-warnings] [-h]

porter save <estimator> [-l {c,go,java,js,php,ruby}]
                        [-t {attached,combined,exported}]
                        [--directory DIRECTORY]
                        [--skip-warnings] [-h]
```

You can serialize an estimator and save it locally. For more details you can read the instructions to  [model persistence](http://scikit-learn.org/stable/modules/model_persistence.html#persistence-example).

```python
from joblib import dump

dump(clf, 'estimator.joblib', compress=0)
```

After that the estimator can be transpiled by using the subcommand `port`:

```bash
porter port estimator.joblib -l js -t attached > estimator.js
```

For further processing you can pass the result to another applications, e.g. [UglifyJS](https://github.com/mishoo/UglifyJS2).

```bash
porter port estimator.joblib -l js -t attached | uglifyjs --compress -o estimator.min.js
```

## Known Issues

- In some rare cases the regression tests of the support vector machine, [SVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html) and [NuSVC](http://scikit-learn.org/stable/modules/generated/sklearn.svm.NuSVC.html), fail since `scikit-learn>=0.22`. Because of that a `QualityWarning` will be raised which should reminds you to evaluate the result by using the `test` method.


## Development

### Aliases

The following commands are useful time savers in the daily development:

```bash
# Install a Python environment with `conda`:
make setup

# Start a Jupyter notebook with examples:
make notebook

# Start tests on the host or in a separate docker container:
make tests
make tests-docker

# Lint the source code with `pylint`:
make lint

# Generate notebooks with `jupytext`:
make examples

# Deploy a new version with `twine`:
make deploy
```

### Dependencies

The prerequisite is Python 3.6 which you can install with [conda](https://docs.conda.io/en/latest/miniconda.html):

```bash
conda env create -n sklearn-porter_3.6 python=3.6
conda activate sklearn-porter_3.6
```

After that you have to install all required packages:

```bash
pip install --no-cache-dir -e ".[development,examples]"
```

### Environment

All tests run against these combinations of [scikit-learn](https://github.com/scikit-learn/scikit-learn) and Python versions:

<table border="0" width="100%">
  <tr align="center">
    <td colspan="2" rowspan="2"></td>
    <td colspan="4"><strong>Python</strong></td>
  </tr>
  <tr align="center">
    <td><strong>3.5</strong></td>
    <td><strong>3.6</strong></td>
    <td><strong>3.7</strong></td>
    <td><strong>3.8</strong></td>
  </tr>
  <tr align="center">
    <td rowspan="18"><strong>scikit-learn</strong></td>
    <td rowspan="3"><strong>0.17</strong></td>
    <td>cython 0.27.3</td>
    <td>cython 0.27.3</td>
    <td rowspan="3">not supported<br>by scikit-learn</td>
    <td rowspan="3">no support<br>by scikit-learn</td>
  </tr>
  <tr align="center">
    <td>numpy 1.9.3</td>
    <td>numpy 1.9.3</td>
  </tr>
  <tr align="center">
    <td>scipy 0.16.0</td>
    <td>scipy 0.16.0</td>
  </tr>
  <tr align="center">
    <td rowspan="3"><strong>0.18</strong></td>
    <td>cython 0.27.3</td>
    <td>cython 0.27.3</td>
    <td rowspan="3">not supported<br>by scikit-learn</td>
    <td rowspan="3">not supported<br>by scikit-learn</td>
  </tr>
  <tr align="center">
    <td>numpy 1.9.3</td>
    <td>numpy 1.9.3</td>
  </tr>
  <tr align="center">
    <td>scipy 0.16.0</td>
    <td>scipy 0.16.0</td>
  </tr>
  <tr align="center">
    <td rowspan="3"><strong>0.19</strong></td>
    <td>cython 0.27.3</td>
    <td>cython 0.27.3</td>
    <td rowspan="3">not supported<br>by scikit-learn</td>
    <td rowspan="3">not supported<br>by scikit-learn</td>
  </tr>
  <tr align="center">
    <td>numpy 1.14.5</td>
    <td>numpy 1.14.5</td>
  </tr>
  <tr align="center">
    <td>scipy 1.1.0</td>
    <td>scipy 1.1.0</td>
  </tr>
  <tr align="center">
    <td rowspan="3"><strong>0.20</strong></td>
    <td>cython 0.27.3</td>
    <td>cython 0.27.3</td>
    <td>cython 0.27.3</td>
    <td rowspan="3">not supported<br>by joblib</td>
  </tr>
  <tr align="center">
    <td>numpy</td>
    <td>numpy</td>
    <td>numpy</td>
  </tr>
  <tr align="center">
    <td>scipy</td>
    <td>scipy</td>
    <td>scipy</td>
  </tr>
  <tr align="center">
    <td rowspan="3"><strong>0.21</strong></td>
    <td>cython</td>
    <td>cython</td>
    <td>cython</td>
    <td>cython</td>
  </tr>
  <tr align="center">
    <td>numpy</td>
    <td>numpy</td>
    <td>numpy</td>
    <td>numpy</td>
  </tr>
  <tr align="center">
    <td>scipy</td>
    <td>scipy</td>
    <td>scipy</td>
    <td>scipy</td>
  </tr>
  <tr align="center">
    <td rowspan="3"><strong>0.22</strong></td>
    <td>cython</td>
    <td>cython</td>
    <td>cython</td>
    <td>cython</td>
  </tr>
  <tr align="center">
    <td>numpy</td>
    <td>numpy</td>
    <td>numpy</td>
    <td>numpy</td>
  </tr>
  <tr align="center">
    <td>scipy</td>
    <td>scipy</td>
    <td>scipy</td>
    <td>scipy</td>
  </tr>
</table>

For the regression tests we have to use specific compilers and interpreters:

<table>
  <tr>
    <th align="left">Name</th>
    <th align="left">Source</th>
    <th align="left">Version</th>
  </tr>
  <tr>
    <td>GCC</td>
    <td><a href="https://gcc.gnu.org">https://gcc.gnu.org</a></td>
    <td>10.2.1</td>
  </tr>
  <tr>
    <td>Go</td>
    <td><a href="https://golang.org">https://golang.org</a></td>
    <td>1.15.15</td>
  </tr>
  <tr>
    <td>Java (OpenJDK)</td>
    <td><a href="https://openjdk.java.net">https://openjdk.java.net</a></td>
    <td>1.8.0</td>
  </tr>
  <tr>
    <td>Node.js</td>
    <td><a href="https://nodejs.org/en/">https://nodejs.org</a></td>
    <td>12.22.5</td>
  </tr>
  <tr>
    <td>PHP</td>
    <td><a href="https://www.php.net/">https://www.php.net</a></td>
    <td>7.4.28</td>
  </tr>
  <tr>
    <td>Ruby</td>
    <td><a href="https://www.ruby-lang.org/en/">https://www.ruby-lang.org</a></td>
    <td>2.7.4</td>
  </tr>
</table>

Please notice that in general you can use older compilers and interpreters with the generated source code. For instance you can use Java 1.6 to compile and run models.

### Logging

You can activate logging by changing the option `logging.level`.

```python
from sklearn_porter import options

from logging import DEBUG

options['logging.level'] = DEBUG
```

### Testing

You can run the unit and regression tests either on your local machine (host) or in a separate running Docker container.

```bash
pytest tests -v \
  --cov=sklearn_porter \
  --disable-warnings \
  --numprocesses=auto \
  -p no:doctest \
  -o python_files="EstimatorTest.py" \
  -o python_functions="test_*"
```

```bash
docker build \
  -t sklearn-porter \
  --build-arg PYTHON_VER=${PYTHON_VER:-python=3.6} \
  --build-arg SKLEARN_VER=${SKLEARN_VER:-scikit-learn=0.21} \
  .

docker run \
  -v $(pwd):/home/abc/repo \
  --detach \
  --entrypoint=/bin/bash \
  --name test \
  -t sklearn-porter

docker exec -it test ./docker-entrypoint.sh \
  pytest tests -v \
    --cov=sklearn_porter \
    --disable-warnings \
    --numprocesses=auto \
    -p no:doctest \
    -o python_files="EstimatorTest.py" \
    -o python_functions="test_*"

docker rm -f $(docker ps --all --filter name=test -q)
```


## Citation

If you use this implementation in you work, please add a reference/citation to the paper. You can use the following BibTeX entry:

```bibtex
@unpublished{sklearn_porter,
  author = {Darius Morawiec},
  title = {sklearn-porter},
  note = {Transpile trained scikit-learn estimators to C, Java, JavaScript and others},
  url = {https://github.com/nok/sklearn-porter}
}
```


## License

The package is Open Source Software released under the [BSD 3-Clause](LICENSE) license.
