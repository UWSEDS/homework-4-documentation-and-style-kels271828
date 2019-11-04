"""
CSE 583: Homework 4 - Documentation and Style

Creates a DataFrame from a url and runs the following tests:
    Column names match those in list COL_NAMES.
    All values in each column have the same type.
    DataFrame has at least 10 rows.
    Column types match those in dictionary COL_TYPES.
    DataFrame does not contain any nan values.
    DataFrame has at least 1 row.

Add your url, desired column names, and desired column types in the
global variables below to test your DataFrame.
"""

import pandas as pd

# Create a DataFrame from user-specified URL, a list containing desired
# column names, and a dictionary containing desired column types.
URL = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
DATA_FRAME = pd.read_csv(URL)
COL_NAMES = DATA_FRAME.columns
COL_TYPES = DATA_FRAME.dtypes


def test_create_dataframe():
    """
    Test that replicates what was done in Item 2 for Homework 2.

    Raises a ValueError if:
        The DataFrame columns do not match those in list COL_NAMES.
        A column in the DataFrame contains values of different types.
        The DataFrame does not have at least 10 rows.
    """
    # Check columns
    if set(DATA_FRAME.columns) != set(COL_NAMES):
        raise ValueError('DataFrame columns do not match input.')

    # Check types
    for col in DATA_FRAME.columns:
        type_set = set([type(entry) for entry in DATA_FRAME[col].to_list()])
        if len(type_set) > 1:
            raise ValueError('Column values do not have same type.')

    # Check length
    if len(DATA_FRAME) < 10:
        raise ValueError('DataFrame does not have at least 10 rows.')


def test_column_type():
    """
    Check that all columns have values of the correct type.

    Raises a ValueError if DataFrame column types do not match those in
    dictionary COL_TYPES.
    """
    for col in DATA_FRAME.columns:
        if DATA_FRAME[col].dtype != COL_TYPES[col]:
            raise ValueError('Column values do not have correct type.')


def test_nan_values():
    """
    Check for nan values.

    Raises a ValueError if the DataFrame contains any nan values.
    """
    if DATA_FRAME.isnull().values.any():
        raise ValueError('DataFrame contains nan values.')


def test_one_row():
    """
    Verify that the DataFrame has at least one row.

    Raises a ValueError if the DataFrame has less than one row.
    """
    if len(DATA_FRAME) < 1:
        raise ValueError('DataFrame does not have at least one row.')
