import random
print("Welcome to the Hangman Game")

lifes = ['''
     _________
    |         |
    |
    |
    |
    |
 ___|___  
 ''', '''
     _________
    |         |
    |         O
    |  
    |
    |       
 ___|___  
 ''', '''
     _________
    |         |
    |         O
    |         |
    |         |
    |
 ___|___  
 ''', '''
     _________
    |         |
    |         O
    |        /|
    |         |
    |
 ___|___  
 ''', '''
     _________
    |         |
    |         O
    |        /|\\
    |         |
    |
 ___|___  
 ''', '''
     _________
    |         |
    |         O
    |        /|\\
    |         |
    |        /
 ___|___  
 ''', '''
     _________
    |         |
    |         O
    |        /|\\
    |         |
    |        / \\
 ___|___  
 ''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


list_of_words = [
    'abruptly',
    'absurd',
    'abyss',
    'affix',
    'askew',
    'avenue',
    'awkward',
    'axiom',
    'azure',
    'bagpipes',
    'bandwagon',
    'banjo',
    'bayou',
    'beekeeper',
    'bikini',
    'blitz',
    'blizzard',
    'boggle',
    'bookworm',
    'boxcar',
    'boxful',
    'buckaroo',
    'buffalo',
    'buffoon',
    'buxom',
    'buzzard',
    'buzzing',
    'buzzwords',
    'caliph',
    'cobweb',
    'cockiness',
    'croquet',
    'crypt',
    'curacao',
    'cycle',
    'daiquiri',
    'dirndl',
    'disavow',
    'dizzying',
    'duplex',
    'dwarves',
    'embezzle',
    'equip',
    'espionage',
    'euouae',
    'exodus',
    'faking',
    'fishhook',
    'fixable',
    'fjord',
    'flapjack',
    'flopping',
    'fluffiness',
    'flyby',
    'foxglove',
    'frazzled',
    'frizzled',
    'fuchsia',
    'funny',
    'gabby',
    'galaxy',
    'galvanize',
    'gazebo',
    'giaour',
    'gizmo',
    'glowworm',
    'glyph',
    'gnarly',
    'gnostic',
    'gossip',
    'grogginess',
    'haiku',
    'haphazard',
    'hyphen',
    'iatrogenic',
    'icebox',
    'injury',
    'ivory',
    'ivy',
    'jackpot',
    'jaundice',
    'jawbreaker',
    'jaywalk',
    'jazziest',
    'jazzy',
    'jelly',
    'jigsaw',
    'jinx',
    'jiujitsu',
    'jockey',
    'jogging',
    'joking',
    'jovial',
    'joyful',
    'juicy',
    'jukebox',
    'jumbo',
    'kayak',
    'kazoo',
    'keyhole',
    'khaki',
    'kilobyte',
    'kiosk',
    'kitsch',
    'kiwifruit',
    'klutz',
    'knapsack',
    'larynx',
    'lengths',
    'lucky',
    'luxury',
    'lymph',
    'marquis',
    'matrix',
    'megahertz',
    'microwave',
    'mnemonic',
    'mystify',
    'naphtha',
    'nightclub',
    'nowadays',
    'numbskull',
    'nymph',
    'onyx',
    'ovary',
    'oxidize',
    'oxygen',
    'pajama',
    'peekaboo',
    'phlegm',
    'pixel',
    'pizazz',
    'pneumonia',
    'polka',
    'pshaw',
    'psyche',
    'puppy',
    'puzzling',
    'quartz',
    'queue',
    'quips',
    'quixotic',
    'quiz',
    'quizzes',
    'quorum',
    'razzmatazz',
    'rhubarb',
    'rhythm',
    'rickshaw',
    'schnapps',
    'scratch',
    'shiv',
    'snazzy',
    'sphinx',
    'spritz',
    'squawk',
    'staff',
    'strength',
    'strengths',
    'stretch',
    'stronghold',
    'stymied',
    'subway',
    'swivel',
    'syndrome',
    'thriftless',
    'thumbscrew',
    'topaz',
    'transcript',
    'transgress',
    'transplant',
    'triphthong',
    'twelfth',
    'twelfths',
    'unknown',
    'unworthy',
    'unzip',
    'uptown',
    'vaporize',
    'vixen',
    'vodka',
    'voodoo',
    'vortex',
    'voyeurism',
    'walkway',
    'waltz',
    'wave',
    'wavy',
    'waxy',
    'wellspring',
    'wheezy',
    'whiskey',
    'whizzing',
    'whomever',
    'wimpy',
    'witchcraft',
    'wizard',
    'woozy',
    'wristwatch',
    'wyvern',
    'xylophone',
    'yachtsman',
    'yippee',
    'yoked',
    'youthful',
    'yummy',
    'zephyr',
    'zigzag',
    'zigzagging',
    'zilch',
    'zipper',
    'zodiac',
    'zombie',
    ]
index_list = (len(list_of_words) - 1)

selected_word = list_of_words[random.randint(0, index_list)]
hangman_word = []
space = '_'

for cont in range(len(selected_word)):
    hangman_word.append(space)

show_hang = "".join(hangman_word)
print(show_hang)

result_word = hangman_word
life_counter = 0
while True:
    print(logo)
    print(lifes[life_counter])
    print(f'You have {6-life_counter} opportunities')
    letter_sel = input("Guess a letter: ").lower()
    if letter_sel not in selected_word:
        print(f"{letter_sel} don't match")
        life_counter += 1

    if life_counter < 6:
        for count in range(0,len(selected_word)):
            if selected_word[count] == letter_sel:
                hangman_word[count] = letter_sel
                print(f'{letter_sel} is correct')
        show = ''.join(hangman_word)
        print(show)

    else:
        print(logo)
        print(lifes[life_counter])
        print(f'Palabra correcta: {selected_word}')
        print("G A M E    O V E R!!!")
        break
    if '_' not in hangman_word:
        print(f'Palabra correcta: {selected_word}')
        print('Y O U    W  I  N  !!!!!')
        break





