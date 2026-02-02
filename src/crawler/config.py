# define a URL padrão dos portais
portals_template = {
    'cnn':'https://www.cnnbrasil.com.br',
    'carta_capital':'https://www.cartacapital.com.br',
    'Amazonas ashshs': 'ahshshs'
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
#amazonas_atual = { term: f"https://amazonasatual.com.br/page/{page}/?s={term}" for term in terms}

portals_template_search = {
    'cnn':urls_search_cnn,
    'carta_capital':urls_search_cc
}
