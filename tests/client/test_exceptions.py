import json
import pytest

from scrapinghub import ScrapinghubAPIError
from scrapinghub.client.exceptions import wrap_http_errors


def test_wrap_http_error_json_decode_error():

    def test_method():
        return json.loads('bad json')

    method = wrap_http_errors(test_method)
    with pytest.raises(ScrapinghubAPIError) as excinfo:
        method()
    assert 'Error decoding server response' in str(excinfo.value)
