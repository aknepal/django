import os
import sys
from league_project.wsgi import application

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "league_project.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()