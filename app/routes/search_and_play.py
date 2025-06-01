from flask import Blueprint, Response, request
from ..services.youtube import YoutubeStream

search_and_play_bp = Blueprint("search_and_play", __name__)

@search_and_play_bp.route("/search-and-play", methods=['GET'])
def search_and_play():
    try:
        query = request.args.get('query')
        if not query:
            return "Missing 'query' parameter", 400

        ytstream = YoutubeStream()
        data = ytstream.searchVideo(query, 1)

        if len(data) > 0:
            audio_url = ytstream.get_audio_url(data[0]["url"])
            if audio_url.isValid():
                return Response(audio_url.generate_audio(), content_type="audio/mpeg")
            return f"Internal error", 500
    except Exception as e:
        return f"ERROR: {e}", 500 

