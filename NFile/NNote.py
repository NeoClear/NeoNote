from third_party.NeoPyStdlib.NData import NJson
from NDate import NDate


class NNote(object):
    """
    Major class for NNote command line tool
    """
    def __init__(self):
        """
        Init metadata and filename of markdown target
        Init json file target using NJsonPrimitive
        Init date info using NDate
        """
        self.__markdown_filename = None
        self.__markdown_metadata = None
        self.__json_file = NJson.NJsonPrimitive("month_12.js")
        self.__date = NDate.NDate()

    @property
    def markdown_filename(self):
        """
        :return: Filename of markdown
        """
        return self.__markdown_filename

    @markdown_filename.setter
    def markdown_filename(self, filename):
        """
        :param filename: Set filename of markdown target
        """
        if isinstance(filename, str):
            self.__markdown_filename = filename
        else:
            print("type of filename is not string")

    def read_from_markdown(self):
        """
        Read data from markdown file and store it
        """
        with open(self.__markdown_filename, "r") as fn:
            self.__markdown_metadata = fn.read()

    def read_from_markdown(self, filename):
        """
        :param filename: Set filename of markdown target
        Directly read data from markdown file and store it
        """
        if isinstance(filename, str):
            self.__markdown_filename = filename
        else:
            print("type of filename is not string")

        with open(self.__markdown_filename, "r") as fn:
            self.__markdown_metadata = fn.read()

    def add_to_json(self):
        """
        Write markdown metadata to json file
        Change content if you had already written before
        Add today's note if you hadn't written it
        """
        self.__json_file.read_from_file()
        for i in range(len(self.__json_file.metadata)):
            if self.__json_file.metadata[i]["Date"] == self.__date.date_str:
                print("Exist")
                self.__json_file.metadata[i]["Content"] = self.__markdown_metadata
                self.__json_file.write_to_file()
                return
        print("Haven't been created")
        note_today = dict()
        note_today.update({
            "Date": self.__date.date_str,
            "Year": self.__date.year_int,
            "Month": self.__date.month_int,
            "Day": self.__date.day_int
        })
        note_today["Content"] = self.__markdown_metadata
        self.__json_file.metadata.append(note_today)
        self.__json_file.write_to_file()
        return

    def print_content(self, date=None, year=None, month=None, day=None):
        self.__json_file.read_from_file()
        if date is not None and isinstance(date, str):
            for cloth in self.__json_file.metadata:
                if cloth["Date"] == date:
                    print(cloth["Content"])
        if date is None and isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
            for cloth in self.__json_file.metadata:
                if cloth["Year"] == year and cloth["Month"] == month and cloth["Day"] == day:
                    print(cloth["Content"])

    def write_to_markdown(self, filename=None, date=None, year=None, month=None, day=None):
        self.__json_file.read_from_file()
        content = None
        if date is not None and isinstance(date, str):
            for cloth in self.__json_file.metadata:
                if cloth["Date"] == date:
                    content = cloth["Content"]
        if date is None and isinstance(year, int) and isinstance(month, int) and isinstance(day, int):
            for cloth in self.__json_file.metadata:
                if cloth["Year"] == year and cloth["Month"] == month and cloth["Day"] == day:
                    content = cloth["Content"]
        if filename is not None:
            with open(filename, "w") as fm:
                fm.write(content)
        else:
            with open(date, "W") as fm:
                fm.write(content)

    @property
    def json_filename(self):
        """
        Do nothing
        Because Python forces me to do that
        """
        return

    @json_filename.setter
    def json_filename(self, filename):
        """
        :param filename: Filename of json file
        Set json filename, set twice because NJsonPrimitive do not support once.
        NJsonPrimitive really need to improve
        """
        self.__json_file.filename_read = filename
        self.__json_file.filename_write = filename
