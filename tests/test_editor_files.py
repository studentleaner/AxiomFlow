import sys
import unittest
from unittest.mock import MagicMock, patch, mock_open

sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import files

class TestEditorFiles(unittest.TestCase):
    
    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data='key: value')
    def test_read_file(self, mock_file, mock_exists):
        content = files.read_file('test.yaml')
        self.assertEqual(content, 'key: value')

    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_file(self, mock_file, mock_makedirs):
        files.save_file('test.yaml', 'content')
        mock_file().write.assert_called_once_with('content')

if __name__ == '__main__':
    unittest.main()
