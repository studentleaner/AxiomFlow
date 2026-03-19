import sys
import argparse
from unittest.mock import MagicMock, patch

# Provide mock dependencies dynamically guarding execution scopes
sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()

import unittest
from axiomflow.cli.commands import init, build, validate, run, search

class TestCLI(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('axiomflow.cli.commands.init.scaffold')
    def test_cli_init(self, mock_scaffold, mock_file):
        args = argparse.Namespace(name="my_proj")
        init.handle(args)
        
        mock_scaffold.init_project.assert_called_once_with("my_proj")
        mock_file.assert_called_once_with("my_proj/axiomflow.yaml", "w")
        
    @patch('axiomflow.cli.commands.build.json')
    @patch('axiomflow.cli.commands.build.axiom')
    def test_cli_build(self, mock_axiom, mock_json):
        args = argparse.Namespace(workflow="flow1")
        mock_registry = MagicMock()
        mock_axiom.load_registry.return_value = mock_registry
        
        # Override file logic trivially for test contexts. 
        with patch("builtins.open", unittest.mock.mock_open()):
            build.handle(args)
        
        mock_axiom.load_registry.assert_called_once_with("./registry")
        mock_registry.get_workflow.assert_called_once_with("flow1")
        mock_axiom.compile.assert_called_once()
        
    @patch('axiomflow.cli.commands.validate.validator')
    @patch('axiomflow.cli.commands.validate.parser')
    def test_cli_validate(self, mock_parser, mock_validator):
        args = argparse.Namespace(path="file.yaml")
        mock_parser.parse_yaml.return_value = {"type": "workflow"}
        mock_validator.validate_workflow_json.return_value = True
        
        validate.handle(args)
        
        mock_parser.parse_yaml.assert_called_once_with("file.yaml")
        mock_validator.validate_workflow_json.assert_called_once_with({"type": "workflow"})
        
    @patch('axiomflow.cli.commands.run.runner')
    def test_cli_run(self, mock_runner):
        args = argparse.Namespace(workflow="flow1")
        mock_runner.run.return_value = {"status": "ok"}
        
        run.handle(args)
        
        mock_runner.run.assert_called_once_with("flow1", {})
        
    @patch('axiomflow.cli.commands.search.axiom')
    def test_cli_search(self, mock_axiom):
        args = argparse.Namespace(tag="routing")
        mock_registry = MagicMock()
        mock_axiom.load_registry.return_value = mock_registry
        mock_registry.query.return_value = ["res1"]
        
        search.handle(args)
        
        mock_axiom.load_registry.assert_called_once_with("./registry")
        mock_registry.query.assert_called_once_with(tag="routing")

if __name__ == '__main__':
    unittest.main()
