# Set global variable
ARG VSNP_VER="3.09"
ARG PYTHON_VER="3.9.6"
ARG PYTHON_VER_SHORT="3.9"

# Build docker image
FROM ubuntu:focal as builder

# Versions of all dependency files
ARG VSNP_VER
ARG PYTHON_VER
ARG PYTHON_VER_SHORT
ARG BIOPYTHON_VER="1.79"
ARG BWA_VER="0.7.17"
ARG BZ2FILE_VER="0.98"
ARG CACHETOOLS_VER="4.2.2"
ARG CAIROCFFI_VER="1.2.0"
ARG CAIROSVG_VER="2.5.2"
ARG CFFI_VER="1.14.6"
ARG CSSSELECT2_VER="0.4.1"
ARG CYCLER_VER="0.10.0"
ARG DASK_VER="2021.7.2"
ARG DEFUSEDXML_VER="0.7.1"
ARG DEPRECATION_VER="2.1.0"
ARG ET_XMLFILE_VER="1.1.0"
ARG FSSPEC_VER="2021.7.0"
ARG HUMANIZE_VER="4.3.0"
ARG JDCAL_VER="1.4.1"
ARG KIWISOLVER_VER="1.3.1"
ARG MATPLOTLIB_VER="3.4.2"
ARG MINIMAP2_VER="2.24"
ARG NUMPY_VER="1.21.1"
ARG OPENPYXL_VER="3.0.7"
ARG PACKAGING_VER="21.0"
ARG PANDAS_VER="1.3.1"
ARG PATHLIB2_VER="2.3.6"
ARG PILLOW_VER="8.3.1"
ARG PY_CPUINFO_VER="8.0.0"
ARG PYCPARSER_VER="2.20"
ARG PYPARSING_VER="2.4.7"
ARG PYSAM_VER="0.16.0.1"
ARG PYTHON_DATEUTIL_VER="2.8.2"
ARG PYTZ_VER="2021.1"
ARG PYVCF_VER="0.6.8"
ARG PYYAML_VER="5.4.1"
ARG RAXML_VER="8.2.12"
ARG REGEX_VER="2021.8.3"
ARG SAMTOOLS_VER="1.15"
ARG SCIKIT_ALLEL_VER="1.3.5"
ARG SCIPY_VER="1.7.1"
ARG SCREED_VER="1.0.5"
ARG SEQKIT_VER="2.3.0"
ARG SETUPTOOLS_VER="57.4.0"
ARG SIX_VER="1.16.0"
ARG SOURMASH_VER="4.2.1"
ARG SPADES_VER="3.15.5"
ARG SVGWRITE_VER="1.4.1"
ARG TINYCSS2_VER="1.1.0"
ARG TOOLZ_VER="0.11.1"
ARG VCFTOOLS_VER="0.1.16"
ARG WEBENCODINGS_VER="0.5.1"
ARG XLRD_VER="2.0.1"
ARG XLSXWRITER_VER="3.0.1"

# Dockerfile Information
LABEL base.image="ubuntu:focal"
LABEL description="Generate annotated SNP tables and phylogenetic trees."
LABEL license.url="https://github.com/USDA-VS/vsnp3/blob/main/LICENSE"
LABEL software.version=${VSNP_VER}
LABEL software="vSNP3"
LABEL website="https://github.com/USDA-VS/vsnp3"
LABEL maintainer="Gregory Sprenger"

# Update and install packages
RUN apt-get update -y 
    && DEBIAN_FRONTEND=noninteractive  \
    apt-get install -y \
    libncursesw5-dev \
    build-essential \
    libreadline-dev \
    libncurses5-dev \
    libvcflib-tools \
    libsqlite3-dev \
    libvcflib-dev \
    libattr1-dev \
    liblzma-dev \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    texlive-full \
    autoconf \
    xz-utils \
    libtool \
    texinfo \
    tk-dev \
    wget \
    pigz \
    make \
    curl \
    llvm \
    git

# Install Python
RUN wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz \
    && tar xvf Python-${PYTHON_VER}.tgz \
    && rm Python-${PYTHON_VER}.tgz \
    && cd Python-${PYTHON_VER} \
    && ./configure \
    && make \
    && make install

ENV PATH="/usr/local/lib/python${PYTHON_VER_SHORT}/site-packages:${PATH}"

# Create symlink so that python=python3 for vSNP3
RUN ln -s /usr/local/bin/python3 /usr/bin/python & \
    ln -s /usr/local/bin/pip3 /usr/bin/pip

# Install needed packages
RUN pip install \
    biopython==${BIOPYTHON_VER} \
    bz2file==${BZ2FILE_VER} \
    cachetools==${CACHETOOLS_VER} \
    cairocffi==${CAIROCFFI_VER} \
    cairosvg==${CAIROSVG_VER} \
    cffi==${CFFI_VER} \
    cssselect2==${CSSSELECT2_VER} \
    cycler==${CYCLER_VER} \
    dask==${DASK_VER} \
    defusedxml==${DEFUSEDXML_VER} \
    deprecation==${DEPRECATION_VER} \
    et-xmlfile==${ET_XMLFILE_VER} \
    fsspec==${FSSPEC_VER} \
    humanize==${HUMANIZE_VER} \
    jdcal==${JDCAL_VER} \
    kiwisolver==${KIWISOLVER_VER} \
    matplotlib==${MATPLOTLIB_VER} \
    numpy==${NUMPY_VER} \
    openpyxl==${OPENPYXL_VER} \
    packaging==${PACKAGING_VER} \
    pandas==${PANDAS_VER} \
    pathlib2==${PATHLIB2_VER} \
    pillow==${PILLOW_VER} \
    py-cpuinfo==${PY_CPUINFO_VER} \
    pycparser==${PYCPARSER_VER} \
    pyparsing==${PYPARSING_VER} \
    pysam==${PYSAM_VER} \
    python-dateutil==${PYTHON_DATEUTIL_VER} \
    pytz==${PYTZ_VER} \
    PyVCF==${PYVCF_VER} \
    PyYAML==${PYYAML_VER} \
    regex==${REGEX_VER} \
    scikit-allel==${SCIKIT_ALLEL_VER} \
    scipy==${SCIPY_VER} \
    screed==${SCREED_VER} \
    setuptools==${SETUPTOOLS_VER} \
    six==${SIX_VER} \
    sourmash==${SOURMASH_VER} \
    svgwrite==${SVGWRITE_VER} \
    tinycss2==${TINYCSS2_VER} \
    toolz==${TOOLZ_VER} \
    webencodings==${WEBENCODINGS_VER} \
    xlrd==${XLRD_VER} \
    XlsxWriter==${XLSXWRITER_VER}

# Install SeqKit
RUN wget https://github.com/shenwei356/seqkit/releases/download/v${SEQKIT_VER}/seqkit_linux_amd64.tar.gz \
    && tar -zxf seqkit_linux_amd64.tar.gz \
    && rm seqkit_linux_amd64.tar.gz \
    && cp seqkit /usr/local/bin/

# Install vcftools
RUN wget https://github.com/vcftools/vcftools/releases/download/v${VCFTOOLS_VER}/vcftools-${VCFTOOLS_VER}.tar.gz -O vcftools.tar.gz \
    && tar -zxf vcftools.tar.gz \
    && rm vcftools.tar.gz \
    && mv vcftools-${VCFTOOLS_VER} vcftools \
    && cd vcftools \
    && ./configure \
    && make \
    && make install

# Install RAxML
RUN wget https://github.com/stamatak/standard-RAxML/archive/refs/tags/v${RAXML_VER}.tar.gz \
    && tar -zxf v${RAXML_VER}.tar.gz \
    && rm v${RAXML_VER}.tar.gz \
    && cd standard-RAxML-${RAXML_VER} \
    && make -f Makefile.AVX.PTHREADS.gcc \
    && mv raxmlHPC-PTHREADS-AVX /usr/local/bin/raxmlHPC-PTHREADS

# Install SPAdes
RUN wget https://github.com/ablab/spades/archive/refs/tags/v${SPADES_VER}.tar.gz \
    && tar -xzf v${SPADES_VER}.tar.gz \
    && rm v${SPADES_VER}.tar.gz \
    && cd spades-${SPADES_VER} \
    && PREFIX=/usr/local/ ./assembler/spades_compile.sh

# Install MiniMap2
RUN wget https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 \
    && tar -xjf minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 \
    && rm minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 \
    && mv minimap2-${MINIMAP2_VER}_x64-linux/minimap2 /usr/local/bin

# Install BWA
RUN wget https://github.com/lh3/bwa/releases/download/v${BWA_VER}/bwa-${BWA_VER}.tar.bz2 \
    && tar -xjf bwa-${BWA_VER}.tar.bz2 \
    && rm bwa-${BWA_VER}.tar.bz2 \
    && cd bwa-${BWA_VER} \
    && make \
    && mv bwa /usr/local/bin

# Install samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 \
    && tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 \
    && rm samtools-${SAMTOOLS_VER}.tar.bz2 \
    && cd samtools-${SAMTOOLS_VER} \
    && ./configure \
    && make \
    && make install

# Install vSNP3
RUN git clone -b ${VSNP_VER} https://github.com/USDA-VS/vsnp3.git
ENV PATH="/vsnp3/bin:${PATH}"

# Run Dockerfile
FROM ubuntu:focal as app
ARG VSNP_VER
ARG PYTHON_VER_SHORT

ENV DEBIAN_FRONTEND=noninteractive 

# Copy packages from builder to production image
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /vsnp3/ /vsnp3/

# Copy path environments from builder to production image
ENV PATH="/usr/local/lib/python${PYTHON_VER_SHORT}/site-packages:${PATH}"
ENV PATH="/vsnp3/bin:${PATH}"

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

# Use git for test data
RUN apt-get update && apt-get install -y git

# Run tests on app output
RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
