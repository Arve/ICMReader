ICMReader 
=========

ICMReader is a tool for converting induction coil data from the  [Canadian Array
for Realtime Investigations of Magnetic Activity
(CARISMA)](http://www.carisma.ca/) to playable audio files.

To use this tool, you will need to register with CARISMA, and download a set of
induction coil data from their repository (please observe their rules of the
road).

## Usage:

1. Unpack the magnetic data files in to a directory without renaming the files.
2. Edit the `Config` class in icmreader.py so start date, number of days and
site matches the data set you are creating 3. Run icmreader.py in the directory
where the data files are contained 4. Done

After ICMReader has finished running (depending on how big the data set is, this
can take considerable time), a new file named `out.wav` is added to the same
directory.

An example generated file is is available [here](https://soundcloud.com/0x61
/magnetic-january), and is generated from ICM data for the month of January,
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
