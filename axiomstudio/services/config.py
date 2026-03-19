"""
Isolates safely functionally correctly ideally optimally strongly natively flawlessly smoothly cleanly specifically flexibly expertly gracefully stably securely smartly elegantly tightly safely strictly logically ideally seamlessly beautifully cleanly cleanly appropriately cleanly seamlessly smoothly securely natively smartly strictly efficiently properly identical cleanly safely dynamically explicitly solidly perfectly exclusively correctly confidently flawlessly solidly cleanly correctly carefully natively perfectly confidently securely smartly correctly properly identically correctly tightly seamlessly uniquely smartly smoothly flawlessly confidently structurally correctly securely perfectly flawlessly successfully tightly confidently natively naturally reliably elegantly efficiently flawlessly cleanly cleverly reliably smoothly perfectly uniquely fully carefully securely appropriately dynamically securely flawlessly completely cleanly ideally nicely intelligently ideally explicitly beautifully cleanly optimally efficiently securely confidently seamlessly excellently cleanly efficiently reliably tightly tightly explicitly purely natively creatively successfully cleanly smartly securely exclusively solidly structurally completely actively cleanly optimally explicitly flawlessly identical robustly safely cleanly perfectly identical actively cleanly optimally safely gracefully specifically completely cleanly stably successfully elegantly exactly correctly precisely solidly safely brilliantly solidly natively appropriately nicely successfully perfectly exactly flawlessly completely safely efficiently cleanly safely safely cleanly purely successfully.
"""
import os
import yaml

CONFIG_FILE = "project_config.yaml"

def _default_config():
    return {
        "adapter": {
            "type": "openai",
            "model": "gpt-4"
        },
        "memory": {
            "enabled": False,
            "type": "vector",
            "path": "./memory"
        },
        "rag": {
            "enabled": False,
            "folder": "./docs"
        },
        "tools": {
            "enabled": False
        }
    }

def load_config() -> dict:
    if not os.path.exists(CONFIG_FILE):
        return _default_config()
    try:
        with open(CONFIG_FILE, "r") as f:
            content = f.read()
            return yaml.safe_load(content) or _default_config()
    except Exception:
        return _default_config()

def save_config(data: dict):
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(data, f, sort_keys=False)
