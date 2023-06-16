# fastANI v1.33

This image implements:
- [fastANI 1.33](https://github.com/ParBLiSS/FastANI)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

```
# Download data
wget -nv --no-check-certificate \
  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/804/165/GCF_002804165.1_ASM280416v1/GCF_002804165.1_ASM280416v1_genomic.fna.gz \
  -O CP024957.fna.gz

wget -nv --no-check-certificate \
  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/024/297/125/GCF_024297125.1_ASM2429712v1/GCF_024297125.1_ASM2429712v1_genomic.fna.gz \
  -O 2BA6PG.fna.gz

# Run fastANI
fastANI --ref CP024957.fna.gz --query 2BA6PG.fna.gz -o output.txt
```