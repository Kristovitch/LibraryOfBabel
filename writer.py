import random
import settings


class Writer:
    def __init__(self) -> None:
        self.current_line = [''] * settings.LINE_LENGTH
        self.current_page = [''] * settings.PAGE_LENGTH
        self.current_book = [''] * settings.BOOK_LENGTH

    def get_character(self):
        character_int = random.randint(settings.CHARSET_MIN,
                                       settings.CHARSET_MAX)
        if character_int == settings.CHARSET_SPACE:
            character_int = 0
        character = chr(character_int)
        return character

    def write_line(self):
        for i in range(0, settings.LINE_LENGTH):
            self.current_line[i] = self.get_character()

    def write_page(self):
        for i in range(0, settings.PAGE_LENGTH):
            self.write_line()
            self.current_page[i] = self.current_line

    def write_book(self):
        for i in range(0, settings.BOOK_LENGTH):
            self.write_page()
            self.current_book[i] = self.current_page
