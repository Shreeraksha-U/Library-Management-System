# Library Management

A small Django app for managing a library's books, members, and borrowing records.

## Features

- Book catalog (title, author, ISBN, availability)
- Member list (name, email, phone)
- Borrow records linking members to books, with borrow and return dates
- Django admin panel for adding and editing everything

## Pages

| URL         | Description     |
|-------------|-----------------|
| `/`         | List of books   |
| `/members/` | List of members |
| `/admin/`   | Admin panel     |

## Setup

Requires Python 3.10+.

```bash
# 1. Clone and enter the project
git clone <your-repo-url>
cd library_management

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env            # Windows: copy .env.example .env
# Then edit .env and set DJANGO_SECRET_KEY (see below)

# 5. Create the database and an admin user
python manage.py migrate
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
```

Open http://127.0.0.1:8000/ and log in to the admin at http://127.0.0.1:8000/admin/ to add books and members.

## To Run tests

```bash
python manage.py test
```

## Configuration

Settings are read from environment variables (or a local `.env` file):

| Variable               | Description                                          |
|------------------------|------------------------------------------------------|
| `DJANGO_SECRET_KEY`    | **Required.** Keep it private.                       |
| `DJANGO_DEBUG`         | `True` for development, `False` in production.       |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hostnames, needed when DEBUG is off. |

Generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key as g; print(g())"
```

## Notes

- `.env` and `db.sqlite3` are git-ignored, so your secrets and data stay local.
