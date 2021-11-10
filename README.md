# Google Ads Keywords Generator

Generate keywords for google ads from products and words files.

## Requirements

* python >= 3.6

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/).
inside package directory
```bash
pip install -e .
```
or 
```bash
sudo make install
```
## Usage
<h3>Python</h3>
Generate keywords as pandas dataframe.
```python
from google_ads_keywords_generator import generate


pandas_dataframe = generate(
    products_path='products.txt',  # products file path
    words_path='words.txt',  # words file path
    campaign_name='test_camp',  # google ads campaign name
    criterion_type=('Exact', 'Phrase', 'Broad'), # optional (Default value = ('Exact', 'Phrase', 'Broad'))
    output_path=None # optional (Default value = None)
)
```
Generate keywords and write result to csv file.
```python
from google_ads_keywords_generator import generate


generate(
    products_path='products.txt',  # products file path
    words_path='words.txt',  # words file path
    campaign_name='test_camp',  # google ads campaign name
    criterion_type=('Exact', 'Phrase', 'Broad'),  # optional (Default value = ('Exact', 'Phrase', 'Broad'))
    output_path='keywords.csv'  # optional (Default value = None)
)
```
Generate keywords from campaign folder as pandas dataframe.
```python
from google_ads_keywords_generator import single_run


# if campaign_name == None then
# campaign_name = campaign_folder 

single_run(
    campaign_folder='test_campaign',  # campaign folder path
    products_filename='products.txt',  # optional (Default value = 'products.txt')
    words_filename='words.txt',  # optional (Default value = 'words.txt')
    criterion_type=('Exact', 'Phrase', 'Broad'),  # optional (Default value = ('Exact', 'Phrase', 'Broad'))
    campaign_name=None,  # optional (Default value = None)
    output_path=None  # optional (Default value = '.')
)

# single run with default 
# products_filename, words_filename,
# criterion_type and custom campaign_name

single_run(
    campaign_folder='test_campaign',  # campaign folder path
    campaign_name='secret_test',  # optional (Default value = None)
    output_path=None  # optional (Default value = '.')
)
```
Generate keywords from campaign folder and write result to csv file.
```python
from google_ads_keywords_generator import single_run


# if campaign_name == None then
# campaign_name = campaign_folder 
# if output_path == '.' then
# output_path = campaign_folder

single_run(
    campaign_folder='test_campaign',  # campaign folder path
    products_filename='products.txt',  # optional (Default value = 'products.txt')
    words_filename='words.txt',  # optional (Default value = 'words.txt')
    criterion_type=('Exact', 'Phrase', 'Broad'),  # optional (Default value = ('Exact', 'Phrase', 'Broad'))
    campaign_name=None,  # optional (Default value = None)
    output_path='.'  # optional (Default value = '.')
)

# single run with default 
# products_filename, words_filename,
# criterion_type and custom campaign_name, output_Path

single_run(
    campaign_folder='test_campaign',  # campaign folder path
    campaign_name='secret_test',  # optional (Default value = None)
    output_path='my_output.csv'  # optional (Default value = '.')
)
```
Generate keywords from campaign folders and write result to csv files.
```python
from google_ads_keywords_generator import batch_run


batch_run(
    campaigns_folder='folder_with_sub_folders',  # path where campaign folders allocated
    products_filename='products.txt',  # optional (Default value = 'products.txt')
    words_filename='words.txt',  # optional (Default value = 'words.txt')
    criterion_type=('Exact', 'Phrase', 'Broad'),  # optional (Default value = ('Exact', 'Phrase', 'Broad'))
)

# result saved in sub_folder/keywords.csv

batch_run(
    campaigns_folder='folder_with_campaigns_folders',  # path where campaign folders allocated
)
```
<h3>Console</h3>
Help info.
```bash
google_ads_keywords_generator generate --help
google_ads_keywords_generator single --help
google_ads_keywords_generator batch --help
```

Generate keywords from "products.txt" and "words.txt" files with "test" as campaign name. Use default criterion type. Output result to stdout.
* -t criterion type. (Default value: EPB) E=Exact, P=Phrase, B=Broad
```bash
google_ads_keywords_generator generate -i products.txt words.txt -c test -t EPB
```
Same but output result to "result.csv" file.
```bash
google_ads_keywords_generator generate -i products.txt words.txt -c test -o result.csv
```
Generate keywords from campaign folder. Using campaign folder name as campaign name, -p as products file, -w words file. Output result to stdout.
```bash
google_ads_keywords_generator single -i campaign_folder -p products.txt -w words.txt -oS
```
Same but output result to "custom_folder/keywords.csv".
* -p products file path. (Default value: products.txt)
* -w words file path. (Default value: words.txt)
```bash
google_ads_keywords_generator single -i campaign_folder -o custom_folder/keywords.csv
```
Custom campaign name.
```bash
google_ads_keywords_generator single -i campaign_folder -c custom_name
```
Generate keywords from folder where campaign folders allocated. Write result to csv files.
```bash
google_ads_keywords_generator batch -i folder_with_sub_folders -p products.txt -w words.txt -t EPB
```
Same.
```bash
google_ads_keywords_generator batch -i folder_with_sub_folders
```
## Authors
x0x0f
## Version History
* 0.1.0
    * Initial Release
## License
[MIT](https://choosealicense.com/licenses/mit/)
