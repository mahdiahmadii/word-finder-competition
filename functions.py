


def is_valid_word(wordlist, word):
    
    ans = False
    for sampleWord in wordlist:
        if sampleWord == word:
            ans = True
    return ans

def make_str_from_row(board, row_index):
    
    ans = ""
    for letter in board[row_index]:
        ans = ans + letter
    return ans
        


def make_str_from_column(board, column_index):
    
    ans = ""
    for row in board :
        ans = ans+row[column_index]
    return ans


def board_contains_word_in_row(board, word):


    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    for row_index in range(len(board[0])):
        if word in make_str_from_column(board, row_index):
            return True
    return False


def board_contains_word(board, word):
    ans = False
    if(board_contains_word_in_column(board, word)) or board_contains_word_in_row(board, word):
        ans = True
    return ans


def word_score(word):
    points = 0
    if(6>=len(word)>=3):
        point = len(word)*1
    elif(7<=len(word)<=9):
        point = len(word)*2
    elif(len(word)>=10):
        point = len(word)*3
    else:
        point = 0
    return point


def update_score(player_info, word):

    point = word_score(word)
    player_info[1]=player_info[1]+point

    


def num_words_on_board(board, words):
    counter = 0
    for word in words :
        if board_contains_word(board, word):
            counter=counter+1
    
    return counter


def read_words(words_file):
    file = words_file
    text= []
    for line in file:
        text.append(line.rstrip('\n'))
    return text


def read_board(board_file):
    file = board_file
    text1 =[]
    for line in file:
        text2 = []
        for i in range(0,len(line)):
            text2.append(line[i])
        text2.remove('\n')
        text1.append(text2)
    return text1

            
        
