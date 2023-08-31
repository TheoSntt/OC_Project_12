import sentry_sdk
import os
import logging
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


class SentryManager:
    _initialized = False

    @classmethod
    def initialize(cls):
        if not cls._initialized:
            sentry_sdk.init(
                dsn=os.environ.get("SENTRY_DSN"),
                integrations=[SqlalchemyIntegration(),
                              LoggingIntegration(level=logging.INFO, event_level=logging.INFO)]
            )
            cls._initialized = True
