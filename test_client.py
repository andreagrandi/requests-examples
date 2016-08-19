import mock
import responses
from unittest import TestCase
import client


class TestClient(TestCase):
    @mock.patch('requests.get')
    def test_get_example_mock(self, mock_request):
        mocked_response = mock.Mock()
        mocked_response.status_code = 200
        expected_dict = {"example": "foo"}
        mocked_response.json.return_value = expected_dict
        mock_request.return_value = mocked_response
        response = client.get_example()
        self.assertEqual(response, expected_dict)

    @responses.activate
    def test_get_example_responses(self):
        responses.add(responses.GET, 'https://httpbin.org/get',
                      body='{"example": "foo"}', status=200,
                      content_type='application/json')

        response = client.get_example()
        self.assertEqual(response, {"example": "foo"})
