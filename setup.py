from setuptools import setup, find_packages

setup(
    name="axiomflow",
    version="0.1.0",
    description="The official usability layer built on top of Axiom and ContextFlow.",
    author="studentleaner",
    packages=find_packages(),
    install_requires=[
        "axiom",
        "contextflow",
        "PyYAML"
    ],
    python_requires=">=3.10",
)
