"""
Module for implementing the unit tests
"""
from unittest.mock import patch
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.json_parser import LoadAndParse


def test_correct_data():
    """
    Action : Test mocking server answer.
    Expected Results : No difference from normal application usage.
    Returns: N/A.
    """
    signal_interpreter_app.testing = True
    signal_interpreter_app_instance = signal_interpreter_app.test_client()
    with patch.object(
            LoadAndParse, "return_signal_by_title",
            return_value="Security Access")\
            as mock_return_signal_by_title:
        with signal_interpreter_app_instance as client:
            payload = {"service": "27"}
            response = client.post("/", json=payload)
            mock_return_signal_by_title.assert_called_with("27")
            assert response.get_json() == "Security Access"
