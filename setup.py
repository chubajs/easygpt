from setuptools import setup, find_packages
from easygpt.version import version

# Extract major and minor version only
version_major_minor = '.'.join(version.split('.')[:2])

setup(
    name='easygpt',
    version=version_major_minor,
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
