from pytest_factoryboy import register

from .factories import EmployerFactory, JobFactory, TalentFactory

register(TalentFactory)
register(EmployerFactory)
register(JobFactory)
