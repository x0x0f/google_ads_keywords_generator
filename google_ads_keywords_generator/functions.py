import pandas as pd
import os


def raise_if_path_not_exists(path, folder=False):
    """raise FileNotFoundError if path not exists

    Parameters
    ----------
    path : str
        
    folder : bool
         (Default value = False)

    Returns
    -------
    None
    """
    if not os.path.exists(path):
        msg = '{} {} not found'.format('Folder' if folder else 'File', path)
        raise FileNotFoundError(msg)


def get_all_sub_folders(folder_path):
    """get all sub folders to list

    Parameters
    ----------
    folder_path : str

    Returns
    -------
    list
    """
    sub_folders = []
    for path in os.listdir(folder_path):
        full_path = os.path.join(folder_path, path)
        if os.path.isdir(full_path):
            sub_folders.append(full_path)

    return sub_folders


def file_to_list(file_path):
    """add file lines to output list if line is not empty, return output list

    Parameters
    ----------
    file_path : str

    Returns
    -------
    list
    """
    output_list = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line:
                output_list.append(line)

    return output_list


def create_keywords_generator(products, words):
    """create keywords generator object from products and words lists

    Parameters
    ----------
    products : list
    words : list

    Returns
    -------
    Generator
    """
    for product in products:
        for word in words:
            for pair in (product, word), (word, product):
                yield product, '{} {}'.format(*pair)


def create_dfs_with_different_criterion_types(df, criterion_type):
    """Create list of pd.DataFrame objects with different criterion types

    Parameters
    ----------
    df : pd.DataFrame
    criterion_type : list

    Returns
    -------
    list
    """
    dfs = []
    for i in range(len(criterion_type)):
        if i != 0:
            df = df.copy()

        df['Criterion Type'] = criterion_type[i]
        dfs.append(df)

    return dfs


def create_pd_dataframe(keywords, campaign_name, criterion_type):
    """create pd.DataFrame from keywords, campaign_name, criterion_type

    Parameters
    ----------
    keywords : Generator
    campaign_name : str
    criterion_type : list

    Returns
    -------
    pd.DataFrame
    """
    base_df = pd.DataFrame(keywords)
    base_df = base_df.rename(columns={0: 'Ad Group', 1: 'Keyword'})
    base_df['Campaign'] = campaign_name

    dfs_with_criterion_type = create_dfs_with_different_criterion_types(base_df, criterion_type)
    df_final = pd.concat(dfs_with_criterion_type)

    return df_final


def write_df(df, output_path):
    """write pd.DataFrame to output csv file

    Parameters
    ----------
    df : pd.DataFrame
    output_path : str

    Returns
    -------
    None
    """
    df.to_csv(output_path, index=False)


def format_report(report_list):
    """create formatted report str from report_list

    Parameters
    ----------
    report_list : list

    Returns
    -------
    str
    """
    header_str = '###REPORT###\n'
    body_str = '\n'.join('FOLDER: {}\nSTATUS: {}, {}\n'.format(*r) for r in report_list)
    footer_str = '############\n'
    return header_str + body_str + footer_str
