from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="markdown_text_clean",
    version="1.0.3",
    LICENSE = 'MIT',
    author="pom",
    author_email="s2222059@stu.musashino-u.ac.jp",
    description="A package to clean markdown text",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    url="https://github.com/pompom7776/markdown-text-clean",
    packages=find_packages(),
    CLASSIFIERS=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
    ],
)
