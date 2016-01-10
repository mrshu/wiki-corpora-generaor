#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import wikipedia
import click
import Queue


def clean_title(title):
    return title.encode('ascii', 'ignore').lower()\
        .replace('/', '_').replace(' ', '_')


def dump_page(title, lang, path):
    wikipedia.set_lang(lang)
    page = wikipedia.page(title)

    real_path = '{}/{}/{}.txt'.format(path, lang, clean_title(title))
    summary = page.summary.encode('utf-8').replace('\n', ' ')
    if len(summary) < 1:
        print("Empty summary, skipping ({}) {}".format(limit, page))
    else:
        with open(real_path, 'w+') as f:
            f.write(summary + '\n')
            print("Dumped {} ({})".format(page, lang))


@click.command()
@click.option('--title', help='The title to start dumping with')
@click.option('--langs', default='en',
              help='The comma separated languages of the wikis')
@click.option('--path',
              default='dumps/',
              help='The default prefix for path where the data will be dumped')
def main(title, langs, path):
    """Simple script for generating clean text corpora from wiki sites."""
    for lang in langs.split(','):
        dump_page(title, lang, path)

if __name__ == "__main__":
    main()
