from dao.sentry_context_manager import capture_exceptions


def test_capture_exceptions_with_mock(mocker):
    sentry_capture_exception_mock = mocker.patch('sentry_sdk.capture_exception')

    with capture_exceptions():
        raise ValueError("Test exception")

    sentry_capture_exception_mock.assert_called_once()
