import sentry_sdk
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration


class SentryManager:
    _initialized = False

    @classmethod
    def initialize(cls):
        if not cls._initialized:
            sentry_sdk.init(
                dsn="https://29d9ca69d09de82e860fe7c3ad4adf68@o4505794950660096.ingest.sentry.io/4505794953871360",
                integrations=[SqlalchemyIntegration()]
            )
            cls._initialized = True
