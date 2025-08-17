"""
Setup script for YouTube Video Downloader
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="youtube-video-downloader",
    version="1.0.0",
    author="Malinda Prabath",
    author_email="",
    description="Professional YouTube Video Downloader with MVC Architecture",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/malinda6997/YouTube-Videos-Downloader-Application",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "youtube-downloader=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
