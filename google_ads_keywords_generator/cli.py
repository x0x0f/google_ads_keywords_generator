from .core import generate, single_run, batch_run
import click
import os


CRITERION_TYPES = {
    'E': 'Exact',
    'P': 'Phrase',
    'B': 'Broad'
}


def validate_criterion_types(ctx, param, value):
    try:
        if set(value.lower()) - set('EPB'.lower()):
            raise ValueError
        return tuple(CRITERION_TYPES[c] for c in value)

    except ValueError:
        raise click.BadParameter('Only E,P,B Chars')


def check_for_reserved_output_file_name(ctx, param, value):
    try:
        if value == 'keywords.csv':
            raise ValueError
        return value

    except ValueError:
        raise click.BadParameter('keyword.csv is RESERVED OUTPUT FILENAME')


@click.group()
def cli():
    pass


@cli.command(name='generate')
@click.option('-i', '--input', required=True, nargs=2, type=click.Path(exists=True),
              help='Products file and words file')
@click.option('-c', '--campaign', required=True, help='Campaign name')
@click.option('-t', '--types', default='EPB', type=str, callback=validate_criterion_types,
              help='Criterion Type\nDefault: EPB\nE=Exact,P=Phrase,B=Broad\nExample: -t E, -t EP, -t BE, -t BPE')
@click.option('-o', '--output', default=None,
              help='Output file path. If not using, output result to stdout')
def generate_cmd(input, campaign, types, output):
    res = generate(
        products_path=input[0],
        words_path=input[1],
        campaign_name=campaign,
        criterion_type=types,
        output_path=output
    )
    click.echo(f'DONE: {output}' if output is not None else res.to_string())


@cli.command(name='single')
@click.option('-i', '--input', required=True, type=click.Path(exists=True),
              help='Campaign folder where products and words files allocated')
@click.option('-p', '--products', default='products.txt', type=str, callback=check_for_reserved_output_file_name,
              help='Name of products file\nDefault: products.txt')
@click.option('-w', '--words', default='words.txt', type=str, callback=check_for_reserved_output_file_name,
              help='Name of words file\nDefault: words.txt')
@click.option('-c', '--campaign', default=None, help='Campaign name\nIf --campaign is not using, Campaign name = --input folder basename')
@click.option('-t', '--types', default='EPB', type=str, callback=validate_criterion_types,
              help='Criterion Type\nDefault: EPB\nE=Exact,P=Phrase,B=Broad\nExample: -t E, -t EP, -t BE, -t BPE')
@click.option('-o', '--output', default='.', type=click.Path(),
              help='Path to result file. If --output = "." then output path = --input folder\nDefault: "."')
@click.option('-oS', '--output_stdout', is_flag=True, help='If using, output result to stdout')
def single_cmd(input, products, words, campaign, types, output, output_stdout):
    if output_stdout:
        output = None

    res = single_run(
        campaign_folder=input,
        products_filename=products,
        words_filename=words,
        criterion_type=types,
        campaign_name=campaign,
        output_path=output
    )
    if output is not None:
        stdout_str = 'DONE: ' + os.path.join(input if output == "." else output, 'keywords.csv')
    else:
        stdout_str = res.to_string()

    click.echo(stdout_str)


@cli.command(name='batch')
@click.option('-i', '--input', required=True, type=click.Path(exists=True),
              help='Campaign folder where products and words files allocated')
@click.option('-p', '--products', default='products.txt', type=str,
              help='Name of products file\nDefault: products.txt')
@click.option('-w', '--words', default='words.txt', type=str,
              help='Name of words file\nDefault: words.txt')
@click.option('-t', '--types', default='EPB', type=str, callback=validate_criterion_types,
              help='Criterion Type\nDefault: EPB\nE=Exact,P=Phrase,B=Broad\nExample: -t E, -t EP, -t BE, -t BPE')
def batch_cmd(input, products, words, types):
    res = batch_run(
        input,
        products_filename=products,
        words_filename=words,
        criterion_type=types
    )
    click.echo(res)


if __name__ == '__main__':
    cli()
