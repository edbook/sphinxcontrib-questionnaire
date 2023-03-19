import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='sphinxcontrib-questionnaire',
    version='2.0.5',
    author='Naeka',
    author_email='contact@naeka.fr',
    maintainer="Benedikt Magnusson",
    maintainer_email="bsm@hi.is",
    namespace_packages=["sphinxcontrib"],
    description="A sphinx extension to integrate multiple choices "
                "questionnaires",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/naeka/sphinx-ext-eqt',
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=[
        ('_static', [
            'sphinxcontrib/_static/css/eqt.css',
            'sphinxcontrib/_static/js/eqt.js',
        ])
    ],
    classifiers=(
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Topic :: Utilities',
    ),
)
