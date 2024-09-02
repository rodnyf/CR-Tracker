import pathlib

from setuptools import setup, find_packages

setup(name='crtracker',
      version='0.21.0',
      description='A tool to track your TFSA Contribution Room from Questrade and Wealthsimple',
      author='RF',
      author_email='me@gmail.com',
      license='MIT',
      packages=find_packages(),
      long_description=pathlib.Path('README.md').read_text(),
      long_description_content_type='text/markdown',
      install_requires=['questrade_api', 'pandas', 'numpy'],
      classifiers=["Development Status :: 3 - Alpha"],
      url="https://github.com/rodnyf/CR-Tracker",
      project_urls={'Source Code': 'https://github.com/rodnyf/CR-Tracker'}
      )

