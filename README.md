<img src="https://raw.githubusercontent.com/QTC-UMD/rydiqule/main/docs/source/img/Rydiqule_Logo_Transparent_300.png" alt="rydiqule" style="max-width: 100%">

# the _rydiqule_ » vendored-conda-builds

### Conda builds of vendored packages for _rydiqule_

[![Actions Status](https://github.com/QTC-UMD/rydiqule-vendored-conda-builds/workflows/Make%20and%20upload%20Conda%20packages/badge.svg)](https://github.com/QTC-UMD/rydiqule-vendored-conda-builds/actions)
[![License](https://img.shields.io/github/license/QTC-UMD/rydiqule-vendored-conda-builds)](https://github.com/QTC-UMD/rydiqule-vendored-conda-builds/raw/master/LICENSE.txt)
[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/QTC-UMD/rydiqule-vendored-conda-builds)](https://github.com/QTC-UMD/rydiqule-vendored-conda-builds/tags)


This repository is used to create Conda builds of the following packages and upload them to the
[rydiqule Anaconda Cloud repository](https://anaconda.org/rydiqule/repo).

| Package | Latest version | Conda version | Conda Platforms |
| :-- | :-- | :-- | :-- |
| [leveldiagram](https://github.com/dihm/leveldiagram) | [![PyPI](https://img.shields.io/pypi/v/leveldiagram.svg)](https://pypi.org/project/leveldiagram) | [![Conda Version](https://img.shields.io/conda/v/rydiqule/leveldiagram)](https://anaconda.org/rydiqule/leveldiagram) | [![Conda Platforms](https://img.shields.io/conda/pn/rydiqule/leveldiagram)](https://anaconda.org/rydiqule/leveldiagram) |
| [arc](https://github.com/nikolasibalic/ARC-Alkali-Rydberg-Calculator) | [![PyPI](https://img.shields.io/pypi/v/arc-alkali-rydberg-calculator.svg)](https://pypi.org/project/arc-alkali-rydberg-calculator) | [![Conda Version](https://img.shields.io/conda/v/rydiqule/ARC-Alkali-Rydberg-Calculator)](https://anaconda.org/rydiqule/ARC-Alkali-Rydberg-Calculator) | [![Conda Platforms](https://img.shields.io/conda/pn/rydiqule/ARC-Alkali-Rydberg-Calculator)](https://anaconda.org/rydiqule/ARC-Alkali-Rydberg-Calculator) |
| [asteval](https://github.com/lmfit/asteval) | [![PyPI](https://img.shields.io/pypi/v/asteval.svg)](https://pypi.org/project/asteval) | [![Conda Version](https://img.shields.io/conda/v/rydiqule/asteval)](https://anaconda.org/rydiqule/asteval) | [![Conda Platforms](https://img.shields.io/conda/pn/rydiqule/asteval)](https://anaconda.org/rydiqule/asteval) |
| [lmfit](https://github.com/lmfit/lmfit-py) | [![PyPI](https://img.shields.io/pypi/v/lmfit.svg)](https://pypi.org/project/lmfit) | [![Conda Version](https://img.shields.io/conda/v/rydiqule/lmfit)](https://anaconda.org/rydiqule/lmfit) | [![Conda Platforms](https://img.shields.io/conda/pn/rydiqule/lmfit)](https://anaconda.org/rydiqule/lmfit) |
| [uncertainties](https://github.com/lebigot/uncertainties) | [![PyPI](https://img.shields.io/pypi/v/uncertainties.svg)](https://pypi.org/project/uncertainties) | [![Conda Version](https://img.shields.io/conda/v/rydiqule/uncertainties)](https://anaconda.org/rydiqule/uncertainties) | [![Conda Platforms](https://img.shields.io/conda/pn/rydiqule/uncertainties)](https://anaconda.org/rydiqule/uncertainties) |
| [cyrk](https://github.com/jrenaud90/CyRK) | [![PyPI](https://img.shields.io/pypi/v/cyrk.svg)](https://pypi.org/project/cyrk) | [![Conda Version](https://img.shields.io/conda/v/rydiqule/cyrk)](https://anaconda.org/rydiqule/cyrk) | [![Conda Platforms](https://img.shields.io/conda/pn/rydiqule/cyrk)](https://anaconda.org/rydiqule/cyrk) |
| [numbakit-ode](https://github.com/hgrecco/numbakit-ode) | [![PyPI](https://img.shields.io/pypi/v/numbakit-ode.svg)](https://pypi.org/project/numbakit-ode) | [![Conda Version](https://img.shields.io/conda/v/rydiqule/numbakit-ode)](https://anaconda.org/rydiqule/numbakit-ode) | [![Conda Platforms](https://img.shields.io/conda/pn/rydiqule/numbakit-ode)](https://anaconda.org/rydiqule/numbakit-ode) |


These packages are not in the [default Anaconda repository](https://docs.anaconda.com/anaconda/user-guide/tasks/using-repositories/), and are made available to _rydiqule_ users with a conda installation via our [Anaconda cloud repository](https://anaconda.org/rydiqule/repo). To reduce the need for users to use the [conda-forge respository](https://anaconda.org/conda-forge/repo), we may also build and publish packages in our Anaconda respository even if they are available on conda-forge.

Please file an [issue](https://github.com/rydiqule/rydiqule-vendored-conda-builds/issues) if you notice a package is out of date or any other issues with the conda packages produced by this repository.


## Methodology

Whenever a new commit is pushed to this repository, the GitHub Action [`.github/workflows/make_packages.yml`](.github/workflows/make_packages.yml) runs the script [`make_packages.py`](make_packages.py), which executes the build of packages listed in [`pkgs.toml`](pkgs.toml). If the packages build sucessfully and the commit is tagged, the GitHub Action uploads them to the labscript-suite Anaconda Cloud repository. Additionally, the build and upload action is automatically run once per week on the latest tagged commit.
