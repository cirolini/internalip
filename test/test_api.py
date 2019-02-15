import pytest

def test_health(client):
    assert b'ok' in client.get('/health').data

def test_list_all_internal(client):
    data = client.get('/list_all_internal').data
    with open('./internalip/internal_ip.txt', 'r') as f:
        for ip in f.read().strip().split("\n"):
            assert ip in data

def test_add_ip(client):
    assert b'success' in client.post("/add_ip/?ipaddr=127.0.0.2").data
    assert b'error' in client.post("/add_ip/?ipaddr=ip_invalido").data

def test_is_internal(client):
    assert b'True' in client.get("/is_internal/127.0.0.2").data
    assert b'False' in client.get("/is_internal/1.1.1.1").data
    assert b'error' in client.get("/is_internal/ip_invalido").data

def test_remove_ip(client):
    assert b'success' in client.post("/remove_ip/?ipaddr=127.0.0.1").data
    assert b'error' in client.post("/remove_ip/?ipaddr=ip_invalido").data
