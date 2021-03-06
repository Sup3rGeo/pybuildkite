from unittest.mock import Mock

from pybuildkite.organizations import Organizations

import pytest


class TestOrganizations:
    """
    Test functionality of the Jobs class
    """

    @pytest.fixture
    def fake_client(self):
        """
        Build a fake API client
        """
        return Mock(get=Mock())

    def test_Organizations(self, fake_client):
        """
        Test organization classes instances
        """
        org = Organizations(fake_client, "https://api.buildkite.com/v2/")
        assert org.client == fake_client
        assert org.path == "https://api.buildkite.com/v2/organizations/"

    def test_list_all(self, fake_client):
        """
        Test organization class 'list_all()'  Method
        """
        org = Organizations(fake_client, "https://api.buildkite.com/v2/")
        org.list_all()
        fake_client.get.assert_called_with(
            org.path, query_params={"page": 0}, with_pagination=False
        )

    def test_list_all_with_pagination(self, fake_client):
        """
        Test organization class 'list_all()'  Method with pagination
        """
        org = Organizations(fake_client, "https://api.buildkite.com/v2/")
        org.list_all(page=2, with_pagination=True)
        fake_client.get.assert_called_with(
            org.path, query_params={"page": 2}, with_pagination=True
        )

    def test_get_org(self, fake_client):
        """
        Test organization class 'get_org()' method
        """
        org = Organizations(fake_client, "https://api.buildkite.com/v2/")
        org.get_org("Test_org")
        fake_client.get.assert_called_with(org.path + "Test_org")
