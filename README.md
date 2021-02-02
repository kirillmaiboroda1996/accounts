# About application.
[![Generic badge](https://img.shields.io/badge/Django-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Django_Soccial-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Sqlite-black.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Js-orange.svg)](https://shields.io/)

Application allows to create both accounts as social and accounts as classic registration.

## Possibilities

- Social authentication with google and facebook.
- Registration with AbstractBaseUser
- Email as username
- Reset password

## Usage

For dev runnig project on your host the first you need to clone the project. 

```bash
https://github.com/kirillmaiboroda1996/accounts.git
```

The next step you need to add .env in your root `registration/` directory.

For example:

```bash
DEBUG=True
SECRET_KEY=foo
FACEBOOK_KEY=foo
FACEBOOK_SECRET=bar

GOOGLE_OAUTH2_KEY=foo
GOOGLE_OAUTH2_SECRET=bar
```

Also you need apply to migrations:
  
```bash
python manage.py makemigrations && python manage.py migrate
```

Finaly you can run server:
  
```bash
python manage.py runserver
```

check out http://localhost:8000/registration/



