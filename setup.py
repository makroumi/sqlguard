"""
SQLGuard - SQL Query Analysis Tool

Professional SQL query analyzer that detects anti-patterns,
performance issues, and potential bugs through static analysis.
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sqlguard",
    version="1.0.0",
    author="El Mehdi Makroumi",
    author_email="elmehdi.makroumi@gmail.com",  
    description="SQL query analyzer for detecting anti-patterns and performance issues",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/makroumi/sqlguard",
    project_urls={
        "Bug Tracker": "https://github.com/makroumi/sqlguard/issues",
        "Documentation": "https://github.com/makroumi/sqlguard#readme",
        "Source Code": "https://github.com/makroumi/sqlguard",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "rich>=13.0.0",
        "sqlparse>=0.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "mypy>=1.0.0",
            "flake8>=6.0.0",
            "isort>=5.0.0",
        ],
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "sqlguard=sqlguard.cli:main",  # For v2.0 CLI
        ],
    },
    keywords="sql, query, optimization, performance, analysis, database",
    include_package_data=True,
    zip_safe=False,
)
