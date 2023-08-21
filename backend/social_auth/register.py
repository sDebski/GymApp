from django.contrib.auth import authenticate
from users.models import User
import os
from rest_framework.exceptions import AuthenticationFailed
from decouple import config


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)
    print(config("SOCIAL_SECRET"), "SOCIAL_SECRET decouple")
    print(os.environ.get("SOCIAL_SECRET"), "SOCIAL_SECRET os")

    if filtered_user_by_email.exists():
        if provider == filtered_user_by_email[0].auth_provider:
            registered_user = authenticate(
                email=email, password=os.environ.get("SOCIAL_SECRET")
            )

            return {
                "username": registered_user.name,
                "email": registered_user.email,
                "tokens": registered_user.tokens(),
            }

        else:
            raise AuthenticationFailed(
                detail="Please continue your login using "
                + filtered_user_by_email[0].auth_provider
            )

    else:
        user = {
            "first_name": name,
            "email": email,
            "password": os.environ.get("SOCIAL_SECRET"),
        }
        user = User.objects.create_user(**user)
        user.is_active = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(email=email, password=os.environ.get("SOCIAL_SECRET"))
        return {
            "email": new_user.email,
            "first_name": new_user.first_name,
            "tokens": new_user.tokens(),
        }
