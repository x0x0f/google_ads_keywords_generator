from .functions import *
import os


RESERVED_OUTPUT_FILENAME = 'keywords.csv'


def generate(products_path,
             words_path,
             campaign_name,
             criterion_type=('Exact', 'Phrase', 'Broad'),
             output_path=None):
    """Generate keywords table for google ads from products file, words file,
        campaign_name, criterion type. Write result to csv or return pd.DataFrame

    Parameters
    ----------
    products_path : str
        path to file with products words

    words_path : str
        path to file with other words
        
    campaign_name : str
        name of ads campaign
        
    criterion_type : list
         ads campaign criterion types (Default value = ('Exact', 'Phrase', 'Broad'))

    output_path : str, None
         path to result file (Default value = None)

    Returns
    -------
    None or df.DataFrame
    if output_path == None return df.DataFrame else None
    """

    for path in products_path, words_path:
        raise_if_path_not_exists(path)

    products, words = map(file_to_list, (products_path, words_path))
    keywords_gen = create_keywords_generator(products, words)

    df = create_pd_dataframe(
        keywords=keywords_gen,
        campaign_name=campaign_name,
        criterion_type=criterion_type
    )

    if output_path is None:
        return df
    else:
        write_df(df, output_path)


def single_run(campaign_folder,
               products_filename='products.txt',
               words_filename='words.txt',
               criterion_type=('Exact', 'Phrase', 'Broad'),
               campaign_name=None,
               output_path='.'):
    """Generate keywords for google ads from folder with products and words files.
        write to csv or return pd.DataFrame

    Parameters
    ----------
    campaign_folder : str
        folder where products and words files allocated
        
    products_filename : str
        name of products file (Default value = 'products.txt')

    words_filename : str
        name of words file (Default value = 'words.txt')

    criterion_type : list
         ads campaign criterion types (Default value = ('Exact', 'Phrase', 'Broad'))

    campaign_name : str, None
         if campaign_name is None, campaign_name = campaign_folder basename
         (Default value = None)

    output_path : str, None
         path to result file. if output_path = '.' then output_path = campaign_folder
         (Default value = '.')

    Returns
    -------
    None or df.DataFrame
    if output_path == None return df.DataFrame else None
    """

    raise_if_path_not_exists(campaign_folder, folder=True)
    if output_path == '.' and RESERVED_OUTPUT_FILENAME in (products_filename, words_filename):
        raise NameError(f'{RESERVED_OUTPUT_FILENAME} is RESERVED OUTPUT FILENAME')

    if '.' == output_path:
        output_path = os.path.join(campaign_folder, RESERVED_OUTPUT_FILENAME)
    if campaign_name is None:
        campaign_name = os.path.basename(os.path.abspath(campaign_folder))

    products_path, words_path = (
        os.path.join(campaign_folder, filename) for filename in (products_filename, words_filename)
    )

    result = generate(
        products_path,
        words_path,
        campaign_name,
        criterion_type,
        output_path
    )

    if output_path is None:
        return result


def batch_run(campaigns_folder,
              products_filename='products.txt',
              words_filename='words.txt',
              criterion_type=('Exact', 'Phrase', 'Broad')):
    """Generate keywords for google ads from sub folders of campaigns_folder.
        write to csv

    Parameters
    ----------
    campaigns_folder : str
        folder with campaigns folders where products and words files allocated
        
    products_filename : str
        name of products file (Default value = 'products.txt')

    words_filename : str
        name of words file (Default value = 'words.txt')

    criterion_type : list
        ads campaign criterion types (Default value = ('Exact', 'Phrase', 'Broad'))

    Returns
    -------
    str
    output result report
    """

    raise_if_path_not_exists(campaigns_folder, folder=True)
    campaign_folders = get_all_sub_folders(campaigns_folder)

    report = []
    for folder in campaign_folders:
        try:
            single_run(folder, products_filename, words_filename, criterion_type)
            report.append((folder, 'DONE', os.path.join(folder, RESERVED_OUTPUT_FILENAME)))

        except FileNotFoundError as e:
            report.append((folder, 'ERROR', e))

        except NameError as e:
            print(e)
            break

    return format_report(report)

