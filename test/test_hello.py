def test_hello(client):
    r = client.get('/')
    assert 'Hello World from container!' in r.data.decode()
