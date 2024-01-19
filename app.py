from flask import Flask, request, jsonify, render_template
from analyze import read_image, analyze_image

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html")


# API at /api/v1/analysis/
@app.route("/api/v1/analysis/", methods=["GET"])
def analysis():
    # Try to get the URI from the JSON
    try:
        get_json = request.get_json()
        image_uri = get_json["uri"]
        analysis_type = get_json.get("type", "text")
    except:
        return jsonify({"error": "Missing URI in JSON"}), 400

    # Try to get the text from the image
    try:
        if analysis_type == "text":
            res = read_image(image_uri)
        else:
            res = analyze_image(image_uri, analysis_type)

        return jsonify({"result": res}), 200
    except Exception as e:
        return ({"error": "failed to analyze image", "details": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
