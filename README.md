# DTS Hackathon 2021

[DTS hackathon 2021](https://distributed-text-services.github.io/workshops/events/2021-hackathon/), organised by the dhCenter UNIL-EPFL and the École Nationale des Chartes.

This repo serves as a work-in-progress place to gather [my](https://twitter.com/epoz) notes and scripts. If you would like to get in touch, you can also mail me on eposthumus at gmail.com

## Also see:

https://github.com/ErnestSuyver/DBNL_experiment

https://neerlandistiek.nl/2020/02/ik-was-een-avondje-sonnetten-uit-de-dbnl-vissen/

## Goal

My primary goal is to get more to grips with the current DTS spec. See what Python scripts I can put together to explore a dataset, and potentially make a new endpoint available serving up the data.

The initial thought was to look at the [DBNL - the Digital Library of Dutch Literature](https://dbnl.org/) when I saw that they make available a [dump of all their public domain TEI files](https://dbnl.org/letterkunde/pd/index.php).

First we download the [CSV file](https://dbnl.org/extern/titels_pd.php), and then the [XML dump](https://dbnl.org/letterkunde/pd/xml_pd.zip)

### CSV File

The csv file is pipe-symbol delimited, and the first line has a big fat hint to that effetc: `SEP=|`
I haven't seen that convention used before, though it is clear enough what it does. Looking at the file using [visidata](https://www.visidata.org/):

`visidata --skip 1 --csv_delimiter \| titels_pd.csv`

**TIP: Use the arrow keys to navigate in the sheet, and then Shift-F to display a quick histogram of a column.**

`6984` rows, and it looks like a mixture of bibliographic and biographic entries, the records are not normalised. There are multiple records for a title id, with the bibliographic details repeated and bio info varying.
Some of the fieldnames jump out at you in their weirdness, like "vrouw" which is either 0 or 1 - but then you notice why it was chose like that: the majority is 0, that means 95.42% of the records in this collection are not attributed to women!

Many other fields use IDs to enumerate values, for example `amste001` or `denha004` for the `geb_plaats_code`.

### The TEI files

The files are contained in a .zip file, size: `591MB` there are `3195 files`. All the files are in the root, no sub-directories. Filenames are IDS, for example: `will028voor01_01.xml` or, `will028voor02_01.xml`

So while there are circa 7K metadata records, only 3K TEI files. The discrepanyc probably those that are not public domain, and repeated records for authors?

Apart from the filename, we can also find an element /TEI.2/teiHeader/fileDesc/publicationStmt/idno - but that also contains a suffix, for example `wolf016corn01_01` which while the same as the filename does not exactly match the ti_id field in the metadata csv file.

## TODO

- [ ] map the fieldnames from the metadata file to something - DC?

- [ ] see if we can find a mapping of identifiers to some of controlled vocabulary (or at least an explanation for them)
