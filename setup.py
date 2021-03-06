from setuptools import setup

setup(
    name='becca',
    version='0.10.0',
    description='A general learning algorithm',
    url='http://github.com/brohrer/becca',
    download_url='https://github.com/brohrer/becca/archive/master.zip',
    author='Brandon Rohrer',
    author_email='brohrer@gmail.com',
    license='MIT',
    packages=['becca'],
    include_package_data=True,
    install_requires=[
        'becca_test',
        'becca_toolbox',
        'becca_viz',
        'numpy',
        'numba',
        'matplotlib',
    ],
    zip_safe=False)
