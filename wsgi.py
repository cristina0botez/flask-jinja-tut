from flask_jinja_tut import create_app


app = create_app()

# To start server from code
# app.run(host='0.0.0.0', port=8080, debug=True)
# > python wsgi.py

# To start using gunicorn
# > python -m gunicorn --config=gunicorn.conf.py
