from setuptools import setup, find_packages

setup(
    name="demoqa_testing",
    version="1.0.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        'selenium',
        'pytest',
        'pytest-html',
        'allure-pytest',
        'webdriver-manager',
        'pytest-xdist',
        'faker'
    ]
)