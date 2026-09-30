import os
import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "project": "Six Eyes",
        "runner": os.getenv("HOSTNAME", "local-dev")
    }), 200

@app.route('/metrics')
def system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    return jsonify({
        "cpu_percent": cpu_usage,
        "memory_total_mb": round(memory.total / (1024 * 1024), 2),
        "memory_used_percent": memory.percent
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
