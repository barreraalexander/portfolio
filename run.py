from website import create_app
from website.config import settings

app = create_app()

if __name__=='__main__':
    app.run(debug=settings.DEBUG, port=settings.PORT)
