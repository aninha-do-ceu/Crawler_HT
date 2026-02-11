# ---------------------------------------- #

# Classe do extrator de informações

# ---------------------------------------- #

from bs4 import BeautifulSoup
import re

class Extractor:
    """
    Base para a extração de dados
    Métodos:
        extract_page_search_numbers
        recognize_link
        extract_links
    """
    def __init__(self):
        pass

    def extract_page_search_numbers(self, html: BeautifulSoup):
        num_url_max = 1
        for a in html.find_all("a", href=True):
            match1 = re.search(r'/pagina/(\d+)/', a.get("href"))
            match2 = re.search(r'/page/(\d+)/', a.get("href"))
            if match1:
                if int(match1.group(1)) >= int(num_url_max):
                    num_url_max = int(match1.group(1)) + 1
            elif match2:
                if int(match2.group(1)) >= int(num_url_max):
                    num_url_max = int(match2.group(1)) + 1

        return num_url_max


    def recognize_link(self, html: str, portal_template: str):
        pattern = re.compile(
            fr'<a[^>]*href="(?P<url>{portal_template}/[^"]*)"[^>]*>'
            r'.*?<h2[^>]*>(?P<title>.*?)</h2>.*?</a>',
            re.DOTALL
        )
        matches = pattern.findall(str(html))
        return matches

    def extract_links(self, dict_html: dict, portals_template: dict):
        list_urls = []
        for portal, list_html_search in dict_html.items():
            for html_search in list_html_search:
                divs_links = html_search.find_all(class_='flex flex-col gap-4')

                for link in divs_links:
                    urls = self.recognize_link(link, portals_template[portal])
                    list_urls = [*list_urls, *urls]
        return list_urls