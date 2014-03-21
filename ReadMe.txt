This is the code and data required to completely reconstruct the fiddlercrab.info website, EXCEPT for media files: images and videos. 

There are two programs, both written in Python 3 (without any external dependencies).

(1) CreatePages.py 
This creates all of the webpages from the various input flatfiles (described below). To run properly it expects to find the following five subfolders, not automatically created:

art
names
photos
references
video

This program uses the following files as input (all but the last are tab-delimited text, exported directly from Excel):

(a) art.txt
Contains primary data for all art on the site, used on both individual species pages and the general multimedia art page.

(b) citeinfo.txt
This file contains the primary context-sensitive name citation data used for constructing all of the name usage 

(c) photos.txt
Contains primary data for all photos on the site, used on both individual species pages and the general multimedia photo page.

(d) references_cites.txt
Contains citation information for each reference in the database: the first column is the formatted citation for cross-referencing, i.e. "(Rosenberg, 2002)", while the second column is the internal unique key used to identify the citation. These references are in the same exact order as those found in the references.html file.

(e) species_info.txt
Contains primary data for all currently recognized valid species, used primarily to construct individual species pages.

(f) species_names.txt
Contains primary data for all specific names (whether valid or not), used as part of the general name index.

(g) subgenera.txt
Contains primary data about the currently accepted subgenera, used as part of the systematic treatement on the site.

(h) videos.txt
Contains primary data for all videos on the site, used on both individual species pages and the general multimedia videos page.

(i) references.html
This is an html file containing all of the references in the database, already properly formatted for web display. It is exported into html output from Endnote. The references are in the same exact order as found in the references_cites.txt file. This html page is not used directly on the site: rather, the pre-formatted references are extracted from this file and output into various pages on the site as necessary.

--
(2) CreateKML.py
This program takes a single KML file ("Fiddler Crabs.kml") which contains internal folders for each species, and outputs cleaned-up KMZ files for each species, as well as a cleaned-up KMZ file for all species combined. Formatting is standardized across the individual species files and transparency automatically added to the combined output file to reflect species density.

A temporary file called doc.kml is produced by this program; it is not automatically deleted upon completion of the code.

This program will create all of the .kmz files in the current directory, but the webpages created by CreatePages.py expects to find all of the .kmz files in a subfolder titled maps
