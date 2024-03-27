#!/bin/bash

# Make negative control dir and make working dir
mkdir -p neg_controls

# Create empty files
touch \
  neg_controls/test.fa \
  neg_controls/test.gus

# Run gustle on test data
gustle genotype \
  --index neg_controls/test.gus \
  neg_controls/test.fa \
  > neg_controls/empty_summary.tsv \
  2> neg_controls/stderr.out
