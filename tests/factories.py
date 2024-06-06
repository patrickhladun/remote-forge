import factory

from apps.user.models import Talent, User


class UserTalentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    is_admin = False
    is_active = True
    is_staff = False
    is_superuser = False
    hide_email = False
    user_type = "talent"


class TalentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Talent

    id = factory.Faker("uuid4")
    user = factory.SubFactory(UserTalentFactory)
