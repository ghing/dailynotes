from setuptools import setup


setup(name='dailynotes',
      version='0.3',
      description='Tools for managing daily notes as text files',
      url='http://github.com/ghing/dailynotes',
      author='Geoff Hing',
      author_email='geoffhing@gmail.com',
      license='MIT',
      packages=['dailynotes'],
      install_requires=[
          'Jinja2',
      ],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['dailynotes=dailynotes.cli:main'],
      })
