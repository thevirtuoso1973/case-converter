import click.testing
import pytest

from case_converter import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

def test_files(runner):
    with runner.isolated_filesystem():
        with open('temp.txt', 'w') as f:
            f.write("def myCamelFunc():\n")
        result = runner.invoke(console.main,
                               ['temp.txt',
                                '--from', 'camel',
                                '--to', 'snake',
                                '-o', 'tempOut.txt'])
        assert result.exit_code == 0
        with open('tempOut.txt', 'r') as f:
            assert f.read() == "def my_camel_func():\n"

def test_same_file(runner):
    with runner.isolated_filesystem():
        with open('temp.txt', 'w') as f:
            f.write("def myCamelFunc():\n")
        result = runner.invoke(console.main,
                               ['temp.txt',
                                '--from', 'camel',
                                '--to', 'snake',
                                '-o', 'temp.txt'])
        assert result.exit_code == 0
        with open('temp.txt', 'r') as f:
            assert f.read() == "def my_camel_func():\n"
