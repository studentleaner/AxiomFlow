from setuptools import setup, find_packages

setup(
    name="axiomflow",
    version="1.0.0",
    description="The official usability layer built on top of Axiom and ContextFlow.",
    author="studentleaner",
    packages=find_packages(),
    install_requires=[
        "axiom",
        "contextflow",
        "PyYAML",
        "streamlit"
    ],
    entry_points={
        "console_scripts": [
            "axiomflow=axiomflow.cli.main:main",
            "axiomflow-ui=axiomflow.ui.app:main"
        ]
    },
    python_requires=">=3.10",
)
