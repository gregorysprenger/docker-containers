#!/bin/bash

# Make negative control dir and make working dir
mkdir -p neg_controls
cd neg_controls

# Create empty files
touch test.fa test.gus

# Run gustle on test data
gustle genotype \
--index test.gus \
test.fa \
> empty_summary.tsv \
2> stderr.out

cd ../