from django.db import migrations
from app.user.models import CustomUser

class Migration(migrations.Migration):
  def seed_data(apps, schema_editor):
    user = CustomUser(name="nym",
                      email="nym673@gmail.com",
                      is_staff=True,
                      is_superuser=True,
                      Category="superuser",
                    )
    user.set_password("nym@1234")
    user.save()

  dependencies = [
  
  ]

  operations = [
    migrations.RunPython(seed_data),
  ]
