from flask import request, Response, Blueprint
from ..services.youtube import YoutubeStream

play_bp = Blueprint("play", __name__)

@play_bp.route("/play", methods=['GET'])
def play():
    url = request.args.get('url')
    if not url:
        return "Missing 'url' parameter", 400

    audio_url = YoutubeStream().get_audio_url(url)
    if audio_url.isValid():
        return Response(audio_url.generate_audio(), content_type="audio/mpeg")
    return f"Internal error", 500

