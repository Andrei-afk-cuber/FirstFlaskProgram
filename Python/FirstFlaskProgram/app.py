import json
from flask import Flask

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf-8') as file:
    candidates = json.load(file)

print(candidates)

@app.route('/')
def index():
    candidates_list = "\n".join([f"{candidate['name']} - {candidate['candidate_position']} - {candidate['abilities']}"
                                 for candidate in candidates])
    print(candidates_list)
    return f"<pre>{candidates_list}</pre>"

@app.route('/candidate/<int:candidate_id>')
def candidate_page(candidate_id):
    candidate = candidates[candidate_id]
    if candidate_id == 0:
        image_path = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1MWm4Uc-yhWB5bkRg8r_Vy6ueABFtDb_qSA&s"
    elif candidate_id == 1:
        image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/ThatcherM.jpg/220px-ThatcherM.jpg"
    elif candidate_id == 2:
        image_path = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Joe_Biden_presidential_portrait.jpg/274px-Joe_Biden_presidential_portrait.jpg"

    return (f"<img src={image_path}>\n"
            f"<pre>name: {candidate['name']}\ncandidate position: {candidate['candidate_position']}\nabilities: {candidate['abilities']}</pre>")

@app.route('/skill/<skill>')
def candidate_skill(skill):
    for candidate in candidates:
        if skill in candidate['abilities']:
            return f"<pre>name: {candidate['name']}\ncandidate position: {candidate['candidate_position']}\nabilities: {candidate['abilities']}</pre>"

app.run()
print(candidates)