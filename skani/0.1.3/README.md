# skani v0.1.3

This image implements:
- [skani 0.1.3](https://github.com/bluenote-1577/skani)
- [rust 1.70.0](https://github.com/rust-lang/rust)

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

# Run skani
skani dist CP024957.fna.gz 2BA6PG.fna.gz -o output.txt
```