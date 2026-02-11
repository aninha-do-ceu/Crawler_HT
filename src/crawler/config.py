# define a URL padrão dos portais
portals_template = {
    'cnn':'https://www.cnnbrasil.com.br',
    'carta_capital':'https://www.cartacapital.com.br',
    #'amazonas_atual': 'https://amazonasatual.com.br',
    'bnc_amazonas':'https://bncamazonas.com.br'
}

# define os termos a serem buscados
terms = ["trafico-de-pessoas","trafico-humano"]
# ver se adiciona "tráfico sexual"

# define a pagina padrão para busca
page = 1

# define a URL padrão de busca de termos para cada portal
# cnn brasil
urls_search_cnn = { term: f"https://www.cnnbrasil.com.br/pagina/{page}/?search={term}" for term in terms}
# carta capital
urls_search_cc = { term: f"https://www.cartacapital.com.br/page/{page}/?s={term}" for term in terms}
# amazonas atual
urls_search_aa = { term: f"https://amazonasatual.com.br/page/{page}/?s={term}" for term in terms}
# BNC amazonas
urls_search_bnc = { term: f"https://bncamazonas.com.br/page/{page}/?s={term}" for term in terms}

portals_template_search = {
    'cnn':urls_search_cnn,
    'carta_capital':urls_search_cc,
    #'amazonas_atual':urls_search_aa,
    'bnc_amazonas':urls_search_bnc
}

portals_div_urls = {
    'cnn':['div', 'flex flex-col gap-4'],
    'carta_capital': ['div','l-list__left'],
    'bnc_amazonas':['div','grid grid-cols-1 gap-12 lg:gap-[60px]']
}