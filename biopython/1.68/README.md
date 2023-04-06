# Biopython 1.68

This image implements:
- [Biopython 1.68](https://biopython.org/)
- [Python 2.7.18](https://www.python.org/)
- [Numpy 1.16.6](https://numpy.org/)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Test analysis from section [2.4.1 Simple FASTA parsing example](http://biopython.org/DIST/docs/tutorial/Tutorial.html).

Get test data:

```
mkdir -p data
cd data

# Download test data
wget -nv https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta
```

Analyze test data with Biopython:

```
python

>>> from Bio import SeqIO
>>> for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
...     print(seq_record.id)
...     print(repr(seq_record.seq))
...     print(len(seq_record))
...
```