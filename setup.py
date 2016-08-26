from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

version = __import__('codeformaine').__version__

install_requires = [
    'Django>=1.9,<1.10',
    'django_configurations>=1.0',
    'dj-database-url>=0.3.0',
    'pylibmc>=1.5.0',
    'httplib2>=0.9.2',
    'feedparser>=5.2.1',
    'Pillow>=2.0.0,<3',
    'whoosh>=2.7.4,<3',
    'beautifulsoup4>=4',
    'Unidecode>=0.04', # for filer
    'shortuuid>=0.4',
    'django-filer>=1.2.4',
    'html5lib==0.9999999',
    'future>=0.15', # for forms_builder
    'django-cache-url>=0.8.0',
    'django-smartcc>=0.1.2',
    'werkzeug>=0.9',
    'gunicorn>=0.19',
    'easy-thumbnails>=1.2',
    'django-debug-toolbar>=1.4',
    'django-extensions>=1.6.1',
    'django-braces>=1.4.0',
    'django-localflavor>=1.1',
    'django-allauth>=0.24.1',
    'django-custom-user>=0.5',
    'django-nose>=1.4.1',
    'django-picklefield>=0.3.2',
    'django-tinymce==2.3.0',
    'django-avatar>=3',
    'django-bootstrap3>=7',
    'django-floppyforms>=1.6',
    'raven==5.2.0',
    'boto>=2.39.0',
    'django-storages>=1.4,<2',
    'djangorestframework>=3.3,<3.4',
    'django-cors-headers==1.1.0',
    'django-markdown-deux>=1.0.4',
    'django-filter>=0.9.2',
    'django-templated-email>=0.4.9',
    'django-registration>=2.1',
    'django-typogrify>=1.3.3',
    'django-cms>=3.3,<3.4',
    'djangocms-snippet>=1.8',
    'djangocms-link>=1.8.2',
    'djangocms-picture>=1.0.0',
    'djangocms-file>=1.0.0',
    'djangocms-video>=1.0.0',
    'djangocms-googlemap>=0.4.0',
    'djangocms-inherit>=0.1.1',
    'djangocms-text-ckeditor>=3.0.0',
    'djangocms-flash>=0.3.0',
    'cmsplugin-filer>=1.1.2',
    'django-email-extras>=0.3',
    'aldryn-search>=0.2',
    'django-jenkins>=0.18',
    'celery[redis]>=3.1,<3.2',
    'django-polymorphic<0.9,>=0.7',
]

dep_links = [
]


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)

setup(
    name="codeformaine",
    version=version,
    url='http://github.org/code4maine/codeformaine',
    license='Closed',
    platforms=['OS Independent'],
    description="codeformaine.org Django applications.",
    author="Colin Powell",
    author_email='colin.powell@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=dep_links,
    include_package_data=True,
    zip_safe=False,
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    package_dir={
        'codeformaine': 'codeformaine',
        'codeformaine/templates': 'codeformaine/templates',
        'codeformaine/static': 'codeformaine/static',
    },
    entry_points={
        'console_scripts': [
            'codeformaine = codeformaine.manage_codeformaine:main',
        ],
    },
)
