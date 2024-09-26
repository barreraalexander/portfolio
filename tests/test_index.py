def test_index(client):
    res = client.get("/")
    assert res.status_code == 200

# def test_styles(client):
#     res = client.get("/styles")
#     assert res.status_code == 200


def test_404(client):
    res = client.get("/doesnotexist")
    assert res.status_code == 404

