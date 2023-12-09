from flask import jsonify, render_template

from app import app
from app.models import ContentModel, ContentModelSchema
from app.util.main import get_source

@app.route("/")
def index():
    result = {
        "Bbc": get_source('bbc'),
        "Manga": get_source('toonily'),
        "Top Anime": get_source('aniwatch'),
        "Reddit Spacex": get_source('reddit_spacex'),
        "Reddit News": get_source('reddit_news'),
        "Verge": get_source('verge'),
        "TechCrunch": get_source('techcrunch'),
        "apple_insider": get_source("apple_insider"),
        "linux_today": get_source("linux_today"),
        "game_informer": get_source("game_informer")

    }

   
    return render_template('app/index.html', result=result)

@app.route("/db")
def database():
    try:
        contents = ContentModel.query.all()
        schema = ContentModelSchema(many=True)
        result = schema.dump(contents)

        if not result:
            return jsonify({"results": "No contents available in database."})
        return jsonify({"results":result})

    except Exception as e:
        raise e