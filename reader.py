import enchant
import settings


class Reader:
    def __init__(self) -> None:
        self.dictionary = enchant.Dict('en_US')
        self.score = 0
        self.highscore = 0

    def check_book(self, book):
        current_string = ''
        current_character = ''
        for i in range(0, settings.BOOK_LENGTH):
            for j in range(0, settings.PAGE_LENGTH):
                for k in range(0, settings.LINE_LENGTH):
                    current_character = book[i][j][k]
                    if current_character != ' ':
                        current_string += str(current_character)
                    else:
                        print(current_string)
                        if self.dictionary.check(current_string):
                            self.score += 1
                            if self.score > self.highscore:
                                self.highscore = self.score
                        else:
                            self.score = 0
