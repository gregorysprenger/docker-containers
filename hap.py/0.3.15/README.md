# hap.py v0.3.15

This image implements the following packages using Ubuntu 22.04.4 LTS:
- [hap.py 0.3.15](https://github.com/Illumina/hap.py)
- [Python 2.7](https://www.python.org/downloads/release/python-2718/)
- [bx-python 0.8.8](https://github.com/bxlab/bx-python)
- [cython 0.29.37](https://github.com/cython/cython)
- [Pysam 0.20.0](https://github.com/pysam-developers/pysam)
- [Apache Ant 1.9.7](https://github.com/apache/ant)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Run basic tests provided within the `hap.py` repository.
```
# Navigate to hap.py directory
cd /opt/hap.py/

# Run hap.py tests
## NOTE: The quantification step will fail due to differences in rounding in outputs
/opt/hap.py-source/src/sh/run_tests.sh
```