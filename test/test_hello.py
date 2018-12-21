def test_hello(client):
    r = client.get('/')
    assert 'Hello World from container!' in r.data.decode()
    print(r.data.decode())
    assert 'todo' in r.data.decode()
