from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView

from .serializers import RegistrationSerializer


USER_MODEL = get_user_model()


class RegistrationView(CreateAPIView):
    model = USER_MODEL
    serializer_class = RegistrationSerializer

