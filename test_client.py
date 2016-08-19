import mock
from unittest import TestCase
import client


class TestClient(TestCase):
    @mock.patch('requests.request')
    def test_get_example(self, mock_request):
        mocked_response = mock.Mock()
        mocked_response.status_code = 200
        expected_dict = {"example": "foo"}
        mocked_response.json.return_value = expected_dict
        mock_request.return_value = mocked_response
        response = client.get_example()
        self.assertEqual(response.json(), expected_dict)
