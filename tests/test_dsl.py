import sys
from unittest.mock import MagicMock
import os
import shutil
import tempfile
import yaml

# Mock axiom to ensure we're interacting with it at arms lengths, no runtime logic tested
sys.modules['axiom'] = MagicMock()
sys.modules['contextflow'] = MagicMock()

import unittest
from axiomflow.dsl import (
    parse_yaml, 
    generate_workflow, 
    create_support_router, 
    init_project, 
    validate_workflow_json
)
from axiomflow.dsl.validator import AxiomRegistry

class TestDSL(unittest.TestCase):
    def setUp(self):
        AxiomRegistry.reset_mock()
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_parse_yaml(self):
        yaml_path = os.path.join(self.test_dir, "test.yaml")
        yaml_content = {"workflow": {"id": "test", "version": "1.0"}}
        with open(yaml_path, 'w') as f:
            yaml.dump(yaml_content, f)
            
        result = parse_yaml(yaml_path)
        self.assertEqual(result, yaml_content)
        
    def test_generate_workflow(self):
        data = {
            "workflow": {
                "id": "my_flow",
                "nodes": ["node1"],
                "edges": [{"from": "node1", "to": "node2"}]
            }
        }
        json_output = generate_workflow(data)
        self.assertEqual(json_output["type"], "workflow")
        self.assertEqual(json_output["id"], "my_flow")
        self.assertEqual(json_output["version"], "1.0.0")
        self.assertEqual(json_output["nodes"], ["node1"])
        
    def test_templates_produce_json(self):
        router = create_support_router()
        self.assertEqual(router["type"], "workflow")
        self.assertEqual(router["id"], "workflow.support_router")
        self.assertTrue(len(router["nodes"]) > 0)
        
    def test_scaffold(self):
        init_project("my_proj", base_dir=self.test_dir)
        proj_path = os.path.join(self.test_dir, "my_proj")
        self.assertTrue(os.path.exists(os.path.join(proj_path, "registry")))
        self.assertTrue(os.path.exists(os.path.join(proj_path, "workflows")))
        self.assertTrue(os.path.exists(os.path.join(proj_path, "templates")))
        
    def test_validator(self):
        mock_registry = MagicMock()
        AxiomRegistry.return_value = mock_registry
        
        valid = validate_workflow_json({"type": "workflow"})
        
        AxiomRegistry.assert_called_once()
        mock_registry.register_workflow.assert_called_once_with({"type": "workflow"})
        self.assertTrue(valid)
        
        # Test failure scenario
        mock_registry.register_workflow.side_effect = Exception("Invalid schema")
        valid_bad = validate_workflow_json({"type": "bad"})
        self.assertFalse(valid_bad)

if __name__ == '__main__':
    unittest.main()
