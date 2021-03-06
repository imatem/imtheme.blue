# -*- coding: utf-8 -*-
"""Installer for the imtheme.blue package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='imtheme.blue',
    version='1.0a1',
    description="Theme for Plone 4",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Informática Académica',
    author_email='gil@im.unam.mx',
    url='https://github.com/collective/imtheme.blue',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/imtheme.blue',
        'Source': 'https://github.com/collective/imtheme.blue',
        'Tracker': 'https://github.com/collective/imtheme.blue/issues',
        # 'Documentation': 'https://imtheme.blue.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['imtheme'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        'Products.Collage',
        # -*- Extra requirements: -*-
        # 'plone.app.themingplugins',
        # 'collective.themefragments',
        'z3c.jbot',
        'plone.api>=1.8.4',
        # 'plone.app.dexterity',
        # 'plone.app.referenceablebehavior',
        # 'plone.app.relationfield',
        # 'plone.app.lockingbehavior',
        # 'plone.schema',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = imtheme.blue.locales.update:update_locale
    """,
)
