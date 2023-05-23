##################
deprecation-alias
##################

.. start short_desc

**A wrapper around 'deprecation' providing support for deprecated aliases.**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos| |coveralls|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Anaconda
	  - |conda-version| |conda-platform|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/deprecation-alias/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/deprecation-alias/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/deprecation-alias/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/deprecation-alias/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/deprecation-alias/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/deprecation-alias/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/deprecation-alias/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/deprecation-alias/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/deprecation-alias/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/deprecation-alias/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/deprecation-alias/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/deprecation-alias/
	:alt: Requirements Status

.. |coveralls| image:: https://img.shields.io/coveralls/github/domdfcoding/deprecation-alias/master?logo=coveralls
	:target: https://coveralls.io/github/domdfcoding/deprecation-alias?branch=master
	:alt: Coverage

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/deprecation-alias?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/deprecation-alias
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/deprecation-alias
	:target: https://pypi.org/project/deprecation-alias/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/deprecation-alias?logo=python&logoColor=white
	:target: https://pypi.org/project/deprecation-alias/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/deprecation-alias
	:target: https://pypi.org/project/deprecation-alias/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/deprecation-alias
	:target: https://pypi.org/project/deprecation-alias/
	:alt: PyPI - Wheel

.. |conda-version| image:: https://img.shields.io/conda/v/domdfcoding/deprecation-alias?logo=anaconda
	:target: https://anaconda.org/domdfcoding/deprecation-alias
	:alt: Conda - Package Version

.. |conda-platform| image:: https://img.shields.io/conda/pn/domdfcoding/deprecation-alias?label=conda%7Cplatform
	:target: https://anaconda.org/domdfcoding/deprecation-alias
	:alt: Conda - Platform

.. |license| image:: https://img.shields.io/github/license/domdfcoding/deprecation-alias
	:target: https://github.com/domdfcoding/deprecation-alias/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/deprecation-alias
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/deprecation-alias/v0.3.1
	:target: https://github.com/domdfcoding/deprecation-alias/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/deprecation-alias
	:target: https://github.com/domdfcoding/deprecation-alias/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2023
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/deprecation-alias
	:target: https://pypi.org/project/deprecation-alias/
	:alt: PyPI - Downloads

.. end shields

Installation
--------------

.. start installation

``deprecation-alias`` can be installed from PyPI or Anaconda.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install deprecation-alias

To install with ``conda``:

	* First add the required channels

	.. code-block:: bash

		$ conda config --add channels https://conda.anaconda.org/conda-forge
		$ conda config --add channels https://conda.anaconda.org/domdfcoding

	* Then install

	.. code-block:: bash

		$ conda install deprecation-alias

.. end installation
