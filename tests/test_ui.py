import sys
import unittest
from unittest.mock import MagicMock, patch

# Sandbox dependencies avoiding actual module leakage.
sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()

import streamlit as st

# Mocks avoiding executing full streamlit cycles contextually natively over tests.
st.set_page_config = MagicMock()
st.title = MagicMock()
st.sidebar = MagicMock()
st.sidebar.header = MagicMock()
st.sidebar.radio = MagicMock()
st.write = MagicMock()
st.info = MagicMock()
st.success = MagicMock()
st.error = MagicMock()
st.header = MagicMock()
st.text_input = MagicMock()
st.button = MagicMock()

# Setup structural columns resolving execution context blocks dynamically locally
mock_col1 = MagicMock()
mock_col1.__enter__ = MagicMock(return_value=mock_col1)
mock_col1.__exit__ = MagicMock(return_value=None)

mock_col2 = MagicMock()
mock_col2.__enter__ = MagicMock(return_value=mock_col2)
mock_col2.__exit__ = MagicMock(return_value=None)

st.columns = MagicMock(return_value=[mock_col1, mock_col2])

# Assign internal mocking layers
sys.modules['streamlit'] = st

from axiomflow.ui import runner, app

class TestUI(unittest.TestCase):

    def setUp(self):
        st.button.reset_mock()
        st.button.side_effect = None

    @patch("axiomflow.ui.app.subprocess.run")
    def test_app_shows_connection(self, mock_subprocess):
        st.button.return_value = True
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess.return_value = mock_result
        st.sidebar.radio.return_value = "Home"
        
        app.main()
        
        # Verify architecture: tests the underlying execution path targets CLI ONLY securely
        mock_subprocess.assert_called_once_with(["axiomflow", "--help"], capture_output=True, text=True)
        
    @patch("axiomflow.ui.runner.subprocess.run")
    def test_ui_runner_calls_cli_build(self, mock_subprocess):
        st.text_input.return_value = "flow1"
        
        def mock_button(label):
            return label == "Build Workflow via CLI"
        st.button.side_effect = mock_button
        
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess.return_value = mock_result
        
        runner.render()
        
        # Asserts build hook passes seamlessly
        mock_subprocess.assert_called_once_with(["axiomflow", "build", "flow1"], capture_output=True, text=True)

    @patch("axiomflow.ui.runner.subprocess.run")
    def test_ui_runner_calls_cli_run(self, mock_subprocess):
        st.text_input.return_value = "flow1"
        
        def mock_button(label):
            return label == "Run Workflow via CLI"
        st.button.side_effect = mock_button
        
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_subprocess.return_value = mock_result
        
        runner.render()
        
        # Asserts run executing logic bounds appropriately
        mock_subprocess.assert_called_once_with(["axiomflow", "run", "flow1"], capture_output=True, text=True)

if __name__ == '__main__':
    unittest.main()
