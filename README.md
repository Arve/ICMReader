ICMReader 
=========

ICMReader is a tool for converting induction coil data from the  [Canadian Array
for Realtime Investigations of Magnetic Activity
(CARISMA)](http://www.carisma.ca/) to playable audio files.

To use this tool, you will need to register with CARISMA, and download a set of
induction coil data from their repository (please observe their rules of the
road).

## Usage:

Invoke icmreader.py from a directory containing icm data files

    usage: icmreader.py [-h] [-o OUT] [-s SITE] start_date days

    positional arguments:
      start_date            Start date, on the form YYYY-mm-dd, e.g 2012-12-13
      days                  How many days to gather data for

    optional arguments:
      -h, --help            show this help message and exit
      -o OUT, --out OUT     Output file. Defaults to 'out.wav'
      -s SITE, --site SITE  Which site to get data from. Defaults to FCHU

After ICMReader has finished running (depending on how big the data set is, this
can take considerable time), the file specified with the -o argument should be 
created in the same directory as the original

An example generated file is is available [here](https://soundcloud.com/0x61/magnetic-january), and is generated from ICM data for the month of January,
2013.

A thank you is extended to I.R. Mann, D.K. Milling and the rest of the CARISMA
team for data. CARISMA is operated by the University of Alberta, funded by the
Canadian Space Agency.

For more information about the data, please consult the following reference
paper:

Mann, I. R., et al. (2008), The upgraded CARISMA magnetometer array in the
THEMIS era, Space Sci. Rev., 141, 413–451, doi:10.1007/s11214-008-9457-6.

The full text of the paper in question is available as a PDF from here:
www.carisma.ca/PDFDocs/CARISMAReference.pdf
::
