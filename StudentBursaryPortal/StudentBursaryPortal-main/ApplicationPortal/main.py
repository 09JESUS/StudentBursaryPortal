# main.py
from website import create_app

app = create_app()  # Use the function from the website package

if __name__ == '__main__':
    app.run(debug=True)
