from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    # Get storage usage
    disk_usage = psutil.disk_usage('/')
    storage_usage = disk_usage.percent
    # Read the temperature (in Celsius)
    temperature = psutil.sensors_temperatures().get('coretemp', [])[0].current if psutil.sensors_temperatures().get('coretemp') else None

    return jsonify(cpu_usage=cpu_usage, memory_usage=memory_usage, temperature=temperature, storage_usage=storage_usage)

if __name__ == '__main__':
    app.run(host='YOURIPHERE', port=5000, debug=True)

