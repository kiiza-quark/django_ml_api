from django.apps import AppConfig
import os
import joblib
from django.apps import AppConfig
from django.conf import settings

class MonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'



class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "DecisionTreeModel.joblib")
    model = joblib.load(MODEL_FILE)
