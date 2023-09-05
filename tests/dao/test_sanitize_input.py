from dao.sanitize_input import sanitize_input


def test_sanitize_should_not_change():
    input = "This is a, pretty, normal ! input23"
    assert sanitize_input(input) == input


def test_sanitize_should_remove_tag():
    input = "This is a <script>pretty malicious looking</script> input"
    assert sanitize_input(input) == "This is a pretty malicious looking input"


def test_sanitize_should_remove_SQL():
    input = "This input looks like it has SQL in it : / * ; -- '"
    assert sanitize_input(input) == "This input looks like it has SQL in it :     "
