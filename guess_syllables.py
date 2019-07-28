from pygame import mixer # Load the required library
from os import system
import random
import glob

NUMBER_OF_SYLLABLES = 15

class word:
    def __init__(self, path):
        self.path = path
        self.word = path[path.rfind("\\")+1:-4].lower()
        self.wrong_ans = 0
        self.wrong_ans_words = []
    
    def play(self, ):
        mixer.init()
        mixer.music.load(self.path)
        mixer.music.play()

def print_statictics():
    global remain_words, right_ans, wrong_ans, right_ans_1_try
    system("cls")
    if right_ans != 0:
        if wrong_ans == 0:
            percents = 100
        else:
            percents = int(100*(right_ans - wrong_ans) / (right_ans + wrong_ans))
    else:
        percents = 0
    print("Right:", right_ans, "Wrong:", wrong_ans,
          "Percents:", percents, "Correct:", right_ans_1_try,
          "\tRemain:", remain_words)
    print()
system("cls")
paths = glob.glob('.\syllables\*')
words = [word(path) for path in paths]
words_rnd = []
print("Guess next syllables:")
for i in range(NUMBER_OF_SYLLABLES):
    words_rnd.append(words[random.randint(0, len(words) - 1)])
    print(words_rnd[-1].word)
words = words_rnd
print("write just letters without tones")
print("press Enter to start...")
input()


remain_words = len(words)
right_ans = 0
wrong_ans = 0
right_ans_1_try = 0
done_words = []

inp = ""
go_next = True
while (inp != "!exit") and (remain_words > 0):
    print_statictics()
    if go_next:
        word_num = random.randint(0,remain_words-1)
        curr_word = words[word_num]
    curr_word.play()
    inp = input()    
    curr_word.play()
    if inp == curr_word.word:
        right_ans += 1
        print("Correct!")
        if go_next == True:
            right_ans_1_try += 1
            done_words.append(words.pop(word_num))
            remain_words -= 1
        else:
            go_next = True
    elif inp == "":#!repeat":
        go_next = False
        continue
    elif (inp == "!next") or (inp == "!stop"):
        go_next = True
    else:
        wrong_ans += 1
        curr_word.wrong_ans += 1
        curr_word.wrong_ans_words.append(inp)
        print("You are wrong! Correct is: " + curr_word.word)
        go_next = False        
    input()

done_words.sort(key=lambda word : word.wrong_ans)
with open ("game_statistics.txt", "w") as f:
    for word in words:
        f.write(word.word + "\t" + str(word.wrong_ans) + "\t" + str(word.wrong_ans_words) + "\n")

