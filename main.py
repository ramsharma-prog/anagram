from collections import defaultdict
import time
from bs4 import BeautifulSoup
import requests


def scraping_data():
    """" fun() scrapes the data from github with beautiful soup & exports to words.txt file"""

    url = "https://github.com/ramsharma-prog/anagram_wordlists/blob/f91bd82fbd2b773c350ed0f5762875365659eb51/smallish_list.txt"
    response = requests.get(url, headers={'User-Agent': 'Chrome/96.0.4664.45'})
    response_code = response.status_code
    if response_code != 200:
        print("Error occurred while scraping the data")
        return
    html_contect = response.content
    dom = BeautifulSoup(html_contect, 'html.parser')
    time.sleep(5)
    data_response = dom.find_all(name='td', class_='blob-code blob-code-inner js-file-line')
    for data in data_response:
        with open('words.txt', 'a') as export_data:
            export_data.writelines(f"{data.text}\n")


if __name__ == "__main__":
    print("Data scraping in process...\n")
    scraping_data()
    time.sleep(5)
    print("Data has been exported to words.txt file.\n")
    print("Preparing data for anagram words...\n")

    time.sleep(5)

    # -Code to check Anagrams words from word.text file- #
    with open('words.txt') as words_text:
        word_data = words_text.readlines()
        amended_word_data = [x.lower()[:-1] for x in word_data]

        default_data = defaultdict(list)
        for element in amended_word_data:
            default_data[str(sorted(element))].append(element)
        amended_default_results = list(default_data.values())

        anagram_data = [i for i in amended_default_results if i[1:]]
        for data in anagram_data:
            results = {''.join(sorted(r)): data for r in data}
            print(results)
