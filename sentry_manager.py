import sentry_sdk
import logging
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


class SentryManager:
    _initialized = False

    @classmethod
    def initialize(cls):
        if not cls._initialized:
            sentry_sdk.init(
                dsn="https://29d9ca69d09de82e860fe7c3ad4adf68@o4505794950660096.ingest.sentry.io/4505794953871360",
                integrations=[SqlalchemyIntegration(),
                              LoggingIntegration(level=logging.INFO, event_level=logging.INFO)]
            )
            cls._initialized = True
