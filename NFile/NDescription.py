import sys
from NDate import NDate
from third_party.NeoPyStdlib.NData import NJson

"""
Example:
[{
"Object": "",
"Date": "",
"Year": 0,
"Month": 0,
"Day": 0,
"Description": "",
"Detail": "",
"Technique": ""
}]
"""


class NDescription:

    def __init__(self):
        self.__date = NDate.NDate()
        self.__json_file = NJson.NJsonPrimitive("Description.js")

    def gen(self, date=None, year=None, month=None, day=None):
        metadata = list()
        obj = dict()
        if date is not None and isinstance(date, str):
            obj.update({
                "Date": date
            })
        if year is not None and isinstance(year, int):
            obj.update({
                "Year": year
            })
        if month is not None and isinstance(month, int):
            obj.update({
                "Month": month
            })
        if day is not None and isinstance(day, int):
            obj.update({
                "Day": day
            })
        obj["Description"] = "Ass we can"
        obj["Detail"] = ""
        obj["Technique"] = ""
        metadata.append(obj)
        self.__json_file.metadata = metadata
        self.__json_file.write_to_file()
