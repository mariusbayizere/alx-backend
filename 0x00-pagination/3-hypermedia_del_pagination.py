#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a page of the dataset with deletion-resilience."""
        # Ensure the index is valid
        assert isinstance(index, int) and \
               0 <= index < len(self.__indexed_dataset)

        # Prepare the data for the page
        data = []
        current_index = index
        for _ in range(page_size):
            while (current_index not in self.__indexed_dataset and
                   current_index < len(self.__dataset)):
                current_index += 1
            if current_index < len(self.__indexed_dataset):
                data.append(self.__indexed_dataset[current_index])
                current_index += 1

        next_index = current_index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
