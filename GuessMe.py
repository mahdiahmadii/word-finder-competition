from tkinter.filedialog import askopenfile
import functions
import os
#mahdiahmadi
#mahdi2002ahmadi82@gmail.com
#https://github.com/mahdiahmadii
def print_board(board):
    """

    Display the contents of board.
    """

    for row_idx in range(len(board)):
        print("         " +functions.make_str_from_row(board, row_idx))


def get_players_list():
    

    players = []
    player = input('Enter player 1 name: ')
    while player.strip() or not players:
        player = player.strip()

        if player in players:
            print("A player by that name is already playing.")

        if player:
            players.append([player, 0])

        if players:
            print('Leave a blank player name to begin playing.')
        player = input('Enter player {num} name: '.format(num=len(players) + 1))
    os.system('cls')
    return players


def play_game(players, board, words):
    """

    Play the game with players, board and words.
    """
    num_remaining = functions.num_words_on_board(board, words) - len(found_words)
    player_num = 0
    while num_remaining > 0:
        print_headers(players, board, found_words, num_remaining)

        guess = input("[{player}] Enter a word (or blank to pass): ".format(
            player=players[player_num % len(players)][0]))

        guess = guess.strip().upper()
        if functions.is_valid_word(words, guess) and functions.board_contains_word(board, guess) and \
            not guess in found_words:
            functions.update_score(players[player_num % len(players)], guess)
            found_words.append(guess)

        num_remaining = functions.num_words_on_board(board, words) - len(found_words)
        player_num += 1
        os.system('cls')

    print("\u001b[31m"+"Game over!\n"+"\u001b[37m")


def print_headers(players, board, found_words, num_remaining):
    """

    Play the score, board, and some other details.
    """

    print_score(players)
    print("\n")
    print_board(board)
    print("\n")
    print('Words remaining: {num} words left.'.format(num=num_remaining))
    print("\n")
    print('Words found: ' + (' '.join(found_words) or 'No words found, yet.'))


def print_score(players):
    """

    Print the scores for each of the players.
    """
    for name, score in players:
        print('  ' + name+"\t"+": "+"\u001b[36m"+ str(score).rjust(3)+"\u001b[37m"  )


# Load the words list.
words_file = askopenfile(mode='r', title='Select word list file')
words = functions.read_words(words_file)
words_file.close()

# Load the board.
board_file = askopenfile(mode='r', title='Select board file')
board = functions.read_board(board_file)
board_file.close()

found_words = []

players = get_players_list()
os.system('cls')

play_game(players, board, words)
print_score(players)