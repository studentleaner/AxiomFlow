import sys
import unittest
from unittest.mock import MagicMock, patch

# Ensure test context executes identically decoupled from any internal processing logics securely
sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio import api

class TestStudioAPI(unittest.TestCase):
    
    @patch("axiomstudio.services.registry.os.listdir")
    @patch("axiomstudio.services.registry.os.path.exists")
    def test_list_workflows(self, mock_exists, mock_listdir):
        mock_exists.return_value = True
        mock_listdir.return_value = ["flow1.yaml", "flow2.yaml", "bad.txt"]
        
        workflows = api.list_workflows()
        
        self.assertEqual(workflows, ["flow1", "flow2"])
        mock_exists.assert_called_with("workflows")
        
    @patch("axiomstudio.services.runner.runner")
    def test_run_workflow(self, mock_runner):
        mock_runner.run.return_value = {"status": "ok"}
        
        result = api.run_workflow("flow1", {"var": 1})
        
        mock_runner.run.assert_called_once_with("flow1", {"var": 1})
        self.assertEqual(result, {"status": "ok"})
        
    @patch("axiomstudio.services.runner.subprocess.run")
    def test_build_workflow(self, mock_subprocess):
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "built"
        mock_subprocess.return_value = mock_result
        
        result = api.build_workflow("flow1")
        
        mock_subprocess.assert_called_once_with(["axiomflow", "build", "flow1"], capture_output=True, text=True)
        self.assertEqual(result, "built")

if __name__ == '__main__':
    unittest.main()
