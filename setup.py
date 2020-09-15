from setuptools import setup

setup(
    name="storage",
    version='0.1',
    py_modules=['query'],
    install_requires=[
        'Click',
    ],
    entry_points={
        "console_scripts": [
            "storage=query:main"
        ],
    },
)
