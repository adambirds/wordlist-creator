import os
import time
import requests
import dotenv

dotenv.load_dotenv()

api_key = os.getenv('WORDNIK_API_KEY')
url = 'https://api.wordnik.com/v4/words.json/randomWords'

while True:
    params = {
        'hasDictionaryDef': 'true',
        'minCorpusCount': '5000',
        'maxCorpusCount': '-1',
        'minDictionaryCount': '5',
        'maxDictionaryCount': '-1',
        'minLength': '4',
        'maxLength': '-1',
        'limit': '500',
        'api_key': api_key
    }

    response = requests.get(url, params=params)
    words = response.json()

    existing_words =[]
    with open('wordlist.txt', 'r') as f:
        for line in f:
            existing_words.append(line.rstrip())

    for word in words:
        actual_word: str = word['word']
        if actual_word not in existing_words:
            if actual_word.isalpha():
                existing_words.append(actual_word.lower())
        else:
            continue

    existing_words = sorted(existing_words)

    with open('wordlist.txt', 'w') as f:
        for word in existing_words:
            f.write(word + '\n')

    time.sleep(18)