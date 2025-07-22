from setuptools import setup, find_packages

setup(
    name="sum_automation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "behave",
        "selenium",
        "webdriver-manager"
    ],
    entry_points={
        'console_scripts': [
            'run-behave=behave.__main__:main',
        ],
    },
    include_package_data=True,
    description="Reusable Python Behave Framework",
    author="Sumit Bhandare",
    author_email="sumit@example.com"
)