from flask import Flask, request, render_template
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
            status = "Finished Reading!! 🎉"
        else:
            status = "Still Reading!! 📖"
        return f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
<div class="container result-container">
<h1>Reading Tracker 📚🌸</h1>
<div class="result-card">
<h2>{name}</h2>
<p><b>Total Pages:</b> {pages}</p>
<p><b>Pages Read:</b> {read}</p>
<p><b>Pages Left:</b> {left}</p>
<p><b>Progress:</b> {progress:.2f}%</p>
<p><b>Status:</b> {status}</p>
<a href="/" class="btn">
Track Another Book ✨
</a>
</div>
</div>
</body>
</html>
"""
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True, port=5004)