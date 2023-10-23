#!/usr/bin/env python3
"""
Module has a function index_range
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and an end index corresponding to the range
    of indices to return a list for the particular pagination parameters

    Args:
        page (int): current page
        page_size (int): items in a page
    Return:
        (tuple): start and end index for the page
    """
    nextPageStart = page * page_size

    return nextPageStart - page_size, nextPageStart
