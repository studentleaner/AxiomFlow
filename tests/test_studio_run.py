import sys
import unittest
from unittest.mock import MagicMock, patch

sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import run

class TestStudioRun(unittest.TestCase):
    
    @patch("axiomstudio.services.run.subprocess.run")
    def test_run_executes_isolated(self, mock_subprocess):
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = "Success!"
        mock_result.stderr = ""
        mock_subprocess.return_value = mock_result
        
        result = run.run("flow1", {"var": 1})
        
        mock_subprocess.assert_called_once_with(["axiomflow", "run", "flow1"], capture_output=True, text=True)
        self.assertTrue(result["status"])
        self.assertEqual(result["stdout"], "Success!")

if __name__ == '__main__':
    unittest.main()
