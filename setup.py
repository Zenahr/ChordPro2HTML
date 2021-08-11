from setuptools import setup

with open('README.md', 'r') as file:
    long_description = file.read()

setup(name='ChordPro2HTML',
      version='0.1.0',
      description='Add chords to lyrics and export an HTML document out of it!',
      url='https://github.com/Zenahr/ChordPro2HTML',
      author='Zenahr Barzani',
      author_email='zenmatica@gmail.com',
      license='MIT',
      packages=['chordpro2html'],
      keywords=['chordpro',
                'lyrics',
                'chords',
                'music'
      ],
      python_requires='>=3.8.6',
      py_modules=["quicksample"],
      install_requires=[],
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.8',
            'Topic :: Text Processing',
            'Topic :: Utilities'

      ],
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)
