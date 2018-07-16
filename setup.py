from setuptools import setup


setup(name='dailynotes',
      version='0.2',
      description='Tools for managing daily notes as text files',
      url='http://github.com/ghing/dailynotes',
      author='Geoff Hing',
      author_email='geoffhing@gmail.com',
      license='MIT',
      packages=['dailynotes'],
      zip_safe=False,
      entry_points={
          'console_scripts': ['dailynotes=dailynotes.cli:main'],
      })
