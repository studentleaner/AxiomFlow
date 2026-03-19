import sys
import unittest
from unittest.mock import MagicMock, patch

sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import editor

class TestEditorWorkflow(unittest.TestCase):
    
    @patch('axiomstudio.services.files.read_file')
    @patch('axiomstudio.services.files.parse_dict')
    def test_load_workflow(self, mock_parse, mock_read):
        mock_read.return_value = "raw"
        mock_parse.return_value = {"id": "test"}
        
        result = editor.load_workflow_file("test")
        self.assertEqual(result, {"id": "test"})
        mock_read.assert_called_once()
        mock_parse.assert_called_once_with("raw", "test.yaml")

if __name__ == '__main__':
    unittest.main()
