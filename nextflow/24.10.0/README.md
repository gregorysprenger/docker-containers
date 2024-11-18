# pandas 2.0.1

This image implements:
- [Nextflow](https://github.com/nextflow-io/nextflow)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Run the nf-core demo pipeline using Docker.

```
nextflow run \
    nf-core/demo \
    -profile docker,test
    --outdir results
```