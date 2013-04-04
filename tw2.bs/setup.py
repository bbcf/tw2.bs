from setuptools import setup, find_packages


setup(
    name='tw-bs',
    version='0.1.0.1',
    description='Special widgets for Bioscript',
    author='Yohan Jarosz',
    author_email='yohan.jarosz@epfl.ch',
    url='http://gdv.epfl.ch/bs',
    licence='EPFL-BBCF',
    install_requires=[
        "tw2.core",
        "tw2.forms",
        "tw2.devtools",
        "tw2.jquery",
        "tw2.dynforms"
        ## Add other requirements here
        # "Genshi",
    ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages=['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite='nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.bs
    """,
    keywords=[
        'toscawidgets.widgets',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
