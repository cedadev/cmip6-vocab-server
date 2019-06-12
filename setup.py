from setuptools import setup, find_packages
from cmip_vocab_server import __version__


def readme():
    with open('README.md') as f:
        return f.read()


reqs = [line.strip() for line in open('requirements.txt')]


GIT_REPO = "https://github.com/cedadev/cmip6-vocab-server"

setup(
    name="cmip6-vocab-server",
    version=__version__,
    description="Python django application for serving CMIP6 vocabularies as json-ld.",
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='',
    author="Antony Wilson",
    author_email="antony.wilson@stfc.ac.uk",
    url=GIT_REPO,
    packages=find_packages(),
    install_requires=reqs,
    tests_require=['pytest'],
    classifiers=[
        'Development Status :: 2 - ???',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: ???',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
    include_package_data=True,
    scripts=[],
    entry_points={},
)
