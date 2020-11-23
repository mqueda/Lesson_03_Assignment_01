"""
Module for implementing the main file
"""
from argparse import ArgumentParser
from signal_interpreter_server.routes import signal_interpreter_app, jsonparser


# Remeber to set the parameter " --file_path ..\signal_database.json "

def get_arguments():
    """
    Action : Load the specified arguments.
    Expected Results : Proper arguments load.
    Returns: parser.parse_args().
    """
    parser = ArgumentParser()
    parser.add_argument('--file_path', required=True)
    return parser.parse_args()


def main():
    """
    Action : Start the server application.
    Expected Results : Proper file load.
    Returns: N/A.
    """
    args = get_arguments()
    jsonparser.load_file(args.file_path)
    signal_interpreter_app.run()


def init():
    """
    Sets the init values
    """
    if __name__ == '__main__':
        main()


init()
