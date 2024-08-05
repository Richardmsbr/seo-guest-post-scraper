import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Função para extrair URLs de guest post de uma página específica
def get_guest_post_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    urls = []
    for link in soup.find_all('a', href=True):
        if 'guest-post' in link['href']:
            urls.append(link['href'])
    return urls

# Função para analisar os dados de SEO da URL do guest post
def analyze_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Exemplo de análise simples de SEO
    title = soup.title.string if soup.title else 'No Title'
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    meta_desc_content = meta_desc['content'] if meta_desc else 'No Description'
    
    return {'URL': url, 'Title': title, 'Meta Description': meta_desc_content}

# URL do site que contém guest posts
site_url = 'https://www.exemplo.com/blog'

# Coleta das URLs de guest posts
guest_post_urls = get_guest_post_urls(site_url)

# Análise dos dados de SEO dos guest posts
seo_data = []
for url in guest_post_urls:
    seo_data.append(analyze_seo(url))

# Exportar os dados para um arquivo CSV
df = pd.DataFrame(seo_data)
df.to_csv('seo_guest_posts.csv', index=False)

print("Análise de SEO concluída e dados salvos em seo_guest_posts.csv")
