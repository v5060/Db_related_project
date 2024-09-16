# setup.py
from setuptools import setup, find_packages

setup(
    name='localdb',  # Name of your package
    version='1.0',  # Version of your package
    packages=find_packages(),  # Automatically find packages in the directory
    description='A simple local database package using SQLite',  # Short description
    # long_description=open('README.md').read(),  # Long description read from a README file
    # long_description_content_type='text/markdown',  # Specify the format of the long description
    author='Vikash Kumar',  # Author name
    author_email='vikash.20.kumar@nokia.com',  # Author email
    url='https://github.com/v5060/Db_related_project',  # URL for the package (e.g., GitHub repository)
    classifiers=[
        'Development Status :: 3 - Alpha',  # Development status
        'Intended Audience :: Testers',  # Audience
        'Programming Language :: Python :: 3',  # Python version
        'Programming Language :: Python :: 3.8',  # Specific Python versions
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[
        # List your package dependencies here if you have any
        # e.g., 'numpy>=1.19.2',
    ],
    include_package_data=True,  # Include non-Python files listed in MANIFEST.in
)
