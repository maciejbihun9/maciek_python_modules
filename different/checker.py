

class Checker:
    """
    Checks different values and returns True or False.
    """

    @staticmethod
    def is_date(item: str) -> bool:
        """
        Checks if string item is a date
        """
        try:
            float(item)
            return False
        except:
            try:
                parse(item)
                return True
            except ValueError:
                return False

    @staticmethod
    def is_empty_str(item: str) -> bool:
        """
        Checks if an item is a n empty string.
        """
        return not bool(len(item))

    @staticmethod
    def is_number(item: str) -> bool:
        """
        Checks if string value is a number
        """
        try:
            float(item)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_number_with_commas(item) -> bool:
        """
        Checks if string value is float number with commas
        """
        # if contains commas between numbers
        splitted_item = item.split(",")
        first_last_items = [splitted_item[0], splitted_item[-1]]
        try:
            list(map(float, first_last_items))
            return True
        except:
            return False