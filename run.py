# run.py

from app import create_app
from comparison import compare_memory_usage
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
