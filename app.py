from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Tehran, Iran',
        'salary': '$10,000'
    },
    {
        'id': 2,
        'title': 'Network Specialist',
        'location': 'Guilan, Iran',
        'salary': '$20,000'
    },
    {
        'id': 3,
        'title': 'Backend Engineer',
        'location': 'Esfahan, Iran',
        'salary': '$20,000'
    },
    {
        'id': 4,
        'title': 'Frontend Engineer',
        'location': 'London, England',
        'salary': '$20,000'
    }
]
@app.route("/")
def hello_world():
    return render_template("index.html", jobs=JOBS, company_name='Binazir')

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)