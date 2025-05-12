from flask import Flask, jsonify
from simulate_before import simulate_before
from simulate_after import simulate_after

app = Flask(__name__)

@app.route('/api/comparison', methods=['GET'])
def compare_memory_usage():
    page_faults_before = simulate_before()
    page_faults_after = simulate_after()
    
    comparison_data = {
        "before_optimization": page_faults_before,
        "after_optimization": page_faults_after
    }
    
    return jsonify(comparison_data)

def compare_performance(before,after):
    return{
        "before_ratio": before,
        "after_ratio": after,
        "improvement": round(((after - before)/ before)* 100, 2)
    }

if __name__ == '__main__':
    app.run(debug=True)
