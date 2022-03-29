import setuptools

long_description = """
Some shared utilities across multiple ASYML projects.
"""

setuptools.setup(
    name="asyml-utilities",
    version="0.0.1",
    url="https://github.com/asyml/asyml-utilities",

    description="Shared Utilities for ASYML Projects",
    long_description=long_description,
    license='Apache License Version 2.0',

    packages=setuptools.find_packages(),
    platforms='any',

    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
