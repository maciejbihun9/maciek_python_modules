import collections
import numpy as np

class ListManager:
    """
    Manages different actions that user can do with lists.
    """

    @staticmethod
    def split_list_of_dicts_by(dicts_list: list, attr_name: str) -> collections.defaultdict:
        """
        Splits the data into different sized chunks
        :param dict_list: list of dicts
        :param attr_name: dict attribute name
        :return: splitted dict by attribute name
        """
        result = collections.defaultdict(list)
        for d in dicts_list:
            result[d[attr_name]].append(d)
        return result

    @staticmethod
    def item_occurrences(data: ndarray) -> dict:
        """
        Find item occurances in list.
        :param data: ndarray of data to count
        :return: dict with number of occurances of each data item.
        """
        u, counts = unique(data, return_counts=True)
        return dict(zip(u, counts))