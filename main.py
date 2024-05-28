import requests
from bs4 import BeautifulSoup

def baidu_search(query):
    url = f"https://www.baidu.com/s?wd={query}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to retrieve content")
        return None

def parse_search_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    results = []
    for item in soup.find_all('div', class_='result c-container'):
        title = item.h3.a.get_text()
        link = item.h3.a['href']
        snippet = item.find('div', class_='c-abstract')
        snippet_text = snippet.get_text() if snippet else ''
        results.append({
            'title': title,
            'link': link,
            'snippet': snippet_text
        })
    return results

def main():
    query = "美白"
    html = baidu_search(query)
    if html:
        results = parse_search_results(html)
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print(f"Snippet: {result['snippet']}")
            print("-" * 40)

if __name__ == "__main__":
    main()
