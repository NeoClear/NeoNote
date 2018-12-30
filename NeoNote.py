from NFile import NNote
from NFile import NDescription

def main():
    note_main = NNote.NNote()
    note_main.json_filename = "month_12.js"
    note_main.read_from_markdown("test.md")
    note_main.add_to_json()
    note_main.print_content("2018-12-30")
    note_main.write_to_markdown(filename="miao.md", date="2018-12-30")
    nd = NDescription.NDescription()
    nd.gen(date="2018-12-30", year=2018, month=12, day=30)


if __name__ == "__main__":
    main()
