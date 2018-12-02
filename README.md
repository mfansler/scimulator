# scimulator
Simulation tools for 3'-end tag-based RNA sequencing.

**This project is in pre-alpha development!**

At present there is a lack of tools to generate raw simulation data of single-cell RNA-seq data, in particular 3'-end tag-based data. Since most single-cell data analyses focus only on characterizing gene expression, previous simulation tools have focused on generating gene count matrices rather than raw data.  This lack of raw data generation hinders the development of specialized pipelines that take advantage of the full information signal present in 3'-end tag based data.  This module seeks to remedy this by providing tools for generating raw FASTQ data using transcriptome annotations.
