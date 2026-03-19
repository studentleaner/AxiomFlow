import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure test context executes identically decoupled from any internal processing logics securely
sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio import api

class TestStudioAPI(unittest.TestCase):
    
    @patch("axiomstudio.services.workflows.list_workflows")
    def test_list_workflows(self, mock_list):
        mock_list.return_value = [{"id": "flow1", "name": "Flow 1"}]
        
        workflows = api.list_workflows()
        
        self.assertEqual(workflows, [{"id": "flow1", "name": "Flow 1"}])
        mock_list.assert_called_once()
        
    @patch("axiomstudio.services.run.run")
    def test_run_workflow(self, mock_run):
        mock_run.return_value = {"status": "ok"}
        
        result = api.run_workflow("flow1", {"var": 1})
        
        mock_run.assert_called_once_with("flow1", {"var": 1})
        self.assertEqual(result, {"status": "ok"})

if __name__ == '__main__':
    unittest.main()
