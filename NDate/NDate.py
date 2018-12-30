import datetime


class NDate(object):
    """
    The mini class for NNote
    """
    def __init__(self):
        """
        init different variables, especially date string
        """
        self.__date_str = datetime.datetime.now().date().isoformat()
        self.__year_int = datetime.datetime.now().year
        self.__month_int = datetime.datetime.now().month
        self.__day_int = datetime.datetime.now().day

    def refresh(self):
        """
        Refresh variables
        :return:
        """
        self.__date_str = datetime.datetime.now().date().isoformat()
        self.__year_int = datetime.datetime.now().year
        self.__month_int = datetime.datetime.now().month
        self.__day_int = datetime.datetime.now().day

    @property
    def date_str(self):
        """
        :return: String of date
        """
        return self.__date_str

    @property
    def year_int(self):
        """
        :return: Integer of year
        """
        return self.__year_int

    @property
    def month_int(self):
        """
        :return: Integer of month
        """
        return self.__month_int

    @property
    def day_int(self):
        """
        :return: Integer of day
        """
        return self.__day_int
