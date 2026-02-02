from crawler.crawler_base import CrawlerBase
from crawler import config as crawler_config
from extractors.extractor import Extractor
import pandas as pd

if __name__ == '__main__':

    crawler = CrawlerBase()
    extractor = Extractor()

    # buscando o número máximo de páginas retornadas ao se pesquisar algum termo em cada portal
    dict_max_url = crawler.get_max_search_pages_number_portal(portals = crawler_config.portals_template_search,
                                                              terms = crawler_config.terms)

    # pegando html das paginas de buscas para puxar os links
    html_search_pages = crawler.get_html_search_pages(portals = crawler_config.portals_template_search,
                                                      dict_max_url = dict_max_url,
                                                      url_max_opt = 2)

    # puxando os links das paginas
    links = extractor.extract_links(dict_html = html_search_pages,
                                    portals_template = crawler_config.portals_template)

    print(len)
    pd.DataFrame(links).to_csv(r'C:\projeto\IC_HT\links_of_articles.csv',sep="~", encoding='utf-8')



