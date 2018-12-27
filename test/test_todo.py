import json


def test_get_collection_default(client):
    r = client.get('/todo/').json
    assert 0 == r['status_code']
    assert 'test todo1' == r['data']['items'][0]['title']
    assert 1 == r['data']['items'][0]['id']
    assert r['data']['_meta']['current_page'] == 1
    assert r['data']['_meta']['next_page'] == 2
    assert len(r['data']['items']) == 10


def test_get_collections_page_2(client):
    r = client.get('/todo?page=2&per_page=10').json
    assert len(r['data']['items']) == 10


def test_get_by_id_ok(client):
    r = client.get('/todo/2').json
    assert r['data']['title'] == 'test todo2'
    assert r['data']['id'] == 2


def test_get_by_id_none(client):
    r = client.get('/todo/31').json
    assert r['status_code'] == 1


def test_update_one(client):
    r = client.post('/todo/1', data=json.dumps(dict(title='update')), content_type='application/json').json
    assert r['status_code'] == 0
    r = client.get('/todo/1').json
    assert r['data']['title'] == 'update'


def test_add_one_missing_field(client):
    r = client.post('/todo', data=json.dumps(dict(titl='')), content_type='application/json')
    assert b'Missing data for required field.' in r.data


def test_update_one_unknown_field(client):
    r = client.post('/todo/1', data=json.dumps(dict(tit='')), content_type='application/json')
    assert b'Unknown field.' in r.data


def test_add_one(client):
    r = client.post(
        '/todo',
        data=json.dumps(dict(title='add at test')),
        content_type='application/json'
    ).json
    assert r['status_code'] == 0
    r = client.get('/todo/' + str(r['data']['id'])).json
    assert r['data']['title'] == 'add at test'


def test_delete_success(client):
    r = client.delete('/todo/2').json
    assert r['status_code'] == 0
    r = client.get('/todo/2').json
    assert r['status_code'] == 1
