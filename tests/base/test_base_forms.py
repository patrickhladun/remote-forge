import pytest

from apps.base.forms import JobSearchForm


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
