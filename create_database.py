from authentication import db, create_app
db.create_all(app=create_app()) # passing create_app result so Flask-SQLAlchemy gets the configuration.