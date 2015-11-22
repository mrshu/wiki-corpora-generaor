#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import wikipedia
import click
import Queue


def clean_title(title):
    return title.encode('ascii', 'ignore').lower()\
        .replace('/', '_').replace(' ', '_')


def dump_page(lang, limit, visited, q, path):
    if limit <= 0:
        return

    if q.empty():
        print("Queue is empty")
        return

    title = q.get()
    if title in visited:
        return dump_page(lang, limit, visited, q, path)

    page = None
    wikipedia.set_lang(lang)
    try:
        page = wikipedia.page(title)
    except:
        page = None

    if page is not None:
        real_path = '{}/{}/{}.txt'.format(path, lang, clean_title(title))
        summary = page.summary.encode('utf-8').replace('\n', ' ')
        if len(summary) < 1:
            print("Empty summary, skipping ({}) {}".format(limit, page))
        else:
            with open(real_path, 'w+') as f:
                f.write(summary + '\n')
                print("Dumped ({}) {}".format(limit, page))
                limit -= 1

    visited.append(title)

    if hasattr(page, 'links'):
        for link in page.links:
            q.put(link)

    dump_page(lang, limit, visited, q, path)


@click.command()
@click.option('--title', help='The title to start dumping with')
@click.option('--lang', default='en', help='The language of the wiki')
@click.option('--count', default=100,
              help='The maximal number of pages to dump.')
@click.option('--path',
              default='dumps/',
              help='The default prefix for path where the data will be dumped')
def main(title, lang, count, path):
    """Simple script for generating clean text corpora from wiki sites."""
    q = Queue.Queue()
    q.put(title)
    page = dump_page(lang, count, [], q, path)

if __name__ == "__main__":
    main()
