
import users


def substitute_func(username):
    return '[{"login": "fitoelizond0"},{"login": "nicolasleal57034"},{"login": "puchee99"},{"login": "pgraciae"}]'


def test_get_follower_names_returns_name_list(monkeypatch):
    monkeypatch.setattr(users, 'get_user_followers', substitute_func)
    assert 'nicolasleal57034' in users.get_follower_names('aleconwifi')