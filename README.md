## Book Publishing

My Python scripts for compiling long-form Obsidian markdown files into a book.

## Prerequisites

Install package dependencies

```bash
source ./env/bin/activate
pip install panflute
```

## Execute Scripts

Execute the following commands to source the virtual environment and then execute a given script.

```bash
source ./env/bin/activate
python <script-name>
```

## Additional Resources

- There are many examples of python filters in [the pandocfilters repository](https://github.com/jgm/pandocfilters).
- For an alternative library for writing pandoc filters, with a more "Pythonic" design, see [panflute](https://github.com/sergiocorreia/panflute).
    - [Panflute User Guide](https://panflute.readthedocs.io/en/latest/guide.html)

## Pandoc Options

Best thing to do is just execute `pandoc --help`

--file-scope

Parse each file individually before combining for multifile documents. 
This will allow footnotes in different files with the same identifiers to work as expected. If this option is set, 
footnotes and links will not work across files.

--wrap=none

To completely disable line-wrapping

--wrap=preserve

To use the same wrapping that was used in the input

--columns=100

If you DO want long lines to be wrapped, but would like up to 100 chars in a line instead of the default of 72 chars, then invoke pandoc with