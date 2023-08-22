"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""
from typing import Dict, List, Tuple
from bs4 import BeautifulSoup
import requests


class Words:
    """ Class representing unique words counting from the page. """
    def __init__(self):
        self.words_in_text: Dict[str, int] = dict()
        self.text: List[str] = ['']

    def get_text(self, url: str) -> None:
        """
        Get text from the page of the given URL.
        :param url: URL of the page.
        :return: text of the page.
        """
        source = requests.get(url, timeout=10).text
        text_from_page = BeautifulSoup(source, 'lxml').text
        self.text = text_from_page.split()

    def count_words(self) -> None:
        """
        Count words in the text.
        """
        for word in self.text:
            if word.isalpha():
                self.add_word(word_to_add=word.lower())

    def add_word(self, word_to_add: str) -> None:
        """
        Add word to the dictionary of words.
        :param word_to_add: word to add to.
        """
        if word_to_add in self.words_in_text:
            self.words_in_text[word_to_add] += 1
        else:
            self.words_in_text[word_to_add] = 1

    def get_top_10_frequent_words(self) -> List[Tuple[str, int]]:
        """
        Get top 10 frequent words.
        :return: pairs of words and their frequency.
        """
        sorted_words = sorted(self.words_in_text.items())
        sorted_words.sort(key=lambda x: x[-1], reverse=True)
        return sorted_words[:10]


words = Words()
words.get_text(url='https://peps.python.org/pep-0020/')
words.count_words()
print(words.get_top_10_frequent_words())
