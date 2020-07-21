from setuptools import setup

version = '0.1.0'

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='discord-ext-rx',
    author='NCPlayz',
    author_email='chowdhurynadir0@outlook.com',
    python_requires='>=3.6.0',
    url='https://github.com/NCPlayz/discord-ext-rx',
    version=version,
    packages=['discord/ext/rx'],
    license='MIT',
    description='Combine RxPy with discord.py.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'discord.py>0.16.12',
        'rx',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
