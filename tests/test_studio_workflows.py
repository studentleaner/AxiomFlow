import sys
import unittest
from unittest.mock import MagicMock, patch, mock_open

sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import workflows

class TestStudioWorkflows(unittest.TestCase):
    
    @patch("axiomstudio.services.workflows.os.listdir")
    @patch("axiomstudio.services.workflows.os.path.exists")
    def test_list_workflows(self, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ["flow1.yaml", "not_flow.txt"]
        
        items = workflows.list_workflows("mock_dir")
        
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["id"], "flow1")
        self.assertEqual(items[0]["file"], "flow1.yaml")

    @patch("axiomstudio.services.workflows.os.path.exists")
    @patch("axiomstudio.services.workflows.parse_yaml")
    @patch("builtins.open", new_callable=mock_open, read_data='flow: data')
    def test_get_workflow(self, mock_file, mock_parse, mock_exists):
        mock_exists.return_value = True
        mock_parse.return_value = {"flow": "data"}
        
        result = workflows.get_workflow("flow1")
        
        self.assertEqual(result, {"flow": "data"})
        mock_parse.assert_called_once_with('flow: data')

if __name__ == '__main__':
    unittest.main()
