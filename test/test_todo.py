def test_all(client):
    r = client.get('/todo/all').json
    assert 0 == r['status_code']
