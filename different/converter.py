from numpy import *
import datetime
from dateutil.parser import parse


class Converter:
    """
    Converts different types of data to other types.
    """

    DATETIME_NOT_PROPERLY_FORMATTED = "Date not properly Formatted. It has to be like '2012-04-22 12:32:11'"
    DATE_NOT_PROPERLY_FORMATTED = "Date not properly Formatted. It has to be like '2012-04-22'"

    @staticmethod
    def lists_to_json(items: list, cols_names_types: list) -> str:
        """
        Maps all data with that titles.
        :param: items: list of list with string items.
        :param: cols_names_types: dict with column names and types
        """
        json_items = []
        for item in items:
            json_item = {}
            for item_feature_value, column in zip(item, cols_names_types):
                json_item[column] = item_feature_value
            json_items.append(json_item)
        return json_items

    @staticmethod
    def json_to_ndarray(dict_object) -> ndarray:
        days_prices = []
        for day_prices in dict_object:
            days_prices.append(list(day_prices.values())[1:])
        return array(days_prices)

    @staticmethod
    def string_to_datetime(datetime_str: str) -> datetime:
        """
        Converts string into datetime.
        """
        try:
            # bez czasu dt = datetime.datetime.strptime(date, '%Y-%m-%d')
            dt = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
        except:
            raise Exception(Converter.DATETIME_NOT_PROPERLY_FORMATTED)
        return dt

    @staticmethod
    def string_to_date(date_str: str) -> datetime:
        """
        Converts string into date.
        """
        try:
            # bez czasu dt = datetime.datetime.strptime(date, '%Y-%m-%d')
            dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
        except:
            raise Exception(Converter.DATE_NOT_PROPERLY_FORMATTED)
        return dt

    @staticmethod
    def string_with_commas_to_float(item: str):
        """
        Converts string with commas to float number.
        :param item: number as a string with commas
        """
        return float(item.replace(',', ''))




