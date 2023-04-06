# vSNP3 from Conda

This image implements:
- [vSNP3 3.09](https://github.com/USDA-VS/vsnp3)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Get test data:

```
mkdir -p data
cd data

# Download test data
git clone https://github.com/USDA-VS/vsnp3_test_dataset.git
```

Add reference to path:
```
cd vsnp3_test_dataset/vsnp_dependencies
vsnp3_path_adder.py -d `pwd`
```

Run Step 1:
```
cd ../AF2122_test_files/step1
vsnp3_step1.py -r1 *_R1*.fastq.gz -r2 *_R2*.fastq.gz -t Mycobacterium_AF2122
sha256sum alignment_NC_002945v4/*_zc.vcf > ../../../step1.checksum
```

Run Step 2:
```
cd ../step2
vsnp3_step2.py -wd . -a -t Mycobacterium_AF2122
sha256sum Mbovis-All/*.fasta > ../../../step2.checksum
```