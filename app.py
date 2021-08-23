from website import create_app

if __name__ == "__main__":
    print('hello world')
    app = create_app()
    app.run(debug=True)
