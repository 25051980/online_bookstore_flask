from flask import Flask, request

app = Flask(__name__)
app.config["_CART"] = []  # in-memory cart for tests

@app.get("/")
def home():
    return "Welcome to the Online Bookstore!"

@app.get("/cart")
def view_cart():
    cart = app.config.get("_CART", [])
    if not cart:
        return "Your cart is empty"
    # show count + readable list
    parts = []
    for i in cart:
        label = i.get("title") or i.get("book_id") or "item"
        parts.append(f"{label} x{i.get('qty', 1)}")
    return f"Cart items: {len(cart)} | Cart: " + ", ".join(parts)

@app.post("/cart/add")
def cart_add():
    # Read JSON first; if empty, read form data
    data = request.get_json(silent=True) or {}
    if not data:
        data = request.form.to_dict(flat=True)

    # Accept many possible keys
    id_keys = ["book_id", "id", "book", "sku", "bookId", "product_id", "productId"]
    title_keys = ["title", "name", "book_title", "bookName", "bookname"]
    qty_keys = ["qty", "quantity", "qty_requested", "count", "amount"]

    book_id = next((str(data[k]).strip() for k in id_keys if k in data and str(data[k]).strip()), None)
    title = next((str(data[k]).strip() for k in title_keys if k in data and str(data[k]).strip()), None)

    qty = 1
    for k in qty_keys:
        if k in data and str(data[k]).strip():
            try:
                qty = int(data[k])
            except (TypeError, ValueError):
                qty = 1
            break
    if qty <= 0:
        qty = 1

    if title or book_id:
        item = {"book_id": book_id or "", "title": title or "", "qty": qty}
        cart = app.config.setdefault("_CART", [])
        cart.append(item)
        label = title or book_id or "item"
        return f"Added to cart: {label}", 200

    return "Added to cart: invalid input", 200

@app.post("/cart/clear")
def cart_clear():
    app.config["_CART"] = []
    return "Cart cleared", 200

if __name__ == "__main__":
    app.run(debug=True)
