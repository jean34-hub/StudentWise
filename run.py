from app import create_app

app = create_app()
application = app

if __name__ == "__main__":
    # use_reloader=False: avoids slow restarts when the venv folder is inside the project.
    app.run(host="127.0.0.1", port=5000, debug=True, use_reloader=False)
