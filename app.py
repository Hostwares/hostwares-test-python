from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'status': '🚀 Running on Hostwares!',
        'app_name': os.environ.get('APP_NAME', 'Hostwares Test Python'),
        'framework': 'Flask 3.0',
        'python_version': os.sys.version.split()[0],
        'environment': {
            'FLASK_ENV': os.environ.get('FLASK_ENV', 'production'),
            'DATABASE_URL': '✅ Connected' if os.environ.get('DATABASE_URL') else '❌ Not configured',
            'SECRET_KEY': '✅ Set' if os.environ.get('SECRET_KEY') else '❌ Not set',
            'REDIS_URL': '✅ Connected' if os.environ.get('REDIS_URL') else '❌ Not configured',
            'OPENAI_API_KEY': '✅ Set' if os.environ.get('OPENAI_API_KEY') else '❌ Not set',
        },
        'deployed_at': datetime.utcnow().isoformat() + 'Z'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
