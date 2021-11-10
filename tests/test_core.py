from google_ads_keywords_generator import generate, single_run
import pytest
import pandas as pd

# google_ads_keyword_generator/tests/test_campaign/products.txt',
# google_ads_keyword_generator/tests/test_campaign/words.txt',

PRODUCTS_PATH = 'tests/test_campaign/products.txt'
WORDS_PATH = 'tests/test_campaign/words.txt'
CAMPAIGN_FOLDER = 'tests/test_campaign'
PRODUCTS_WORDS_PATH_PAIRS = ('INVALID_PATH', WORDS_PATH), (PRODUCTS_PATH, 'INVALID_PATH')


def test_generate_with_invalid_products_and_word_path():
    for products_path, words_path in PRODUCTS_WORDS_PATH_PAIRS:
        with pytest.raises(FileNotFoundError) as e:
            generate(products_path=products_path,
                     words_path=words_path,
                     campaign_name='test')
        e.match('File INVALID_PATH not found')


def test_generate_with_none_output_path_for_valid_return_type():
    df = generate(products_path=PRODUCTS_PATH,
                  words_path=WORDS_PATH,
                  campaign_name='test',
                  output_path=None)
    assert isinstance(df, pd.DataFrame), 'INVALID RETURN TYPE'



def test_single_run_with_invalid_folder_path():
    with pytest.raises(FileNotFoundError) as e:
        single_run(campaign_folder='INVALID_PATH')
    e.match('Folder INVALID_PATH not found')


def test_single_run_with_products_and_words_path_equal_reserved_output_path():
    for p in 'products_filename', 'words_filename':
        with pytest.raises(NameError) as e:
            single_run(campaign_folder=CAMPAIGN_FOLDER, **{p: 'keywords.csv'})
        e.match(' is RESERVED OUTPUT FILENAME')


def test_single_run_with_none_output_path_for_correct_output():
    df = single_run(campaign_folder=CAMPAIGN_FOLDER,
                    output_path=None)
    assert isinstance(df, pd.DataFrame), 'INVALID RETURN TYPE'


def test_single_run_with_for_correct_file_output():
    single_run(campaign_folder=CAMPAIGN_FOLDER)
    with open(f'{CAMPAIGN_FOLDER}/keywords.csv') as k1, open(f'{CAMPAIGN_FOLDER}/valid_keywords.csv') as k2:
        assert k1.read() == k2.read()



