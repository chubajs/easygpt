from setuptools import setup, find_packages

setup(
    name='easygpt',
    version='0.1.0',
    url='https://github.com/chubajs/easygpt',
    author='Sergey Bulaev',
    author_email='sergeonsamui@gmail.com',
    description='Easy to use GPT-4 wrapper with cost estimation',
    packages=find_packages(),
    install_requires=[
        'openai>=0.27.2',
        'tiktoken>=0.3.3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
