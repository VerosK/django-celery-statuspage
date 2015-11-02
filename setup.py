# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='django-celery-statuspage',

    version='0.0.2',

    description='Django view to render Celery status',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/verosk/django-celery-statuspage',

    # Author details
    author='Veros Kaplan',
    author_email='verosk@noreply.users.github.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        'Framework :: Django',
    ],

    keywords='celery django monitoring statuspage',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    #install_requires=[''],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)
