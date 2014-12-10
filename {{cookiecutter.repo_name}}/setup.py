from setuptools import (
    find_packages,
    setup,
)

import service

requirements = [
# TODO package requirements
]

test_requirements = [
    'nose>=1.0',
    'coverage>=1.0',
    'mock==1.0.1',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version=service.__version__,
    description='{{ cookiecutter.project_short_description }}',
    packages=find_packages(exclude=[
        "*.tests",
        "*.tests.*",
        "tests.*",
        "tests",
    ]),
    install_requires=requirements,
    tests_require=test_requirements,
)
