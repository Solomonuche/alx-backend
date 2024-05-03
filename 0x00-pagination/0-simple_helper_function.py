#!/usr/bin/env python3
"""
Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    start index and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """

    start_index = 0
    end_index = 0

    if page == 1:
        return (start_index, page_size)
    else:
        end_index = page * page_size
        start_index = end_index - page_size
        return (start_index, end_index)
