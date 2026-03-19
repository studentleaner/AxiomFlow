import sys
import unittest
from unittest.mock import MagicMock, patch, mock_open

sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import config

class TestStudioConfig(unittest.TestCase):
    
    @patch('os.path.exists', return_value=False)
    def test_load_default(self, mock_exists):
        c = config.load_config()
        self.assertEqual(c["adapter"]["type"], "openai")
        self.assertFalse(c["memory"]["enabled"])

    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data="adapter:\n  type: ollama")
    def test_load_existing(self, mock_file, mock_exists):
        c = config.load_config()
        self.assertEqual(c["adapter"]["type"], "ollama")

    @patch('builtins.open', new_callable=mock_open)
    def test_save_config(self, mock_file):
        config_data = {"adapter": {"type": "anthropic"}}
        config.save_config(config_data)
        self.assertTrue(mock_file().write.called)

if __name__ == '__main__':
    unittest.main()
