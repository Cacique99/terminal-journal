from setuptools import setup

setup(
    name="tj",
    version="0.1.0",
    packages=["tj"],
    include_package_data=True,
    install_requires=[
        'click',
        'pylint',
        'pytest',
        'pydocstyle',
        'pycodestyle',
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "tj = tj.__main__:main"
        ]
    },
)
