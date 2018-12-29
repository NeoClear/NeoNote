from third_party.NeoPyStdlib.NData import NJson


class NNote(object):

    def __init__(self):
        self.__markdown_filename = None
        self.__markdown_metadata = None

    @property
    def markdown_filename(self):
        return self.__markdown_filename

    @markdown_filename.setter
    def markdown_filename(self, filename):
        if isinstance(filename, str):
            self.__markdown_filename = filename
        else:
            print("type of filename is not string")

    def read_from_markdown(self):
        with open(self.__markdown_filename, "r") as fn:
            self.__markdown_metadata = fn.read()
        print(self.__markdown_metadata)

    def read_from_markdown(self, filename):
        if isinstance(filename, str):
            self.__markdown_filename = filename
        else:
            print("type of filename is not string")

        with open(self.__markdown_filename, "r") as fn:
            self.__markdown_metadata = fn.read()
        print(self.__markdown_metadata)


def main():
    ins = NNote()
    ins.read_from_markdown("test.md")


if __name__ == "__main__":
    main()
