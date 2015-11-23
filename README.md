# wiki-corpora-generator

A script that generates corpora (preferably for further exploration/exploiation
in context of Natural Language Processing) by dumping text from rendered
Wikipedia pages.

The process of dumping goes as follows:

1. The article/page specified in `--title` added to a Queue.

2. The first article/page title from Queue is taken. It is then dumped and if
   it contains links to other pages (that is those that were not visited yet)
   these are added to a Queue.

3. Part 2. is repeated until the Queue is not empty or the `--limit` of
   articles/pages has not been reached.


Note that this script does not only work on `en.wikipedia.org` but also on any
other Wikipedia locale. The language can be specified with the `--lang`
parameter.
