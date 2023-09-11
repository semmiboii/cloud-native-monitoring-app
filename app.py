import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    cpu_util = psutil.cpu_percent()
    mem_util = psutil.virtual_memory().percent
    Message = None
    if cpu_util > 80 or mem_util > 80:
        Message = "High CPU or High Memory Utilization Detected. Please Scale Up"
    return render_template(
        "index.html", cpu_util=cpu_util, mem_util=mem_util, message=Message
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
