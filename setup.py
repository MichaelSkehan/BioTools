from setuptools import setup, find_packages

setup(
    name="primertools",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "click>=8.0"
    ],
    entry_points={
        "console_scripts": [
            "ci=cli:main",  # 'ci' command calls main() in cli.py
        ],
    },
)