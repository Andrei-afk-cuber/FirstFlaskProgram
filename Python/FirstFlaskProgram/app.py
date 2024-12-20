import json
from flask import Flask

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf-8') as file:
    candidates = json.load(file)

print(candidates)

@app.route('/')
def index():
    candidates_list = "\n".join([f"{candidate['name']} - {candidate['position']} - {candidate['skills']}"
                                 for candidate in candidates])
    print(candidates_list)
    return f"<pre>{candidates_list}</pre>"

@app.route('/candidate/<int:candidate_id>')
def candidate_page(candidate_id):
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            candidate = candidate
            return (f"<img src={candidate['picture']}>\n"
                f"<pre>name: {candidate['name']}\ncandidate position: {candidate['position']}\nabilities: {candidate['skills']}</pre>")

@app.route('/skill/<skill>')
def candidate_skill(skill):
    for candidate in candidates:
        if skill in candidate['skills']:
            return f"<pre>name: {candidate['name']}\ncandidate position: {candidate['position']}\nabilities: {candidate['skills']}</pre>"

app.run()
print(candidates)