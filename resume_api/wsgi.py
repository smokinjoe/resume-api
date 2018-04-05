from resume_api.app import create_app  # pragma: no cover

app = create_app()  # pragma: no cover

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
