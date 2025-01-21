from django.apps import AppConfig

# Define a configuration class for the 'about' app
class AboutConfig(AppConfig):
    # Specify the default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the app
    name = 'about'
