from google_ads_keywords_generator.cli import generate_cmd, single_cmd, batch_cmd
from .test_core import PRODUCTS_PATH, WORDS_PATH, CAMPAIGN_FOLDER, PRODUCTS_WORDS_PATH_PAIRS
from click.testing import CliRunner


runner = CliRunner()
COMMANDS = (generate_cmd, 'generate'), (single_cmd, 'single'), (batch_cmd, 'batch')


def test_show_help_if_command_without_args():
    for cmd_func, cmd_str in COMMANDS:
        result = runner.invoke(cmd_func)
        assert f"Try '{cmd_str} --help' for help" in result.output


def test_generate_with_invalid_products_or_words_path():
    for products_path, words_path in PRODUCTS_WORDS_PATH_PAIRS:
        result = runner.invoke(COMMANDS[0][0], ['-i', products_path, words_path, '-c', 'test'])
        assert result.exit_code == 2


def test_generate_with_none_output_path_and_check_return_data():
    result = runner.invoke(COMMANDS[0][0], ['-i', PRODUCTS_PATH, WORDS_PATH, '-c', 'test'])
    assert 'Ad Group' in result.output, 'INVALID RETURN DATA'


def test_single_run_with_invalid_folder_path():
    result = runner.invoke(COMMANDS[1][0], ['-i', 'INVALID_PATH'])
    assert result.exit_code == 2


def test_single_run_with_words_or_products_path_equal_reserved_output_path():
    for opt in '-w', '-p':
        result = runner.invoke(COMMANDS[1][0], ['-i', CAMPAIGN_FOLDER, opt, 'keywords.csv'])
        assert 'keyword.csv is RESERVED OUTPUT FILENAME' in result.output


def test_single_run_with_none_output_path_and_check_return_data():
    result = runner.invoke(COMMANDS[1][0], ['-i', CAMPAIGN_FOLDER, '-c', 'test', '-oS'])
    assert 'Ad Group' in result.output, 'INVALID RETURN DATA'
