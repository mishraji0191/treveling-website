from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

PHOTO_FOLDER = os.path.join('static', 'photos')
COVER_PHOTO = "vaishnodevi.jpg.jpg"   # your cover photo name

@app.route("/")
def index():
    photos = os.listdir(PHOTO_FOLDER)

    # Remove cover photo from the list so it doesn't repeat
    if COVER_PHOTO in photos:
        photos.remove(COVER_PHOTO)

    return render_template("index.html", cover=COVER_PHOTO, photos=photos)

if __name__ == "__main__":
    app.run(debug=True)
