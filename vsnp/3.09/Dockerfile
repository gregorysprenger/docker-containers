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
ARG PANDAS_VER="1.3.1"
ARG PYTZ_VER="2021.1"
ARG PYTHON_DATEUTIL_VER="2.8.2"
ARG PYSAM_VER="0.16.0.1"
ARG PYVCF_VER="0.6.8"
ARG HUMANIZE_VER="4.3.0"
ARG BIOPYTHON_VER="1.79"
ARG REGEX_VER="2021.8.3"
ARG DASK_VER="2021.7.2"
ARG TOOLZ_VER="0.11.1"
ARG OPENPYXL_VER="3.0.7"
ARG JDCAL_VER="1.4.1"
ARG ET_XMLFILE_VER="1.1.0"
ARG PY_CPUINFO_VER="8.0.0"
ARG PYPARSING_VER="2.4.7"
ARG XLRD_VER="2.0.1"
ARG XLSXWRITER_VER="3.0.1"
ARG SCIKIT_ALLEL_VER="1.3.5"
ARG SVGWRITE_VER="1.4.1"
ARG CAIROSVG_VER="2.5.2"
ARG CAIROCFFI_VER="1.2.0"
ARG PATHLIB2_VER="2.3.6"
ARG CSSSELECT2_VER="0.4.1"
ARG WEBENCODINGS_VER="0.5.1"
ARG TINYCSS2_VER="1.1.0"
ARG DEFUSEDXML_VER="0.7.1"
ARG PYYAML_VER="5.4.1"
ARG FSSPEC_VER="2021.7.0"
ARG NUMPY_VER="1.21.1"
ARG BZ2FILE_VER="0.98"
ARG CACHETOOLS_VER="4.2.2"
ARG CFFI_VER="1.14.6"
ARG CYCLER_VER="0.10.0"
ARG DEPRECATION_VER="2.1.0"
ARG KIWISOLVER_VER="1.3.1"
ARG MATPLOTLIB_VER="3.4.2"
ARG PACKAGING_VER="21.0"
ARG PILLOW_VER="8.3.1"
ARG PYCPARSER_VER="2.20"
ARG SCIPY_VER="1.7.1"
ARG SCREED_VER="1.0.5"
ARG SETUPTOOLS_VER="57.4.0"
ARG SIX_VER="1.16.0"
ARG SOURMASH_VER="4.2.1"
ARG SEQKIT_VER="2.3.0"
ARG VCFTOOLS_VER="0.1.16"
ARG RAXML_VER="8.2.12"
ARG SPADES_VER="3.15.5"
ARG MINIMAP2_VER="2.24"
ARG BWA_VER="0.7.17"
ARG SAMTOOLS_VER="1.15"

# Dockerfile Information
LABEL base.image="ubuntu:focal"
LABEL software="vSNP3"
LABEL software.version=${VSNP_VER}
LABEL description="Generate annotated SNP tables and phylogenetic trees."
LABEL website="https://github.com/USDA-VS/vsnp3"
LABEL license.url="https://github.com/USDA-VS/vsnp3/blob/main/LICENSE"
LABEL maintainer="Gregory Sprenger"

ENV DEBIAN_FRONTEND=noninteractive 

# Update and install packages
RUN apt-get update -y && apt-get install -y \
    wget \
    libattr1-dev \
    git \
    pigz \
    build-essential \
    autoconf \
    libssl-dev \
    libtool \
    libsqlite3-dev \
    zlib1g-dev \
    make \
    libbz2-dev \
    libreadline-dev \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    liblzma-dev \
    libvcflib-tools \
    libvcflib-dev \
    texinfo \
    texlive-full

# Install Python
RUN wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz && \
    tar xvf Python-${PYTHON_VER}.tgz && \
    rm Python-${PYTHON_VER}.tgz
RUN cd Python-${PYTHON_VER} && \
    ./configure && \
    make && \
    make install

ENV PATH="/usr/local/lib/python${PYTHON_VER_SHORT}/site-packages:${PATH}"

# Create symlink so that python=python3 for vSNP3
RUN ln -s /usr/local/bin/python3 /usr/bin/python & \
    ln -s /usr/local/bin/pip3 /usr/bin/pip

# Install needed packages
RUN pip install pandas==${PANDAS_VER} && \
	pip install pytz==${PYTZ_VER} && \
	pip install pysam==${PYSAM_VER} && \
	pip install PyVCF==${PYVCF_VER} && \
	pip install humanize==${HUMANIZE_VER} && \
	pip install biopython==${BIOPYTHON_VER} && \
	pip install regex==${REGEX_VER} && \
	pip install dask==${DASK_VER} && \
	pip install toolz==${TOOLZ_VER} && \
	pip install openpyxl==${OPENPYXL_VER} && \
	pip install jdcal==${JDCAL_VER} && \
	pip install pyparsing==${PYPARSING_VER} && \
	pip install xlrd==${XLRD_VER} && \
	pip install XlsxWriter==${XLSXWRITER_VER} && \
	pip install svgwrite==${SVGWRITE_VER} && \
	pip install cairosvg==${CAIROSVG_VER} && \
	pip install cairocffi==${CAIROCFFI_VER} && \
	pip install pathlib2==${PATHLIB2_VER} && \
	pip install cssselect2==${CSSSELECT2_VER} && \
	pip install webencodings==${WEBENCODINGS_VER} && \
	pip install tinycss2==${TINYCSS2_VER} && \
	pip install defusedxml==${DEFUSEDXML_VER} && \
	pip install PyYAML==${PYYAML_VER} && \
	pip install fsspec==${FSSPEC_VER} && \
	pip install numpy==${NUMPY_VER} && \
	pip install bz2file==${BZ2FILE_VER} && \
	pip install cachetools==${CACHETOOLS_VER} && \
	pip install cffi==${CFFI_VER} && \
	pip install cycler==${CYCLER_VER} && \
	pip install deprecation==${DEPRECATION_VER} && \
	pip install kiwisolver==${KIWISOLVER_VER} && \
	pip install matplotlib==${MATPLOTLIB_VER} && \
	pip install packaging==${PACKAGING_VER} && \
	pip install pillow==${PILLOW_VER} && \
	pip install pycparser==${PYCPARSER_VER} && \
	pip install scipy==${SCIPY_VER} && \
	pip install screed==${SCREED_VER} && \
	pip install setuptools==${SETUPTOOLS_VER} && \
	pip install six==${SIX_VER} && \
    pip install sourmash==${SOURMASH_VER} && \
    pip install scikit-allel==${SCIKIT_ALLEL_VER} && \
    pip install python-dateutil==${PYTHON_DATEUTIL_VER} && \
    pip install et-xmlfile==${ET_XMLFILE_VER} && \
    pip install py-cpuinfo==${PY_CPUINFO_VER}

# Install SeqKit
RUN wget https://github.com/shenwei356/seqkit/releases/download/v${SEQKIT_VER}/seqkit_linux_amd64.tar.gz && \
    tar -zxvf seqkit_linux_amd64.tar.gz && \
    rm seqkit_linux_amd64.tar.gz && \
    cp seqkit /usr/local/bin/
ENV PATH="/usr/local/bin/seqkit:${PATH}"

# Install vcftools
RUN wget https://github.com/vcftools/vcftools/releases/download/v${VCFTOOLS_VER}/vcftools-${VCFTOOLS_VER}.tar.gz -O vcftools.tar.gz && \
    tar -zxvf vcftools.tar.gz && \
    rm vcftools.tar.gz && \
    mv vcftools-${VCFTOOLS_VER} vcftools && \
    cd vcftools && \
    ./configure && \
    make && \
    make install

# Install RAxML: https://cme.h-its.org/exelixis/resource/download/NewManual.pdf
RUN wget https://github.com/stamatak/standard-RAxML/archive/refs/tags/v${RAXML_VER}.tar.gz && \
    tar -zxvf v${RAXML_VER}.tar.gz && \
    rm v${RAXML_VER}.tar.gz && \
    cd standard-RAxML-${RAXML_VER} && \
    make -f Makefile.AVX.PTHREADS.gcc && \
    cp raxmlHPC-PTHREADS-AVX /usr/local/bin/raxmlHPC-PTHREADS
ENV PATH="/usr/local/bin/raxmlHPC-PTHREADS:${PATH}"

# Install SPAdes
RUN wget http://cab.spbu.ru/files/release${SPADES_VER}/SPAdes-${SPADES_VER}-Linux.tar.gz && \
  tar -xzf SPAdes-${SPADES_VER}-Linux.tar.gz && \
  rm -r SPAdes-${SPADES_VER}-Linux.tar.gz && \
  mv SPAdes-${SPADES_VER}-Linux SPAdes
# set PATH and locale settings for singularity
ENV LC_ALL=C.UTF-8 \
    PATH="/SPAdes/bin:${PATH}"

# Install MiniMap2
RUN wget https://github.com/lh3/minimap2/releases/download/v${MINIMAP2_VER}/minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 && \
    tar -jxvf minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 && \
    rm minimap2-${MINIMAP2_VER}_x64-linux.tar.bz2 && \
    mv minimap2-${MINIMAP2_VER}_x64-linux minimap2
ENV PATH="minimap2/minimap2:${PATH}"

# Install BWA
RUN wget https://github.com/lh3/bwa/releases/download/v${BWA_VER}/bwa-${BWA_VER}.tar.bz2 && \
  tar -xjf bwa-${BWA_VER}.tar.bz2 && \
  rm bwa-${BWA_VER}.tar.bz2 && \
  mv bwa-${BWA_VER} bwa && \
  cd bwa && \
  make
ENV PATH="${PATH}:/bwa"

# Install Samtools
RUN wget https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 && \
  tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 && \
  rm samtools-${SAMTOOLS_VER}.tar.bz2 && \
  mv samtools-${SAMTOOLS_VER} samtools && \
  cd samtools && \
  ./configure && \
  make && \
  make install

# Install vSNP3
RUN git clone -b ${VSNP_VER} https://github.com/USDA-VS/vsnp3.git
ENV PATH="/vsnp3/bin:${PATH}"

FROM ubuntu:focal as app
ARG VSNP_VER
ARG PYTHON_VER_SHORT

ENV DEBIAN_FRONTEND=noninteractive 

# Copy packages from builder to production image
COPY --from=builder /usr/local/lib/ /usr/local/lib/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/
COPY --from=builder /SPAdes/ /SPAdes/
COPY --from=builder /minimap2/ /minimap2/
COPY --from=builder /bwa/ /bwa/
COPY --from=builder /vsnp3/ /vsnp3/

# Copy path environments from builder to production image
ENV PATH="/usr/local/lib/python${PYTHON_VER_SHORT}/site-packages:${PATH}"
ENV PATH="/usr/local/bin/seqkit:${PATH}"
ENV PATH="/usr/local/bin/raxmlHPC-PTHREADS:${PATH}"
ENV LC_ALL=C.UTF-8 \
    PATH="/SPAdes/bin:${PATH}"
ENV PATH="minimap2/minimap2:${PATH}"
ENV PATH="${PATH}:/bwa"
ENV PATH="/vsnp3/bin:${PATH}"

RUN mkdir data/
WORKDIR /data

FROM app as test

# Use git for test data
RUN apt-get update && apt-get install -y git

# Run tests on app output
RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
