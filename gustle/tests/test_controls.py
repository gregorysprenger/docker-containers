import os
import pytest
import subprocess
from subprocess import PIPE


def test_positive_controls(capsys):
    run_positive_controls = "bash /tests/scripts/run_positive_controls.sh"
    subprocess.run(run_positive_controls, shell=True, stdout=PIPE)

    # Test gustle index
    with open("pos_controls/test.cgst.checksum") as f:
        cgst_checksum = f.readlines()[0].split(" ")[0]
    assert (
        cgst_checksum
        == "f7c03c7ec44ce1dca23dadc01f7d41a42da90940f34d4241ad86f0cd5f19fc55"
    )

    # Test summary output
    with open("pos_controls/test_summary.tsv.checksum") as f:
        summary_checksum = f.readlines()[0].split(" ")[0]
    assert (
        summary_checksum
        == "43853c7930be69c560a6e08d3a10bcdfbb66aa47d56a21979f0bb1f9bde66f62"
    )


def test_negative_controls(capsys):
    run_negative_controls = "bash /tests/scripts/run_negative_controls.sh"
    subprocess.run(run_negative_controls, shell=True, stdout=PIPE)

    # Test gustle genotype
    with open("neg_controls/stderr.out") as f:
        error_output = f.readlines()[-1].strip()
    assert error_output.endswith("EOF")

    # Test summary output file size
    file_size = os.path.getsize("neg_controls/empty_summary.tsv")
    assert file_size == 0
