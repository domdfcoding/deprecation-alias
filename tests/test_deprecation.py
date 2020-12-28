# 3rd party
import pytest

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
