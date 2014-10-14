from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

    # Code goes here


    
@app.route("/")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")# Change this as appropriate
    return hackbright_app.get_student_by_github(student_github)

if __name__ == "__main__":
    app.run(debug=True)

