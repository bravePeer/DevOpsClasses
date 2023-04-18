import requests

def test_sub():
    a = '3.0'
    b = '2.0'
    result = b'1.0'
    r = requests.get('http://localhost:8080/api/sub?a='+a+'&b='+b)
    assert r.status_code==200
    assert r.content== result

def test_mul():
    a = '3.0'
    b = '3.0'
    result = b'9.0'
    r = requests.get('http://localhost:8080/api/mul?a='+a+'&b='+b)
    assert r.status_code==200
    assert r.content== result

def test_div():
    a = '4.0'
    b = '2.0'
    result = b'2.0'
    r = requests.get('http://localhost:8080/api/div?a='+a+'&b='+b)
    assert r.status_code==200
    assert r.content== result

def test_div_by_0():
    a = '4'
    b = '0'
    r = requests.get('http://localhost:8080/api/div?a='+a+'&b='+b)
    assert r.status_code==400