import sys
from unittest.mock import MagicMock

# Mock dependencies before importing axiomflow since these might not be installed in the environment
sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()

import unittest
from axiomflow import run
from axiomflow.runner import axiom
from axiomflow.bridge import contextflow

class TestRunner(unittest.TestCase):
    def setUp(self):
        # Reset mocks before each test
        axiom.reset_mock()
        contextflow.reset_mock()

    def test_run_executes_correctly(self):
        # Setup mocks
        mock_registry = MagicMock()
        mock_workflow = MagicMock()
        mock_plan = MagicMock()
        
        axiom.load_registry.return_value = mock_registry
        mock_registry.get_workflow.return_value = mock_workflow
        axiom.compile.return_value = mock_plan
        
        mock_engine = MagicMock()
        mock_session = MagicMock()
        
        contextflow.ContextEngine.return_value = mock_engine
        mock_engine.create_session.return_value = mock_session
        
        expected_result = {"status": "success"}
        mock_session.run.return_value = expected_result
        
        # Execute
        inputs = {"query": "hello"}
        result = run("workflow.support_router", inputs)
        
        # Assertions
        axiom.load_registry.assert_called_once()
        mock_registry.get_workflow.assert_called_once_with("workflow.support_router")
        axiom.compile.assert_called_once_with(mock_workflow)
        
        contextflow.ContextEngine.assert_called_once()
        mock_engine.create_session.assert_called_once_with(mock_plan)
        mock_session.run.assert_called_once_with(inputs)
        
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
