"""
Module for implementing the routes
"""
from flask import Flask
from flask import request
from flask import jsonify
from signal_interpreter_server.json_parser import LoadAndParse


signal_interpreter_app = Flask(__name__)
jsonparser = LoadAndParse()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """
    Action : Make the received code interpretation.
    Expected Results : Proper code interpretation.
    Returns: jsonfy_data.
    """
    data = request.get_json()
    print(data)
    parsed_data = jsonparser.return_signal_by_title(data['service'])
    jsonfy_data = jsonify(parsed_data)
    return jsonfy_data
