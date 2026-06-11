from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["book"]
        pages = int(request.form["pages"])
        read = int(request.form["read"])

        if read > pages:
            return "<h1>Error! Pages read cannot be more than total pages.</h1>"

        left = pages - read
        progress = (read / pages) * 100

        if read == pages:
            status = "FINISHED 🎉"
        else:
            status = "STILL READING 📖"

        return f"""
        <h1>📚 Book Status Tracker</h1>

        <p><b>Book:</b> {name}</p>
        <p><b>Total Pages:</b> {pages}</p>
        <p><b>Pages Read:</b> {read}</p>
        <p><b>Pages Left:</b> {left}</p>
        <p><b>Progress:</b> {progress:.2f}%</p>
        <p><b>Status:</b> {status}</p>

        <br>
        <a href="/">Calculate Another Book</a>
        """

    return """
    <h1>📚 Book Status Tracker</h1>

    <form method="POST">

        <p>Book Name</p>
        <input type="text" name="book" required>

        <p>Total Pages</p>
        <input type="number" name="pages" required>

        <p>Pages Read</p>
        <input type="number" name="read" required>

        <br><br>

        <button type="submit">Calculate</button>

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5004)