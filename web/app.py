from flask import Flask, render_template, request
import sys
import os
import markdown

# allow import from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.orchestrator import run_pipeline

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        topic = request.form.get("topic")

        try:
            pipeline_output = run_pipeline(topic)

            # ✅ convert markdown → HTML
            result = {
                "research": markdown.markdown(pipeline_output["research"]),
                "summary": markdown.markdown(pipeline_output["summary"]),
                "final": markdown.markdown(pipeline_output["final"])
            }

        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)