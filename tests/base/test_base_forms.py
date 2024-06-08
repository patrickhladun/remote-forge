import pytest

from apps.base.forms import ContactForm, JobSearchForm


@pytest.mark.django_db
class TestJobSearchForm:

    def test_form_initial_state(self):
        form = JobSearchForm()
        assert not form.is_bound

    def test_form_with_valid_data(self):
        form_data = {"keyword": "developer", "location": "dublin"}
        form = JobSearchForm(data=form_data)

        assert form.is_bound
        assert form.is_valid()
        assert form.cleaned_data["keyword"] == "developer"
        assert form.cleaned_data["location"] == "dublin"

    def test_form_with_empty_data(self):
        form_data = {}
        form = JobSearchForm(data=form_data)

        assert form.is_bound
        assert form.is_valid()
        assert "keyword" not in form.cleaned_data or form.cleaned_data["keyword"] == ""
        assert (
            "location" not in form.cleaned_data or form.cleaned_data["location"] == ""
        )


@pytest.mark.django_db
class TestContactForm:

    def test_form_initial_state(self):
        form = ContactForm()
        assert not form.is_bound

    def test_form_with_valid_data(self):
        form_data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "subject": "Hello",
            "message": "Hello, World!",
        }
        form = ContactForm(data=form_data)

        assert form.is_bound
        assert form.is_valid()
        assert form.cleaned_data["name"] == "John Doe"
        assert form.cleaned_data["email"] == "johndoe@example.com"
        assert form.cleaned_data["subject"] == "Hello"
        assert form.cleaned_data["message"] == "Hello, World!"

    def test_form_with_empty_data(self):
        form_data = {}
        form = ContactForm(data=form_data)

        assert form.is_bound
        assert not form.is_valid()
        assert "name" in form.errors
        assert "email" in form.errors
        assert "subject" in form.errors
        assert "message" in form.errors
        assert form.errors["name"] == ["This field is required."]
        assert form.errors["email"] == ["This field is required."]
        assert form.errors["subject"] == ["This field is required."]
        assert form.errors["message"] == ["This field is required."]

    def test_form_with_invalid_email(self):
        form_data = {
            "name": "John Doe",
            "email": "john.doe@example",
            "subject": "Hello",
            "message": "Hello, World!",
        }
        form = ContactForm(data=form_data)

        assert form.is_bound
        assert not form.is_valid()
        assert "email" in form.errors
        assert form.errors["email"] == ["Enter a valid email address."]
