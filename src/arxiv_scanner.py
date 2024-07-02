import datetime
import urllib.request
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_yesterday_date():
    return (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')

def fetch_arxiv_papers(date):
    base_url = 'http://export.arxiv.org/api/query?'
    search_query = f'submittedDate:{date}235959'
    start = 0
    max_results = 100
    
    url = f"{base_url}search_query={search_query}&start={start}&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    
    try:
        with urllib.request.urlopen(url) as response:
            xml_data = response.read()
    except urllib.error.URLError as e:
        logger.error(f"Error fetching data from arXiv: {e}")
        return []
    
    return parse_arxiv_response(xml_data)

def parse_arxiv_response(xml_data):
    root = ET.fromstring(xml_data)
    papers = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text.strip()
        authors = ', '.join([author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')])
        summary = entry.find('{http://www.w3.org/2005/Atom}summary').text.strip()
        papers.append((title, authors, summary))
    return papers

def main():
    yesterday = get_yesterday_date()
    papers = fetch_arxiv_papers(yesterday)
    
    logger.info(f"Papers submitted to arXiv on {yesterday}:")
    for paper in papers:
        logger.info(f"Title: {paper[0]}")
        logger.info(f"Authors: {paper[1]}")
        logger.info(f"Summary: {paper[2][:200]}...")
        logger.info("---")

if __name__ == "__main__":
    main()