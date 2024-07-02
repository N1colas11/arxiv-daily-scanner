import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

def fetch_arxiv_papers(search_query, start=0, max_results=10):
    base_url = 'http://export.arxiv.org/api/query?'
    
    params = {
        'search_query': search_query,
        'start': start,
        'max_results': max_results,
        'sortBy': 'lastUpdatedDate',
        'sortOrder': 'descending'
    }
    
    url = base_url + urllib.parse.urlencode(params)
    
    print(f"Querying arXiv API with URL: {url}")
    
    with urllib.request.urlopen(url) as response:
        xml_data = response.read()
    
    root = ET.fromstring(xml_data)
    
    papers = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        authors = [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')]
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
        papers.append({'title': title, 'authors': authors, 'summary': summary})
    
    return papers

def main():
    search_query = 'cat:cs.AI'  # Example: Search for papers in the Computer Science AI category
    papers = fetch_arxiv_papers(search_query)
    
    print(f"Papers from arXiv matching query '{search_query}':")
    for paper in papers:
        print(f"Title: {paper['title']}")
        print(f"Authors: {', '.join(paper['authors'])}")
        print(f"Summary: {paper['summary'][:200]}...")  # Print first 200 characters of summary
        print("---")

if __name__ == "__main__":
    main()