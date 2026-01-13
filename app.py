from flask import Flask, render_template, request
from study_assistant import generate_study_content, get_mcqs

app = Flask(__name__)


# Home page - Study content

@app.route("/", methods=["GET", "POST"])
def index():
    topic = ""
    result = ""  # Always defined

    if request.method == "POST":
        topic = request.form.get("topic")
        result = generate_study_content(topic)

    return render_template(
        "index.html",
        topic=topic,
        result=result
    )


# Take Test page

@app.route("/test", methods=["GET", "POST"])
def take_test():
    topic = ""
    mcqs = []
    score = None

    if request.method == "POST":
        topic = request.form.get("topic")
        mcqs = get_mcqs(topic)

        if "answers" in request.form:
            user_answers = request.form.getlist("answers")
            correct_answers = [mcq["answer"] for mcq in mcqs]
            score = sum([1 for ua, ca in zip(user_answers, correct_answers) if ua == ca])

    return render_template(
        "test.html",
        topic=topic,
        mcqs=mcqs,
        score=score
    )


# Run the app

if __name__ == "__main__":
    app.run(debug=True)
