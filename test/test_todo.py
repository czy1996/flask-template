def test_all(client):
    r = client.get('/todo/').json
    assert 0 == r['status_code']
    assert 'test todo' == r['data'][0]['title']
    assert 1 == r['data'][0]['id']


def test_get_by_id(client):
    r = client.get('/todo/2').json
    assert r['data']['title'] == 'test todo2'
    assert r['data']['id'] == 2
