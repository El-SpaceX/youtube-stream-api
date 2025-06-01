from flask import Blueprint, request
from ..services.youtube import YoutubeStream

search_bp = Blueprint("search", __name__)

@search_bp.route("/search", methods=['GET'])
def search():
    try:
        query = request.args.get('query')
        if not query:
            return "Missing 'query' parameter", 400

        max_result = request.args.get('max_result')
        if not max_result:
            max_result = 5

        ytstream = YoutubeStream()
        data = ytstream.searchVideo(query, max_result)
        return data, 200    
    except Exception as e:
        return f"ERROR: {e}", 500 

