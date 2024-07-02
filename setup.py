from setuptools import setup, find_packages

setup(
    name='arxiv-daily-scanner',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'arxiv-scanner=arxiv_scanner:main',
        ],
    },
)