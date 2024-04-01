from setuptools import setup, find_packages

setup(
    name='portofolio',
    version='0.1',
    python_requires='>=3.8',
    include_package_data=True,
    install_requires=[
        'Django >= 4, < 4.2',
        'djangorestframework',
        'python-decouple',
    ],
    packages=find_packages(),
    extras_require={},
)
