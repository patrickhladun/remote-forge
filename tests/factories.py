from random import choice

import factory
from factory import Faker, LazyFunction, SubFactory
from factory.django import DjangoModelFactory

from apps.job.models import Job
from apps.user.models import Employer, Talent, User

job_titles = [
    "Software Engineer",
    "Data Scientist",
    "DevOps Engineer",
    "Frontend Developer",
    "Backend Developer",
    "Full Stack Developer",
    "Mobile App Developer",
    "Cloud Engineer",
    "Cybersecurity Analyst",
    "IT Project Manager",
]


class UserTalentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = Faker("email")
    username = Faker("user_name")
    password = "pbkdf2_sha256$720000$d9nahLFNnDl5Yr9A3ewMgx$igf567La3i6LuPJRwaGH05bRs8CHgq8os+4nYh/PbdQ="
    is_admin = False
    is_active = True
    is_staff = False
    is_superuser = False
    user_type = "talent"


class TalentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Talent

    id = Faker("uuid4")
    user = factory.SubFactory(UserTalentFactory)
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    phone = Faker("phone_number")
    city = Faker("city")
    country = Faker("country")
    title = Faker("job")
    image = "media/talent/profile/profile.jpg"
    bio = Faker("paragraph")
    resume = "media/talent/resumes/resume.pdf"
    website = Faker("url")
    social = [
        {"site": "linkedin", "url": "https://www.linkedin.com/"},
    ]
    experience = [
        {
            "company_name": "Tech Innovations Inc.",
            "position": "Software Engineer",
            "start_date": "2019-07-01",
            "end_date": None,
            "still_on": True,
            "responsibilities": "Designed and implemented scalable software solutions, participated in code reviews and technical discussions, and collaborated with product and design teams to deliver user-centric features.",
        },
        {
            "company_name": "Startup XYZ",
            "position": "Full Stack Developer",
            "start_date": "2018-01-15",
            "end_date": "2019-06-30",
            "still_on": False,
            "responsibilities": "Developed and maintained web applications, designed and implemented database schemas, and optimized application performance for scalability.",
        },
        {
            "company_name": "Freelance Projects",
            "position": "Freelance Developer",
            "start_date": "2016-05-01",
            "end_date": "2017-12-31",
            "still_on": False,
            "responsibilities": "Worked on various freelance projects, developed custom web solutions, and provided technical consultation to clients.",
        },
    ]
    education = [
        {
            "level": "Udacity Nanodegree in Full Stack Web Development",
            "status": "Completed",
            "start_date": "2017-09-01",
            "end_date": "2018-06-30",
            "still_on": False,
            "expected_end_date": "",
        },
        {
            "level": "Udemy Course: Advanced JavaScript",
            "status": "Completed",
            "start_date": "2016-03-01",
            "end_date": "2016-06-30",
            "still_on": False,
            "expected_end_date": "",
        },
        {
            "level": "Development Diploma in Web Development",
            "status": "Completed",
            "start_date": "2015-01-01",
            "end_date": "2015-12-31",
            "still_on": False,
            "expected_end_date": "",
        },
    ]
    interests = "Open Source Projects, Cloud Computing, Machine Learning"
    skills = ["JavaScript", "HTML", "CSS", "Python"]
    created_at = Faker("date_time_this_decade")
    updated_at = Faker("date_time_this_decade")
    is_published = True


class UserEmployerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = Faker("email")
    username = Faker("user_name")
    password = "pbkdf2_sha256$720000$d9nahLFNnDl5Yr9A3ewMgx$igf567La3i6LuPJRwaGH05bRs8CHgq8os+4nYh/PbdQ="
    is_admin = False
    is_active = True
    is_staff = False
    is_superuser = False
    user_type = "employer"


class EmployerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employer

    id = Faker("uuid4")
    user = factory.SubFactory(UserEmployerFactory)
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    phone = Faker("phone_number")
    company = Faker("company")
    about = Faker("paragraph", nb_sentences=5)
    image = "media/employer/profile/profile.jpg"
    website = Faker("url")
    social = [{"site": "twitter", "url": "https://twitter.com/"}]
    is_published = True


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job

    id = Faker("uuid4")
    user = factory.SubFactory(UserEmployerFactory)
    title = LazyFunction(lambda: choice(job_titles))
    city = Faker("city")
    country = Faker("country")
    salary = Faker("random_int", min=30000, max=100000)
    schedule = Faker("random_element", elements=["Full-time", "Part-time", "Contract"])
    details = [
        {
            "heading": "Job Description",
            "content": "We are seeking a skilled DevOps Engineer to manage our deployment pipelines and ensure the reliability of our infrastructure. You will work closely with the development team to streamline our CI/CD processes.",
        },
        {
            "heading": "Requirements",
            "content": "Bachelor's degree in Computer Science or related field. 3-4 years of experience as a DevOps Engineer. Proficiency in tools like Docker, Kubernetes, Jenkins, and cloud platforms such as AWS or Azure. Strong scripting skills in Bash, Python, or similar languages.",
        },
        {
            "heading": "Benefits",
            "content": "Competitive salary and benefits package. Remote work options. Health and wellness programs. Opportunities for career advancement.",
        },
    ]
    created_at = Faker("date_time_this_year")
    updated_at = Faker("date_time_this_year")
    is_published = True
