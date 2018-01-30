# bookstore
我的书城案例--python--django
atguigu@ubuntu:~/djiango/bookstore2$ tree
.
├── book
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_address.py
│   │   ├── 0003_auto_20180123_1310.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-35.pyc
│   │       ├── 0002_address.cpython-35.pyc
│   │       ├── 0003_auto_20180123_1310.cpython-35.pyc
│   │       └── __init__.cpython-35.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   ├── models.cpython-35.pyc
│   │   ├── tasks.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── views.cpython-35.pyc
│   ├── tasks.py
│   ├── templatetags
│   │   ├── filters.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── filters.cpython-35.pyc
│   │       └── __init__.cpython-35.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── books
│   ├── admin.py
│   ├── enums.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20180125_0803.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-35.pyc
│   │       ├── 0002_auto_20180125_0803.cpython-35.pyc
│   │       └── __init__.cpython-35.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-35.pyc
│   │   ├── enums.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   ├── models.cpython-35.pyc
│   │   ├── search_indexes.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── views.cpython-35.pyc
│   ├── search_indexes.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── bookstore2
│   ├── celery.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── __pycache__
│   │   ├── celery.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── wsgi.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── cart
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-35.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   ├── models.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── views.cpython-35.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db
│   ├── base_models.py
│   ├── __init__.py
│   └── __pycache__
│       ├── base_models.cpython-35.pyc
│       └── __init__.cpython-35.pyc
├── manage.py
├── order
│   ├── admin.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_auto_20180127_0324.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-35.pyc
│   │       ├── 0002_auto_20180127_0324.cpython-35.pyc
│   │       └── __init__.cpython-35.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   ├── models.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── views.cpython-35.pyc
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── css
│   │   ├── main.css
│   │   └── reset.css
│   ├── images
│   │   ├── adv01.jpg
│   │   ├── adv02.jpg
│   │   ├── banner01.jpg
│   │   ├── banner02.jpg
│   │   ├── banner03.jpg
│   │   ├── banner04.jpg
│   │   ├── banner05.jpg
│   │   ├── banner06.jpg
│   │   ├── book
│   │   │   ├── book001.jpg
│   │   │   ├── book002.jpg
│   │   │   ├── book003.jpg
│   │   │   ├── book004.jpg
│   │   │   ├── book005.jpg
│   │   │   ├── book006.jpg
│   │   │   ├── book007.jpg
│   │   │   ├── book008.jpg
│   │   │   ├── book009.jpg
│   │   │   ├── book010.jpg
│   │   │   ├── book011.jpg
│   │   │   ├── book012.jpg
│   │   │   ├── book013.jpg
│   │   │   ├── book014.jpg
│   │   │   ├── book015.jpg
│   │   │   ├── book016.jpg
│   │   │   ├── book017_353MKj3.jpg
│   │   │   ├── book017.jpg
│   │   │   ├── book017_XDPGNRZ.jpg
│   │   │   ├── book018.jpg
│   │   │   ├── book020.jpg
│   │   │   ├── book021.jpg
│   │   │   ├── book023.jpg
│   │   │   └── book024.jpg
│   │   ├── book02.jpg
│   │   ├── book_detail.jpg
│   │   ├── book.jpg
│   │   ├── down.png
│   │   ├── icons02.png
│   │   ├── icons.png
│   │   ├── interval_line.png
│   │   ├── left_bg.jpg
│   │   ├── login_banner.png
│   │   ├── logo02.png
│   │   ├── logo.png
│   │   ├── pay_icons.png
│   │   ├── register_banner.png
│   │   ├── shop_cart.png
│   │   ├── slide02.jpg
│   │   ├── slide03.jpg
│   │   ├── slide04.jpg
│   │   └── slide.jpg
│   ├── __init__.py
│   └── js
│       ├── cart.js
│       ├── cart-update.js
│       ├── detail.js
│       ├── jquery-1.12.4.min.js
│       ├── jquery.cookie.js
│       ├── jquery-ui.min.js
│       ├── login.js
│       ├── order.js
│       ├── pay.js
│       ├── register.js
│       └── slide.js
├── templates
│   ├── base.html
│   ├── base_sidebar.html
│   ├── __init__.py
│   ├── search
│   │   ├── indexes
│   │   │   └── books
│   │   │       └── books_text.txt
│   │   └── search.html
│   ├── search_top.html
│   └── users
│       ├── cart.html
│       ├── detail.html
│       ├── index.html
│       ├── list.html
│       ├── login.html
│       ├── place_order.html
│       ├── register.html
│       ├── user_center_info.html
│       ├── user_center_order.html
│       └── user_center_site.html
├── utils
│   ├── decorators.py
│   ├── get_hash.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── decorators.cpython-35.pyc
│   │   ├── get_hash.cpython-35.pyc
│   │   ├── __init__.cpython-35.pyc
│   │   └── time.cpython-35.pyc
│   └── time.py
└── whoosh_index
    ├── MAIN_2g9ac8fq6k9k80b1.seg
    ├── _MAIN_2.toc
    ├── MAIN_9tn5mp28luyfijxn.seg
    └── MAIN_WRITELOCK
