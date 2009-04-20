from setuptools import setup, find_packages

setup(
    name = 'trml2pdf',
    version = '0.1',
    description = 'Tiny RML2PDF is a tool to easily create PDF document without programming.',
    keywords = 'django apps pdf reportlab',
    license = 'GNU LESSER GENERAL PUBLIC LICENSE',
    author = 'Fabien Pinckaers',
    author_email = 'fp@tiny.be',
    maintainer = 'Rohit Sankaran',
    maintainer_email = 'rohit@lincolnloop.com',
    url = 'http://github.com/roadhead/trml2pdf/',
    dependency_links = [],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
)

