import contextlib
import sentry_sdk


@contextlib.contextmanager
def capture_exceptions():
    try:
        yield
    except Exception as e:
        sentry_sdk.capture_exception(e)
        # Optionally, you can choose to raise the exception here
        # raise e
