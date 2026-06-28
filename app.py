from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    profile = {
        "name": "Yuki Minami",
        "title": "Aspiring Cloud Developer",
        "bio": "I build simple, useful web experiences and enjoy learning modern cloud tools.",
        "location": "City, Country",
        "email": "you@example.com",
        "github": "https://github.com/yourusername",
        "linkedin": "https://www.linkedin.com/in/yourusername",
    }
    projects = [
        {
            "name": "Azure Portfolio Site",
            "description": "A lightweight Flask portfolio site deployed to Azure App Service.",
        },
        {
            "name": "Automation Helper",
            "description": "A small Python tool that simplifies repetitive tasks for workshop attendees.",
        },
    ]
    return render_template("index.html", profile=profile, projects=projects)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
