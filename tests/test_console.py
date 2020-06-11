import click.testing
import pytest

from case_converter import console

@pytest.fixture
def runner():
    return click.testing.CliRunner()

@pytest.mark.parametrize("inputString, expectedString, from_, to", [
    ("def myCamelFunc():\n",  "def my_camel_func():\n", 'camel', 'snake'),
    ("def myCamelFunc():\n",  "def my-camel-func():\n", 'camel', 'kebab'),
    ("def my_camel_func():\n", "def myCamelFunc():\n", 'snake', 'camel'),
    ("def my_camel_func():\n", "def my-camel-func():\n", 'snake', 'kebab'),
])
def test_different_files(inputString, expectedString, from_, to, runner):
    with runner.isolated_filesystem():
        with open('temp.txt', 'w') as f:
            f.write(inputString)
        result = runner.invoke(console.main,
                               ['temp.txt',
                                '--from', from_,
                                '--to', to,
                                '-o', 'tempOut.txt'])
        assert result.exit_code == 0
        with open('tempOut.txt', 'r') as f:
            assert f.read() == expectedString

@pytest.mark.parametrize("inputString, expectedString, from_, to", [
    ("def myCamelFunc():\n",  "def my_camel_func():\n", 'camel', 'snake'),
    ("def myCamelFunc():\n",  "def my-camel-func():\n", 'camel', 'kebab'),
    ("def my_camel_func():\n", "def myCamelFunc():\n", 'snake', 'camel'),
    ("def my_camel_func():\n", "def my-camel-func():\n", 'snake', 'kebab'),
])
def test_same_files(inputString, expectedString, from_, to, runner):
    with runner.isolated_filesystem():
        with open('temp.txt', 'w') as f:
            f.write(inputString)
        result = runner.invoke(console.main,
                               ['temp.txt',
                                '--from', from_,
                                '--to', to,
                                '-o', 'temp.txt'])
        assert result.exit_code == 0
        with open('temp.txt', 'r') as f:
            assert f.read() == expectedString
