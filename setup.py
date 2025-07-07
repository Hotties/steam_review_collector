from setuptools import setup, find_packages

setup(
    name='steam_review_collector',
    version='0.1',
    description='A package for collecting and storing Steam game reviews.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'pymysql',
        'requests',
        'python-dotenv',
        'transformers>=4.0.0',
        'torch>=1.10.0',
        'steamreviews',
        'emoji',
        'soynlp',
        'konlpy',
        'matplotlib',
        'seaborn',
        ###'git+https://github.com/stopwords-iso/stopwords-ko.git'
    ],
)
