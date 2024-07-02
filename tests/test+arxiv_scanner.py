import unittest
from unittest.mock import patch
import datetime
from src import arxiv_scanner

class TestArxivScanner(unittest.TestCase):

    def test_get_yesterday_date(self):
        # This test will depend on the current date, so we need to mock datetime
        with patch('src.arxiv_scanner.datetime') as mock_datetime:
            mock_datetime.date.today.return_value = datetime.date(2023, 7, 1)
            mock_datetime.timedelta.side_effect = datetime.timedelta
            self.assertEqual(arxiv_scanner.get_yesterday_date(), '20230630')

    def test_parse_arxiv_response(self):
        # Mock XML data
        xml_data = '''
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <title>Test Paper</title>
            <author><name>John Doe</name></author>
            <summary>This is a test summary.</summary>
          </entry>
        </feed>
        '''
        papers = arxiv_scanner.parse_arxiv_response(xml_data)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0], ('Test Paper', 'John Doe', 'This is a test summary.'))

if __name__ == '__main__':
    unittest.main()