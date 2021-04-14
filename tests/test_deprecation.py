# stdlib
import datetime

# 3rd party
import pytest
from deprecation import UnsupportedWarning  # type: ignore

# this package
from deprecation_alias import deprecated


def test_deprecation():

	def func(*args, **kwargs):
		"""
		A normal function.
		"""

		return args, kwargs

	@deprecated(deprecated_in='1', removed_in='3', current_version='2', details="use 'bar' instead.")
	def deprecated_func(*args, **kwargs):
		"""
		A deprecated function.
		"""

		return args, kwargs

	deprecated_alias = deprecated(
		deprecated_in='1',
		removed_in='3',
		current_version='2',
		details="use 'bar' instead.",
		name="deprecated_alias",
		)(func)  # yapf: disable

	with pytest.warns(DeprecationWarning) as record:
		assert deprecated_func(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})
		assert deprecated_alias(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})

	assert len(record) == 2
	assert record[0].message.args == (  # type: ignore
			"deprecated_func", '1', '3', "use 'bar' instead."
			)
	assert record[1].message.args == (  # type: ignore
			"deprecated_alias", '1', '3', "use 'bar' instead."
			)

	assert ".. deprecated::" in deprecated_func.__doc__
	assert ".. deprecated::" in deprecated_alias.__doc__
	assert ".. deprecated::" not in func.__doc__  # type: ignore


def test_unsupported():

	def func(*args, **kwargs):
		"""
		A normal function.
		"""

		return args, kwargs

	@deprecated(deprecated_in='1', removed_in='3', current_version='5', details="use 'bar' instead.")
	def deprecated_func(*args, **kwargs):
		"""
		A deprecated function.
		"""

		return args, kwargs

	deprecated_alias = deprecated(
		deprecated_in='1',
		removed_in='3',
		current_version='5',
		details="use 'bar' instead.",
		name="deprecated_alias",
		)(func)  # yapf: disable

	with pytest.warns(UnsupportedWarning) as record:
		assert deprecated_func(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})
		assert deprecated_alias(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})

	assert len(record) == 2
	assert record[0].message.args == (  # type: ignore
			"deprecated_func", '1', '3', "use 'bar' instead."
			)
	assert record[1].message.args == (  # type: ignore
			"deprecated_alias", '1', '3', "use 'bar' instead."
			)

	assert ".. deprecated::" in deprecated_func.__doc__
	assert ".. deprecated::" in deprecated_alias.__doc__
	assert ".. deprecated::" not in func.__doc__  # type: ignore


def test_deprecation_dates(fixed_datetime: datetime.datetime):

	def func(*args, **kwargs):
		"""
		A normal function.
		"""

		return args, kwargs

	@deprecated(
			deprecated_in='1',
			removed_in=datetime.date(2021, 1, 1),
			details="use 'bar' instead.",
			)
	def deprecated_func(*args, **kwargs):
		"""
		A deprecated function.
		"""

		return args, kwargs

	deprecated_alias = deprecated(
		deprecated_in='1',
		removed_in=datetime.date(2021, 1, 1),
		details="use 'bar' instead.",
		name="deprecated_alias",
		)(func)  # yapf: disable

	with pytest.warns(DeprecationWarning) as record:
		assert deprecated_func(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})
		assert deprecated_alias(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})

	assert len(record) == 2
	assert record[0].message.args == (  # type: ignore
		"deprecated_func", '1', datetime.date(2021, 1, 1), "use 'bar' instead."
		)
	assert record[1].message.args == (  # type: ignore
		"deprecated_alias", '1', datetime.date(2021, 1, 1), "use 'bar' instead."
		)

	assert ".. deprecated::" in deprecated_func.__doc__
	assert ".. deprecated::" in deprecated_alias.__doc__
	assert ".. deprecated::" not in func.__doc__  # type: ignore


def test_deprecation_as_function():

	def func(*args, **kwargs):
		"""
		A normal function.
		"""

		return args, kwargs

	deprecated_func = deprecated(
			deprecated_in='1',
			removed_in='3',
			current_version='2',
			details="use 'bar' instead.",
			func=func,
			)
	deprecated_alias = deprecated(
			deprecated_in='1',
			removed_in='3',
			current_version='2',
			details="use 'bar' instead.",
			func=func,
			name="deprecated_alias",
			)

	with pytest.warns(DeprecationWarning) as record:
		assert deprecated_func(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})
		assert deprecated_alias(1, a_list=['a', 'b']) == ((1, ), {"a_list": ['a', 'b']})

	assert len(record) == 2
	assert record[0].message.args == (  # type: ignore
			"func", '1', '3', "use 'bar' instead."
			)
	assert record[1].message.args == (  # type: ignore
			"deprecated_alias", '1', '3', "use 'bar' instead."
			)

	assert deprecated_func.__doc__ is not None
	assert ".. deprecated::" in deprecated_func.__doc__

	assert deprecated_alias.__doc__ is not None
	assert ".. deprecated::" in deprecated_alias.__doc__

	assert ".. deprecated::" not in func.__doc__  # type: ignore


def test_bad_args():
	with pytest.raises(TypeError, match="Cannot set removed_in to a value without also setting deprecated_in"):
		deprecated(removed_in="1.2.3")
