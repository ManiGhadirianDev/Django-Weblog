# Django Multi‑App Project

## Overview

This repository contains a small Django project named **`First`** with two applications:

| App | Purpose |
|-----|---------|
| `firstOne` | Serves three static pages – *Home*, *About* and *Contact*. |
| `blog` | Provides a minimal blog structure with a `Post` model and two placeholder templates (list view and single‑post view). |

The project is configured to use SQLite for the database and serves static files from the `statics/` directory during development.

---

## Project Structure

```
├─ manage.py                     # Django command‑line utility
├─ First/                        # Project package
│   ├─ __init__.py
│   ├─ asgi.py
│   ├─ settings.py                # Global settings (installed apps, DB, static/media, etc.)
│   ├─ urls.py                    # Root URL dispatcher (includes app urls)
│   └─ wsgi.py
├─ firstOne/                     # Simple static‑page app
│   ├─ __init__.py
│   ├─ admin.py
│   ├─ apps.py
│   ├─ models.py
│   ├─ tests.py
│   ├─ views.py                  # index, about, contact views
│   └─ urls.py                   # URL patterns for the three pages
├─ blog/                         # Basic blog app
│   ├─ __init__.py
│   ├─ admin.py                  # Register `Post` model (optional)
│   ├─ apps.py
│   ├─ migrations/
│   ├─ models.py                 # `Post` model definition
│   ├─ tests.py
│   ├─ views.py                  # Placeholder list & detail views
│   └─ urls.py                   # (should map '' and '<int:pk>/')
├─ templates/                    # Global template directory (used by both apps)
│   ├─ firstOne/ …
│   └─ blog/ …
├─ statics/                      # Development static files (CSS, JS, images)
│   ├─ css/ …
│   ├─ js/ …
│   └─ img/ …
├─ db.sqlite3                    # SQLite database (created after migrations)
└─ README.md                     # <‑‑ **You are reading it!**
```

---

## Prerequisites

- Python 3.10+ (the project was generated with Django 6.0.6)
- `pip` (or `uv`, `poetry`, etc.)
- A virtual environment is strongly recommended to keep dependencies isolated.

---

## Setup & Installation

```bash
# 1. Clone the repository
git clone <repository‑url>
cd <repo‑folder>

# 2. Create and activate a virtual environment (optional but recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Install Django (and any other dependencies if added later)
pip install django==6.0.6

# 4. Apply migrations – this creates the SQLite database and the `Post` table
python manage.py migrate

# 5. (Optional) Create a superuser to access the admin site
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser:
- `/` – Home page (from `firstOne`)
- `/about` – About page
- `/contact` – Contact page
- `/blog/` – Blog placeholder page
- `/admin/` – Django admin (requires the superuser created above)

---

## Extending the Blog (quick start)

The current `blog` views only render static templates. To display real posts:
1. **Update the views** – query `Post` objects and pass them to the template.
2. **Add URL patterns** – include a detail view that accepts a post ID or slug.
3. **Register the model in the admin** – edit `blog/admin.py` to expose `Post`.
4. **Create templates** that iterate over the queryset.

Example snippet for `blog/views.py`:

```python
from django.shortcuts import render, get_object_or_404
from .models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True).order_by('-publushed_date')
    return render(request, 'blog/blog-home.html', {'posts': posts})

def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk, status=True)
    return render(request, 'blog/blog-single.html', {'post': post})
```

---

## static & media handling (development)

- **Static files** are collected from `statics/` (`STATICFILES_DIRS`). Django serves them automatically because `First/urls.py` appends `static()` when `DEBUG=True`.
- **Media files** (user‑uploaded) are stored in `media/` (`MEDIA_ROOT`). The same `static()` helper makes them reachable at `/media/` during development.

For production you would run `python manage.py collectstatic` and configure a proper web server (NGINX, Apache, etc.) to serve the collected files.

---

## License

This starter project is provided **as‑is** for educational purposes. Feel free to modify, extend, and use it in your own applications.

---

## Contact & Contributions

If you have suggestions or want to contribute, open an issue or a pull request on the repository. Happy coding!
# weblog
