"""
Setup script for Tic Tac Toe game package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tic-tac-toe-game",
    version="1.0.0",
    author="Developer",
    description="A well-structured Tic Tac Toe game with AI opponents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Board Games",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "tic-tac-toe=main:main",
        ],
    },
    keywords="tic-tac-toe game ai minimax cli",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/tic-tac-toe/issues",
        "Source": "https://github.com/yourusername/tic-tac-toe",
    },
)