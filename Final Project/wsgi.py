from di_app import create_app, models, db, forms

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
