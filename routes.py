# app/api/routes.py

from flask import Blueprint, request, jsonify
from app.cache.cache_manager import LRUCache

api_bp = Blueprint('api', __name__)

@api_bp.route('/simulate-cache', methods=['POST'])
def simulate_cache():
    data = request.get_json()
    sequence = data.get('pages', [])
    capacity = data.get('capacity', 3)

    cache = LRUCache(capacity)
    result = cache.simulate(sequence)

    return jsonify({
        'status': 'success',
        'result': result
    })
