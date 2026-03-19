import sys
import unittest
from unittest.mock import MagicMock, patch, mock_open

# Sandbox Axiom core modules
sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import registry

class TestStudioRegistry(unittest.TestCase):
    
    @patch("axiomstudio.services.registry.os.listdir")
    @patch("axiomstudio.services.registry.os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='{"type": "prompt", "version": "2.0", "tags": ["test"]}')
    def test_list_registry_json(self, mock_file, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ["test.json"]
        
        items = registry.list_registry("mock_dir")
        
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["id"], "test.json")
        self.assertEqual(items[0]["type"], "prompt")
        self.assertEqual(items[0]["version"], "2.0")
        self.assertEqual(items[0]["tags"], ["test"])
        
    @patch("axiomstudio.services.registry.os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='{"content": "hello"}')
    def test_get_item(self, mock_file, mock_exists):
        mock_exists.return_value = True
        
        item = registry.get_item("test.json")
        self.assertEqual(item, {"content": "hello"})

if __name__ == '__main__':
    unittest.main()
