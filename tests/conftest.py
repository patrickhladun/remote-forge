import uuid

import pytest
from pytest_factoryboy import register

from .factories import (
    EmployerFactory,
    JobFactory,
    TalentFactory,
    UserEmployerFactory,
    UserTalentFactory,
)

register(TalentFactory)
register(EmployerFactory)
register(JobFactory)


@pytest.fixture
def test_data_jobs():
    employer_user_1 = UserEmployerFactory()
    employer_1 = EmployerFactory(user=employer_user_1, city="Dublin")

    employer_user_2 = UserEmployerFactory()
    employer_2 = EmployerFactory(user=employer_user_2, city="Galway")

    employer_user_3 = UserEmployerFactory()
    employer_3 = EmployerFactory(user=employer_user_3, city="Krakow")

    job1 = JobFactory(
        id=uuid.uuid4(),
        user=employer_user_1,
        title="DevOps Engineer",
        city="Dublin",
        country="Ireland",
        salary="60000",
        schedule="full-time",
        is_published=True,
    )
    job2 = JobFactory(
        id=uuid.uuid4(),
        user=employer_user_2,
        title="Frontend Developer",
        city="Galway",
        country="Ireland",
        salary="60000",
        schedule="full-time",
        is_published=True,
    )
    job3 = JobFactory(
        id=uuid.uuid4(),
        user=employer_user_3,
        title="Backend Developer",
        city="Warsaw",
        country="Poland",
        salary="60000",
        schedule="full-time",
        is_published=True,
    )
    job4 = JobFactory(
        id=uuid.uuid4(),
        user=employer_user_3,
        title="Backend Developer",
        city="Wroclaw",
        country="Poland",
        salary="60000",
        schedule="full-time",
        is_published=False,
    )

    return job1, job2, job3, job4


@pytest.fixture
def test_data_single_job():
    employer_user = UserEmployerFactory()
    employer = EmployerFactory(user=employer_user, city="Dublin")

    job = JobFactory(
        id=uuid.uuid4(),
        user=employer_user,
        title="DevOps Engineer",
        city="Dublin",
        country="Ireland",
        salary="60000",
        schedule="full-time",
        is_published=True,
    )

    return job
