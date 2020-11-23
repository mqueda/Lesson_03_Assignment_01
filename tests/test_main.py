"""
Module for implementing the unit tests
"""
from unittest.mock import patch
from signal_interpreter_server.main import main, init, ArgumentParser,\
    get_arguments
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.json_parser import LoadAndParse


class MockMainClass:
    """
    Class for the mock functionalities.
    """
    file_path = "file/path"


@patch.object(ArgumentParser, "parse_args", return_value=MockMainClass)
@patch.object(ArgumentParser, "add_argument")
def test_main_arguments(mock_add_argument, mock_parse_args):
    """
    Action : Test mocking parse arguments.
    Expected Results : No difference from normal application usage.
    Returns: N/A.
    """
    assert get_arguments() == MockMainClass
    mock_add_argument.assert_called_with('--file_path', required=True)
    mock_parse_args.assert_called_once()


@patch.object(signal_interpreter_app, "run")
@patch.object(LoadAndParse, "load_file")
@patch("signal_interpreter_server.main.get_arguments",
       return_value=MockMainClass)
def test_main_functions(mock_get_arguments, mock_load_file, mock_run):
    """
    Action : Test mocking signal interpretation.
    Expected Results : No difference from normal application usage.
    Returns: N/A.
    """
    main()
    mock_get_arguments.assert_called_once()
    mock_load_file.assert_called_with(MockMainClass.file_path)
    mock_run.assert_called_once()


@patch("signal_interpreter_server.main.main")
@patch("signal_interpreter_server.main.__name__", "__main__")
def test_init(mock_main):
    """
    Action : Test init call.
    Expected Results : Init correctly called.
    Returns: N/A.
    """
    init()
    mock_main.assert_called_once()
