from hangman.game import Game
from hangman.game_status import GameStatus

game = Game()
word = game.generate_word()
letters_number = len(word)

print(word)
print(f'The word consists of {letters_number} letters.')
print('Try to guess the secret word letter by letter \n')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Pick a letter \n')
    state = game.guess_letter(letter)

    print(state)
    print(f'Remaining tries: {game.remaining_tries}')
    print(f'Tried letters: {sorted("".join(game.tried_letters))}\n')

if game.game_status == GameStatus.LOST:
    print('You are hanged')
    print(f'The word was "{word}"')
else:
    print('Congratulations! You won!')
