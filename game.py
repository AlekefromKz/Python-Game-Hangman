import random
from typing import Iterable, List

from hangman.game_status import GameStatus
from hangman.invalid_operation_exception import InvalidOperationError


class Game:

    def __init__(self, allowed_misses: int = 6):
        if not 5 <= allowed_misses <= 8:
            raise ValueError("Number of allowed misses should be between 5 and 8")

        self.__allowed_misses = allowed_misses
        self.__tries_counter = 0
        self.__tried_letters = []
        self.__open_indexes = []
        self.__game_status = GameStatus.NOT_STARTED
        self.__word = ''

    def generate_word(self) -> str:
        filename = './data/words.txt'
        words: List[str] = []
        with open(filename, encoding='utf8') as file:
            for line in file:
                words.append(line.strip('\n'))

        index = random.randint(0, len(words) - 1)
        self.__word = words[index]
        self.__open_indexes = [False for _ in self.__word]
        self.__game_status = GameStatus.IN_PROGRESS

        return self.__word

    def guess_letter(self, letter: str) -> str:
        if self.tries_counter == self.allowed_misses:
            raise InvalidOperationError(f'Exceeded the maximum number of misses. Allowed: {self.allowed_misses}')

        elif self.game_status != GameStatus.IN_PROGRESS:
            raise InvalidOperationError(f'Inappropriate game status. Current: {self.game_status}')

        open_any = False
        result = []

        for i, symbol in enumerate(self.word):
            if symbol == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(symbol)
            else:
                result.append('-')

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        if self.__won():
            self.__game_status = GameStatus.WON
        elif self.allowed_misses == self.tries_counter:
            self.__game_status = GameStatus.LOST

        return ''.join(result)

    def __won(self):
        for each in self.__open_indexes:
            if not each:
                return False
        return True

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self) -> str:
        return self.__word

    @property
    def allowed_misses(self) -> int:
        return self.__allowed_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def tried_letters(self) -> Iterable[str]:
        return sorted(self.__tried_letters)

    @property
    def remaining_tries(self) -> int:
        return self.allowed_misses - self.tries_counter
