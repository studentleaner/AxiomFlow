import sys
import unittest
from unittest.mock import MagicMock, patch

sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import editor

class TestEditorPrompt(unittest.TestCase):
    
    @patch('axiomstudio.services.files.save_file')
    @patch('axiomstudio.services.files.stringify_dict')
    def test_save_registry(self, mock_str, mock_save):
        mock_str.return_value = "str_data"
        editor.save_registry_file("prompt1.yaml", {"v": 1})
        mock_str.assert_called_once_with({"v": 1}, "prompt1.yaml")
        mock_save.assert_called_once()

if __name__ == '__main__':
    unittest.main()
