import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("KIWI_DB_NAME", "kiwitcms"),
        "USER": os.environ.get("KIWI_DB_USER", "kiwi"),
        "PASSWORD": os.environ.get("KIWI_DB_PASSWORD", ""),
        "HOST": os.environ.get("KIWI_DB_HOST", "10.190.205.6"),
        "PORT": os.environ.get("KIWI_DB_PORT", "5432"),
        "CONN_MAX_AGE": 60,
    }
}
