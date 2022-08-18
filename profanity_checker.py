import os
import requests
import os
import dotenv

dotenv.load_dotenv()

api_key = os.getenv('RAPID_API_KEY')
url = "https://neutrinoapi-bad-word-filter.p.rapidapi.com/bad-word-filter"

existing_words: list[str] = []
with open('wordlist.txt', 'r') as f:
    for line in f:
        existing_words.append(line.rstrip())

payload = "content="

for words in existing_words:
    payload += words + ","

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "neutrinoapi-bad-word-filter.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    bad_words = data['bad-words-list']

    new_words = []
    for word in existing_words:
        if word not in new_words:
            if word not in bad_words:
                new_words.append(word)
            else:
                continue
        else:
            continue
    
    new_words = sorted(new_words)

    with open('wordlist.txt', 'w') as f:
        for word in new_words:
            f.write(word + '\n')
elif response.status_code == 429:
    print('Rate limit exceeded. Will skip running profanity filter.')