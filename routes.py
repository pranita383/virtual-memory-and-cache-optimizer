from flask import Blueprint, render_template, jsonify
from app.cache_manager import CacheManager
from app.simulate_before import simulate_before
from app.simulate_after import simulate_after
from app.performance_logger import log_performance
from app.comparison import compare_performance

routes = Blueprint('routes', __name__)

# Homepage
@routes.route('/')
def index():
    return render_template('index.html')

# Run simulation before optimization
@routes.route('/simulate-before')
def simulate_before_route():
    before_ratio = simulate_before()
    log_performance(before_ratio, "Before Optimization")
    return jsonify({"status": "success", "hit_ratio": before_ratio})

# Run simulation after optimization
@routes.route('/simulate-after')
def simulate_after_route():
    after_ratio = simulate_after()
    log_performance(after_ratio, "After Optimization")
    return jsonify({"status": "success", "hit_ratio": after_ratio})

# Compare both results
@routes.route('/compare')
def compare():
    try:
        with open('performance_log.txt', 'r') as f:
            lines = f.readlines()

        before_line = next((line for line in lines if "Before Optimization" in line), None)
        after_line = next((line for line in lines if "After Optimization" in line), None)

        if before_line and after_line:
            before_ratio = float(before_line.split("Ratio: ")[1].strip())
            after_ratio = float(after_line.split("Ratio: ")[1].strip())

            result = compare_performance(before_ratio, after_ratio)

            return render_template('compare.html', result=result)
        else:
            return "Run both simulations first.", 400

    except Exception as e:
        return f"Error: {str(e)}", 500



