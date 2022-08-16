import os
import time
import requests
import dotenv

dotenv.load_dotenv()

api_key = os.getenv('WORDNIK_API_KEY')
url = 'https://api.wordnik.com/v4/words.json/randomWords'

total_count = 0

for i in range(1, 13):
    for j in range(1, 5 + 1):
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
        if response.status_code == 200:
            words = response.json()

            existing_words = []
            with open('wordlist.txt', 'r') as f:
                for line in f:
                    existing_words.append(line.rstrip())
            
            count = 0
            for word in words:
                actual_word: str = word['word']
                if actual_word.isalpha():
                    if actual_word.lower() not in existing_words:
                            count += 1
                            existing_words.append(actual_word.lower())
                    else:
                        continue

            existing_words = sorted(existing_words)

            with open('wordlist.txt', 'w') as f:
                for word in existing_words:
                    f.write(word + '\n')

            print(f'Run {i}.{j}: {count} words added to wordlist.txt.')
            total_count += count
        elif response.status_code == 429:
            print('Run {i}.{j}: Rate limit exceeded. Waiting...')
            time.sleep(30)
        
    time.sleep(30)

print(f'{total_count} words added to wordlist.txt during runtime.')