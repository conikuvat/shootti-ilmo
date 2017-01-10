# New photoshoot signup system for Desucon & co.

The aim of this application is to enable cosplayers and photographers find each other in a convention and facilitate arranging cosplay photoshoots.

## Getting started

### Docker Compose

    docker-compose up

In another terminal:

    docker-compose exec web python manage.py import_event frostbite2017
    docker-compose exec web python manage.py make_dummy_photographers 3
    docker-compose exec web python manage.py make_dummy_cosplayers 5

    open http://localhost:8000

### Traditional way

    python3 -m venv venv3-shoottikala
    source venv3-shoottikala/bin/activate
    git clone git@github.com:conikuvat/shoottikala
    cd shoottikala
    pip install -r requirements.txt
    export DEBUG=1

    python manage.py setup
    python manage.py import_event frostbite2017
    python manage.py make_dummy_photographers 3
    python manage.py make_dummy_cosplayers 5

    python manage.py runserver
    open http://localhost:8000

The `setup` script created a superuser `mahti` with password `mahti`. Use [/admin/login/](http://localhost:8000/admin/login/) instead of the login link to log in.

## License

    The MIT License (MIT)

    Copyright (c) 2016–2017 Santtu Pajukanta

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
