from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "housecov.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import housecov.users.signals  # noqa F401
        except ImportError:
            pass
