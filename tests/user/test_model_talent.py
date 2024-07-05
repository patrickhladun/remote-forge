import pytest

from apps.user.models import User
from tests.factories import TalentFactory, UserTalentFactory

pytestmark = pytest.mark.django_db


class TestTalentModel:
    def test_create_talent(self, talent_factory):
        talent_user = UserTalentFactory()
        talent = TalentFactory(user=talent_user)

        assert talent.id is not None

    def test_talent_str_return(self, talent_factory):
        talent_user = UserTalentFactory()
        talent = TalentFactory(user=talent_user)

        assert talent.__str__() == talent.user.username
