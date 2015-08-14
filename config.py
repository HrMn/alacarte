# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/alacarte_db'
DATABASE_CONNECT_OPTIONS = {}

CATEGORIES_UPLOAD_PATH = 'app/static/'
ALLOWED_IMG_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"