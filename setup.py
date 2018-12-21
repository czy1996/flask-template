from setuptools import setup, find_packages

setup(
    name='flask-template',
    version='0.0.1',
    maintainer='czy1996',
    description='Flask 开发模板',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
