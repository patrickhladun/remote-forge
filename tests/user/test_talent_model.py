import pytest

pytestmark = pytest.mark.django_db

class TestTalentModel:
    def test_create_talent(self, talent_factory):
        """Test creating a new talent object."""
        talent = talent_factory(first_name="Patrick", last_name="Hladun")
        assert talent.id is not None

    def test_talent_str_return(self, talent_factory):
        """Test the string representation of a talent object."""
        talent = talent_factory()
        assert talent.__str__() == talent.user.username
        