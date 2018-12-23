import json


def test_all(client):
    r = client.get('/todo/').json
    assert 0 == r['status_code']
    assert 'test todo' == r['data'][0]['title']
    assert 1 == r['data'][0]['id']


def test_get_by_id_ok(client):
    r = client.get('/todo/2').json
    assert r['data']['title'] == 'test todo2'
    assert r['data']['id'] == 2


def test_get_by_id_none(client):
    r = client.get('/todo/3').json
    assert r['status_code'] == 1


def test_add_one(client):
    r = client.post('/todo/1', data=dict(title='update'), content_type='application/json').json
    assert r['status_code'] == 0

def test_delete_success(client):
    r = client.delete('/todo/2').json
    assert r['status_code'] == 0
