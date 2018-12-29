from third_party.NeoPyStdlib.NData import NJson
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
        self.__date = NDate()

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
        flag = True
        for i in range(len(self.__json_file.metadata)):
            if self.__json_file.metadata[i]["Date"] == self.__date.date_str:
                print("Exist")
                self.__json_file.metadata[i]["Content"] = self.__markdown_metadata
                flag = False
                break
        if flag:
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


def main():
    note_main = NNote()
    note_main.json_filename = "month_12.js"
    note_main.read_from_markdown("test.md")
    note_main.add_to_json()


if __name__ == "__main__":
    main()
