from setuptools import setup, find_packages

setup(
    name='studyProject',
    # version='1.0',
    # description='A description of your project',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # author='Your Name',
    # author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        "PySide6","pymysql"
    ],
)
