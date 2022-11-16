#!/bin/bash

# Positive controls
python -c 'from Bio.Seq import Seq; test_seq = Seq("AGTACACTGGT"); print(test_seq)' > pos_test.txt
sha256sum pos_test.txt > pos_test.txt.checksum

# Negative controls
python3 2> py3_test.txt
sha256sum py3_test.txt > py3_test.txt.checksum

python -c 'import bio' 2> misprint_test.txt
sha256sum misprint_test.txt > misprint_test.txt.checksum