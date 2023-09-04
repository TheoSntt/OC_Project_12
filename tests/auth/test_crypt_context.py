from auth.crypt_context import cryptcontext


def test_should_return_params():
    cfg = cryptcontext.to_string()
    assert "schemes = argon2" in cfg
    assert "argon2__memory_cost = 131072" in cfg
    assert "argon2__parallelism = 4" in cfg
    assert "argon2__rounds = 15" in cfg
