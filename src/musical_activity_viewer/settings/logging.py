import logging
import os

from log4mongo.handlers import MongoHandler


# REF
# https://github.com/log4mongo/log4mongo-python/blob/c2aac237689e4a3a9abbb61740e6d5d30f8e7be7/log4mongo/handlers.py#L78-L113
class BaseMongoHandler(MongoHandler):
    def __init__(self):
        super().__init__(
            host=(
                os.getenv('MONGO_HOST')
                if os.getenv('MONGO_HOST', None)
                else "localhost"
            ),
        )
        self.database_name = "django_log"
        # self.host = "localhost"
        # self.port = 27017
        # self.collection_name = ""
        # self.username = "root"
        # self.password = "example"
        # self.authentication_database_name = "admin"
        # self.fail_silently = False
        # self.connection = None
        # self.db = None
        # self.collection = None
        # self.authenticated = False
        # self.formatter = formatter or MongoFormatter()
        # self._connect()


class DjangoCRUDMongoHandler(BaseMongoHandler):
    def __init__(self):
        super().__init__()
        self.collection_name = "django_crud"
        self._connect()


class DjangoQTaskMongoHandler(BaseMongoHandler):
    def __init__(self):
        super().__init__()
        self.collection_name = "djangoq_task"
        self._connect()


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "django_crud": {
            "class": DjangoCRUDMongoHandler,
        },
        "django_task": {
            "class": DjangoQTaskMongoHandler,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": 11,
            "propagate": False,
            "format": "\n".join(
                [
                    "👉 %(levelname)s: L%(lineno)d @ %(pathname)s",
                    "%(message)s",
                ],
            ),
        },
        "django_crud": {
            "handlers": ["django_crud"],
            "level": 1,
            "propagate": False,
        },
        "django_task": {
            "handlers": ["django_task"],
            "level": 1,
            "propagate": False,
        },
    },
}
