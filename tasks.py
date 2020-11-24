'''
tasks.py
'''
import subprocess
from invoke import task


@task  # pylint: disable=undefined-variable
def style(_):
    '''
    style method
    :return:
    '''
    cmd = f"pycodestyle signal_interpreter_server"
    subprocess.call(cmd, shell=True)


@task  # pylint: disable=undefined-variable
def lint_sources(_):
    '''
    lint method
    :return:
    '''
    cmd = f"pylint signal_interpreter_server"
    subprocess.call(cmd, shell=True)


@task  # pylint: disable=undefined-variable
def lint_tests(_):
    '''
    lint method
    :return:
    '''
    cmd = f"pylint tests"
    subprocess.call(cmd, shell=True)


@task  # pylint: disable=undefined-variable
def unit_test(_):
    '''
    unit_test method
    :return:
    '''
    cmd = f"pytest tests " \
          f"--cov signal_interpreter_server " \
          f"--cov-config=coveragerc"
    subprocess.call(cmd, shell=True)
