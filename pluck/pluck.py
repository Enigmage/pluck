import json
import requests 
from bs4 import BeautifulSoup as beSo
from colorama import Fore,Style

def scrape(option, word):
    if( option == "-s"):
        loadPage = requests.get(f"https://www.thesaurus.com/browse/{word}")
        src = loadPage.content
        soup = beSo(src, 'html.parser')
        myText = soup.find_all("a", {"class":"css-1s3v085 eh475bn1"}) 
        print(f"{Fore.CYAN}{Style.BRIGHT}Synonyms of {word}:")
        for num, txt in enumerate(myText, 1):
            print(f"{Fore.GREEN}{Style.BRIGHT}{num}: {txt.text}")
    
    elif( option == "-a"):            
        loadPage = requests.get(f"https://www.thesaurus.com/browse/{word}")
        src = loadPage.content
        soup = beSo(src, 'html.parser')
        myText = soup.find_all("a", {"class":"css-itvgb eh475bn1"})
        #myTextWeak = soup.find_all("a", {"class" : ""})
        print(f"{Fore.CYAN}{Style.BRIGHT}Antonyms of {word}:")
        for num, txt in enumerate(myText, 1):
            print(f"{Fore.RED}{Style.BRIGHT}{num}: {txt.text}")

    elif( option == "-m"):
        try:
            res = requests.get(f" https://api.dictionaryapi.dev/api/v1/entries/en/{word} ")
            res_json = json.loads(res.content)
            print(f"{Fore.CYAN}{Style.BRIGHT}Meaning of {word}: ")
            n = 1
            for v in res_json[0]['meaning'].values():
                for m in range(len(v)):
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{n}: {v[m]['definition']}")
                    n +=1
        except KeyError:
            print(f"{Fore.RED} Sorry couldn't find the meaning of this word !!")

    else:
        print("Usage pluck [OPTIONS] [WORD] \n Examples: \n $ pluck -m good  (Fetches meaning of good) \n $ pluck -s good  (Fetch synonyms of good) \n $ pluck -a good  (Fetch antonyms of good) ")
