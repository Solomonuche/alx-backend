#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple, Dict
import math


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        constructor class
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        pagination method
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        start, end = index_range(page, page_size)

        try:
            self.dataset()
            self.__dataset[start]
            self.__dataset[end]
        except Exception:
            return []

        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        return hypermedia
        """

        prev_page = page - 1
        next_page = page + 1
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)

        obj = {
                "page_size": len(data),
                "page": page,
                "data": data,
                "next_page": next_page if end < len(self.__dataset) else None,
                "prev_page": prev_page if start > 0 else None,
                "total_page": math.ceil(len(self.__dataset) / page_size)
                }
        return obj
