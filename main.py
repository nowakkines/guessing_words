# rich
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.progress import track

# random
from random import choice

# time
from time import sleep

# variables
console = Console()
heart = '♡ '
tries = 5
STOP_GAME = False

word_list = ['year', 'person', 'time', 'business', 'life', 'day', 'hand', 'time', 'work', 'word', 'place', 'face',
            'friend', 'eye', 'question', 'house', 'side', 'country', 'world', 'case', 'head', 'child', 'strength', 'end',
            'kind', 'system', 'part', 'city', 'attitude', 'woman', 'money', 'land', 'car', 'water', 'father',
            'problem', 'hour', 'right', 'leg', 'solution', 'door', 'image', 'history', 'power', 'law', 'war',
            'god', 'voice', 'thousand', 'book', 'opportunity', 'result', 'night', 'table', 'name', 'area', 'article',
            'number', 'company', 'people', 'wife', 'group', 'development', 'process', 'court', 'condition', 'means',
            'beginning', 'light', 'time', 'path', 'soul', 'level', 'form', 'connection', 'minute', 'street', 'evening',
            'quality', 'thought', 'road', 'mother', 'action', 'month', 'state', 'language', 'love', 'look',
            'mom', 'century', 'school', 'goal', 'society', 'activity', 'organization', 'president', 'room',
            'order', 'moment', 'theater', 'letter', 'morning', 'help', 'situation', 'role', 'ruble', 'meaning', 'condition',
            'apartment', 'organ', 'attention', 'body', 'labor', 'son', 'measure', 'death', 'market', 'program', 'task',
            'enterprise', 'window', 'conversation', 'government', 'family', 'production', 'information', 'position',
            'center', 'answer', 'husband', 'author', 'wall', 'interest', 'federation', 'rule', 'management', 'man',
            'idea', 'party', 'council', 'account', 'heart', 'movement', 'thing', 'material', 'week', 'feeling', 'chapter',
            'science', 'row', 'newspaper', 'reason', 'leverage', 'price', 'plan', 'speech', 'point', 'basis', 'comrade',
            'culture', 'data', 'opinion', 'document', 'institute', 'course', 'project', 'meeting', 'director', 'term',
            'finger', 'experience', 'service', 'destiny', 'girl', 'queue', 'forest', 'composition', 'member', 'quantity', 'event',
            'object', 'hall', 'creation', 'value', 'period', 'step', 'brother', 'art', 'structure', 'number',
            'example', 'research', 'citizen', 'game', 'boss', 'growth', 'theme', 'principle', 'method', 'type',
            'film', 'edge', 'guest', 'air', 'character', 'struggle', 'usage', 'size', 'education',
            'boy', 'blood', 'district', 'sky', 'army', 'class', 'representative', 'participation', 'girl', 'politics',
            'hero', 'picture', 'dollar', 'back', 'territory', 'floor', 'field', 'change', 'direction', 'drawing',
            'current', 'church', 'bank', 'stage', 'population', 'majority', 'music', 'truth', 'freedom', 'memory',
            'team', 'union', 'doctor', 'contract', 'tree', 'fact', 'host', 'nature', 'corner', 'phone', 'position',
            'yard', 'writer', 'airplane', 'volume', 'genus', 'sun', 'faith', 'shore', 'performance', 'firm', 'method',
            'factory', 'color', 'magazine', 'manager', 'specialist', 'evaluation', 'region', 'song', 'percentage', 'parent',
            'sea', 'requirement', 'base', 'half', 'novel', 'circle', 'analysis', 'poems', 'car',
            'economics', 'literature', 'paper', 'poet', 'degree', 'master', 'hope', 'subject', 'option',
            'minister', 'border', 'spirit', 'model', 'operation', 'couple', 'dream', 'name', 'mind', 'occasion', 'old man',
            'million', 'success', 'happiness', 'guys', 'office', 'shop', 'space', 'exit', 'blow', 'base',
            'knowledge', 'text', 'protection', 'guidance', 'area', 'consciousness', 'age', 'participant', 'plot',
            'item', 'line', 'desire', 'dad', 'doctor', 'lip', 'daughter', 'wednesday', 'chairman', 'presentation',
            'soldier', 'artist', 'hair', 'weapon', 'match', 'wind', 'guy', 'vision', 'general', 'fire',
            'concept', 'construction', 'ear', 'chest', 'nose', 'fear', 'service', 'content', 'joy',
            'safety', 'product', 'complex', 'business', 'garden', 'employee', 'summer', 'course', 'offer', 'mouth',
            'technology', 'reform', 'absence', 'dog', 'stone', 'future', 'story', 'control', 'river',
            'products', 'sum', 'equipment', 'building', 'sphere', 'necessity', 'fund', 'preparation', 'sheet',
            'republic', 'economy', 'will', 'budget', 'snow', 'village', 'peasant', 'element', 'circumstance',
            'german', 'victory', 'source', 'star', 'choice', 'mass', 'result', 'sister', 'practice', 'holding',
            'pocket', 'glory', 'kitchen', 'definition', 'function', 'army', 'commission', 'application', 'captain',
            'employee', 'provision', 'officer', 'surname', 'limit', 'election', 'scientist', 'bottle', 'battle', 'theory',
            'zone', 'department', 'tooth', 'development', 'personality', 'mountain', 'commodity', 'meter', 'holiday', 'influence',
            'reader', 'pleasure', 'actor', 'tear', 'responsibility', 'teacher', 'act', 'pain', 'set',
            'feature', 'indicator', 'ship', 'sound', 'impression', 'particularity', 'childhood', 'conclusion', 'professor',
            'share', 'norm', 'past', 'commander', 'corridor', 'support', 'frame', 'enemy', 'stage', 'devil', 'grandfather',
            'meeting', 'reception', 'illness', 'cell', 'skin', 'statement', 'attempt', 'comparison', 'calculation', 'deputy',
            'committee', 'sign', 'uncle', 'accounting', 'bread', 'tea', 'regime', 'whole', 'virus', 'expression', 'health',
            'winter', 'ten', 'depth', 'network', 'student', 'second', 'speed', 'search', 'essence', 'tax', 'error',
            'income', 'director', 'surface', 'sensation', 'map', 'club', 'station', 'revolution', 'knee',
            'ministry', 'glass', 'floor', 'height', 'grandmother', 'tube', 'gas', 'master', 'behavior', 'capital',
            'mechanism', 'transmission', 'ability', 'approach', 'energy', 'existence', 'performance', 'cinema',
            'regret', 'deputy', 'resource', 'action', 'birth', 'administration', 'cost', 'smile', 'artist',
            'neighbor', 'phrase', 'figure', 'subject', 'reaction', 'list', 'photograph', 'journalist', 'may', 'violation',
            'meeting', 'crowd', 'hospital', 'creature', 'property', 'duty', 'generation', 'animal', 'scheme',
            'effort', 'difference', 'island', 'opponent', 'wave', 'realization', 'page', 'formation', 'inhabitant',
            'beauty', 'bird', 'plant', 'shadow', 'phenomenon', 'temple', 'smell', 'vodka', 'presence', 'horror', 'clothes',
            'chair', 'patient', 'train', 'university', 'tradition', 'address', 'december', 'palm', 'mixing', 'flower',
            'leader', 'october', 'occupation', 'september', 'room', 'january', 'spectator', 'editorial office', 'style', 'spring',
            'factor', 'august', 'news', 'dependence', 'security', 'equipment', 'concert', 'department', 'expense',
            'exhibition', 'militia', 'transition', 'epoch', 'west', 'work', 'homeland', 'property', 'mystery',
            'grass', 'camp', 'property', 'bed', 'apparatus', 'middle', 'march', 'client', 'lady', 'front',
            'industry', 'chair', 'conversation', 'legislation', 'sale', 'promotion', 'museum', 'trace', 'colonel',
            'doubt', 'understanding', 'april', 'prince', 'fish', 'duma', 'code', 'day', 'miracle', 'neck', 'judge',
            'roof', 'mood', 'stream', 'position', 'crime', 'brain', 'honor', 'post', 'jew', 'June',
            'hundred', 'rain', 'ladder', 'cottage', 'installation', 'appearance', 'receipt', 'sample', 'pipe', 'main',
            'autumn', 'costume', 'woman', 'value', 'duty', 'play', 'table', 'wine', 'memory', 'horse',
            'colleague', 'organism', 'student', 'institution', 'discovery', 'volume', 'trait', 'characteristic', 'performance',
            'defense', 'performance', 'temperature', 'perspective', 'girlfriend', 'order', 'victim', 'restaurant',
            'kilometer', 'dispute', 'taste', 'sign', 'industry', 'american', 'forehead', 'conclusion', 'east',
            'exception', 'key', 'resolution', 'layer', 'side', 'july', 'translation', 'secretary', 'piece', 'hearing',
            'benefit', 'call', 'situation', 'official', 'agreement', 'detail', 'russian', 'silence', 'salary',
            'ticket', 'gift', 'prison', 'box', 'competition', 'book', 'study', 'request', 'tsar', 'audience', 'laughter',
            'message', 'threat', 'trouble', 'block', 'achievement', 'assignment', 'advertisement', 'portrait', 'oil', 'glass',
            'lesson', 'clock', 'scream', 'creativity', 'TV', 'instrument', 'concept', 'lieutenant', 'screen', 'bottom',
            'reality', 'channel', 'meat', 'familiar', 'cheek', 'conflict', 'negotiations', 'recording', 'wagon', 'playground',
            'consequence', 'cooperation', 'mirror', 'tone', 'academy', 'chamber', 'need', 'November',
            'increase', 'fool', 'trip', 'lunch', 'loss', 'february', 'event', 'park', 'acceptance',
            'device', 'substance', 'category', 'season', 'hotel', 'publication', 'association', 'darkness',
            'humanity', 'wheel', 'danger', 'resolution', 'impact', 'collective', 'camera', 'stock',
            'consequence', 'length', 'wing', 'district', 'background', 'candidate', 'relative', 'pressure', 'presence',
            'interaction', 'board', 'partner', 'engine', 'noise', 'dignity', 'sin', 'knife', 'flight', 'passion',
            'trial', 'truth', 'payment', 'difference', 'driver', 'package', 'reduction', 'formula', 'belly', 'capital',
            'bridge', 'news', 'effect', 'entrance', 'governor', 'report', 'shift', 'murder', 'expert', 'bus',
            'dress', 'frame', 'aunt', 'communication', 'psychology', 'lion', 'threshold', 'check', 'procedure', 'worker',
            'repair', 'treatment', 'training', 'waiting', 'monument', 'root', 'observation', 'letter',
            'proof', 'confession', 'bed', 'headquarters', 'owner', 'computer', 'engineer', 'old woman', 'boat',
            'rocket', 'series', 'joke', 'top', 'issue', 'fist', 'ice', 'trade', 'oil', 'youth', 'digit',
            'body', 'lack', 'boot', 'essence', 'talent', 'efficiency', 'coffee', 'strip', 'basic',
            'review', 'collection', 'staff', 'investigator', 'housing', 'bag', 'description', 'bush', 'refusal', 'lock',
            'editor', 'palace', 'care', 'beer', 'sofa', 'table', 'experiment', 'print', 'ring', 'gun',
            'education', 'superiors', 'profession', 'gates', 'kindness', 'friendship', 'peace', 'risk', 'ending', 'smoke',
            'marriage', 'magnitude', 'note', 'initiative', 'conscience', 'activity', 'bone', 'sport', 'credit', 'lord',
            'major', 'conference', 'ceiling', 'library', 'assistant', 'construction', 'rest', 'pen', 'metal',
            'milk', 'prosecutor', 'transport', 'poetry', 'connection', 'paint', 'distance', 'dream', 'village', 'food',
            'evil', 'division', 'plot', 'frontier', 'signal', 'atmosphere', 'cross', 'weight', 'explosion', 'contact',
            'cigarette', 'delight', 'gold', 'soil', 'premium', 'king', 'entrance', 'chance', 'automatic', 'order',
            'boy', 'glasses', 'moment', 'piece', 'reading', 'village', 'witness', 'bet', 'bag', 'surprise',
            'tail', 'sand', 'turn', 'return', 'moment', 'status', 'lake', 'formation', 'parameter', 'fairy tale',
            'trend', 'guilt', 'breath', 'version', 'scale', 'monastery', 'mistress', 'daughter', 'dance',
            'exploitation', 'communist', 'pension', 'buddy', 'explanation', 'set', 'manufacturer', 'dust',
            'philosophy', 'power', 'commitment', 'care', 'throat', 'crisis', 'indication', 'payment', 'apple',
            'drug', 'reality', 'muscovite', 'remainder', 'image', 'transaction', 'essay',
            'buyer', 'tank', 'cost', 'string', 'unit']


def get_word(word_list):
    return choice(word_list).upper()


def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
                 '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tries]


def hello():
    console.print(Panel(
      '''
      The rules are pretty simple : you must enter either a letter or a word..
      [red]You have only 5 attempts[/red]. All letters are uppercase! Using the command [red]info[/red], you can find out : [blue]number of attempts, named letters and words.
      ''', title='Hangman'), justify='center')
    play(tries)


def play(tries):
    result = get_word(word_list)
    word_completion = '_' * len(result)
    word_as_lst = list(word_completion)
    guessed_letters = []
    guessed_word = []
    word_count = word_completion.count('_')

    for _ in track(range(50), description='[green]Processing...'):
        sleep(0.03)
    print(f'[red]The word was generated[/red]: {word_completion} REMAINED {word_count} LETTERS {result}')
    gaming(result, guessed_letters, guessed_word, word_as_lst, word_completion, tries)



def again():
    global STOP_GAME
    question = input('Do you want to continue the game?(+/-) >> ')
    match question:
        case '+':
            play(tries)
        case '-':
            console.print('[blue]Thank you for playing the game.', justify='center')
            STOP_GAME = True
        case _:
            console.print(Panel('You have entered an invalid character.', title='[red]Error'), justify='center')
            again(STOP_GAME)


def gaming(result, guessed_letters, guessed_word, word_as_lst, word_completion, tries):
    while STOP_GAME != True and word_completion != result:
        letter = input('Enter a letter or word >> ').upper()
        indices = [x for x in range(len(result)) if result[x] == letter]

        if letter == 'INFO':
            show_info(guessed_letters, guessed_word)

        elif is_valid(letter, result):

            if tries == 0:
                again()

            elif len(letter) == 1 and letter in guessed_letters:
                print('[red]You have entered the letter that was used.')

            elif len(letter) == 1 and letter not in result:
                console.print('You entered the wrong letter - [red]your attempt is exhausted[/red].')
                tries -= 1

            elif letter == result:
                print('You guessed the word, you\'re a good.')
                again()

            elif len(letter) == len(result) and letter in guessed_word:
                console.print('[red]Have you already entered this word and are you going to use it again?')
                show_info(guessed_letters, guessed_word)
                continue

            elif len(letter) == 1 and letter in result and letter not in guessed_letters:
                guessed_letters.append(letter)
                for index in indices:
                    word_as_lst[index] = letter
                    word_completion = ''.join(word_as_lst)
                print(word_completion)

            elif len(letter) == len(result) and letter != result:
                print('The word entered was incorrect. So you take away your attempt')
                guessed_word.append(letter)
                tries -= 1
        else:
            console.print(Panel('You have entered an invalid character or your length does not match.', title='[red]Error'))
    else:
        if word_completion == result:
            again()


def show_info(guessed_letters, guessed_word):
    info = console.input('''
    What would you like to see? ([blue]'LETTERS'[/blue], [yellow]'WORDS'[/yellow], [red]'ATTEMPTS'[/red], [green]'POSITION')
    >> ''')
    match info:
        case 'LETTERS':
            print('Your used letters: ', end='')
            print(*guessed_letters)
        case 'WORDS':
            print('Your used words: ', end='')
            print(*guessed_word)
        case 'ATTEMPTS':
            print(tries * heart)
        case 'POSITION':
            console.print('↓↓  Your current position ↓↓ ', justify='center')
            print(display_hangman(tries))
        case _:
            console.print(Panel('You have entered an invalid character.', title='[red]Error'))


def is_valid(value, result):
    return value.isalpha() and (len(value) == 1 or len(value) == len(result))


if __name__ == '__main__':
    hello()