from flask import Flask   # ← this line is required

print("Starting app.py...")  # sanity print

app = Flask(__name__)

@app.get("/")
def home():
    return "Welcome to the Online Bookstore!"

if __name__ == "__main__":
    print("Calling app.run(...)")  # sanity print
    app.run(debug=True)

