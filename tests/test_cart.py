from http import HTTPStatus

def test_cart_empty(client):
    r = client.get("/cart")
    assert r.status_code == HTTPStatus.OK
    assert "Your cart is empty" in r.get_data(as_text=True)
