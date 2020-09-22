from setuptools import setup

setup(
    name="storage",
    version='0.1',
    py_modules=['query', 'utils'],
    install_requires=[
        'Click',
        'python-decouple',
        'base58'
    ],
    entry_points={
        "console_scripts": [
            "storage=query:main"
        ],
    },
)
