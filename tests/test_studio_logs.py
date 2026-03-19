import sys
import unittest
from unittest.mock import MagicMock, patch, mock_open

sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()
sys.modules['streamlit'] = MagicMock()

from axiomstudio.services import logs

class TestStudioLogs(unittest.TestCase):

    @patch("axiomstudio.services.logs.os.path.exists")
    @patch("builtins.open", new_callable=mock_open, read_data='{"plan": "mock_data"}')
    def test_get_last_plan(self, mock_file, mock_exists):
        mock_exists.return_value = True
        
        plan = logs.get_last_plan()
        
        mock_exists.assert_called_once_with("execution_plan.json")
        self.assertEqual(plan, {"plan": "mock_data"})

    def test_get_logs(self):
        log_data = logs.get_logs()
        self.assertTrue(len(log_data) > 0)
        self.assertEqual(log_data[0]["level"], "INFO")

if __name__ == '__main__':
    unittest.main()
