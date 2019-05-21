# coding:utf-8
from setuptools import setup, find_packages


setup(
    name='typeidea',
    version='${version}',
    description='Blog System base on Django',
    author='juedi294',
    author_email='juedi294@gmail.com',
    url='https://juedi294.com',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    # package_data={'': [    # 打包数据文件，方法一
        # 'themes/*/*/*/*',  # 需要按目录层级匹配
    # ]},
    include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
        'django~=2.0',
        'gunicorn==19.8.1',
        'supervisor==4.0.0dev0',
        'xadmin==2.0.1',
        'mysqlclient==1.3.12',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.8.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.3',
        'Pillow==4.3.0',
        'coreapi==2.3.3',
        'django-redis==4.8.0',
        'hiredis==0.2.0',
        # debug
        'django-debug-toolbar==1.9.1',
        'django-silk==2.0.0',
    ],
    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],

)
