"""
This program takes a single KML file with folders for each species, and
outputs cleaned-up KMZ files for each species, as well as a cleaned-up KMZ
file for all species combined. Formatting is standardized across the individual
species files and transparency automatically added to the combined output
file to reflect species density.

A temporary file called doc.kml is produced and not automatically deleted upon
completion of the code.
"""

import zipfile


def read_placemark(infile):
    namestr = infile.readline().strip()  # read name
    line = infile.readline().strip()
    while (not line.startswith("<LineString>") and not line.startswith("<Polygon>") and
           not line.startswith("<MultiGeometry>")):
        line = infile.readline().strip()
    typestr = line
    if typestr.startswith("<MultiGeometry>"):
        coords = []
        while not line.startswith("</Placemark>"):
            line = infile.readline().strip()
            if line.startswith("<coordinates>"):
                line = infile.readline().strip()
                coords.append(line)
        return [namestr, True, coords]
    else:
        line = infile.readline().strip()
        while not line.startswith("<coordinates>"):
            line = infile.readline().strip()
        coords = infile.readline().strip()
        line = infile.readline().strip()
        while not line.startswith("</Placemark>"):
            line = infile.readline().strip()
        return [namestr, False, coords]


def read_crab(infile, namestr):
    line = infile.readline().strip()
    crabplaces = []
    while not line.startswith("</Folder>"):
        if line.startswith("<Placemark>"):
            newplace = read_placemark(infile)
            crabplaces.append(newplace)
        line = infile.readline().strip()
    return [namestr, crabplaces]


def read_folder(infile):
    line = infile.readline().strip()
    crab = None
    while not line.startswith("</Folder>"):
        if line.startswith("<name>Uca"):
            crab = read_crab(infile, line)
            line = "</Folder>"
        else:
            line = infile.readline().strip()
    return crab


def readraw():
    crablist = []
    infile = open("Fiddler Crabs.kml", "r")
    line = infile.readline()
    while line != "":
        line = line.strip()
        if line.startswith("<Folder>"):
            newcrab = read_folder(infile)
            crablist.append(newcrab)
        line = infile.readline()    
    infile.close()
    return crablist


def output_species_kml(crab):
    name = crab[0]
    locs = crab[1]
    name = name[name.find("Uca")+4:name.find("</")]
    with open("doc.kml", "w") as outfile:
        outfile.write("<?xml version=\"1.0\"?>\n")
        outfile.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n")
        outfile.write(" <Document>\n")
        outfile.write("  <Style id=\"species_range\">\n")
        outfile.write("    <LineStyle>\n")
        outfile.write("      <color>FFFF55FF</color>\n")
        outfile.write("      <width>5</width>\n")
        outfile.write("    </LineStyle>\n")
        outfile.write("  </Style>\n")
        outfile.write("  <Placemark>\n")
        outfile.write("    <name/>\n")
        outfile.write("    <description/>\n")
        outfile.write("    <styleUrl>\n")
        outfile.write("      #species_range\n")
        outfile.write("    </styleUrl>\n")
        outfile.write("    <MultiGeometry>\n")
        for loc in locs:
            if loc[1]:
                for x in loc[2]:
                    outfile.write("      <LineString>\n")
                    outfile.write("        <coordinates>\n")
                    outfile.write("          " + x + "\n")
                    outfile.write("        </coordinates>\n")
                    outfile.write("      </LineString>\n")
            else:
                outfile.write("      <LineString>\n")
                outfile.write("        <coordinates>\n")
                outfile.write("          " + loc[2] + "\n")
                outfile.write("        </coordinates>\n")
                outfile.write("      </LineString>\n")
        outfile.write("    </MultiGeometry>\n")
        outfile.write("  </Placemark>\n")
        outfile.write(" </Document>\n")
        outfile.write("</kml>\n")
    with zipfile.ZipFile("u_" + name + ".kmz", "w", zipfile.ZIP_DEFLATED) as myzip:
        myzip.write("doc.kml")
        myzip.close()


def output_all_kml(crabs):
    with open("doc.kml", "w") as outfile:
        outfile.write("<?xml version=\"1.0\"?>\n")
        outfile.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n")
        outfile.write(" <Document>\n")
        for crab in crabs:
            name = crab[0]
            name = name[name.find("Uca")+4:name.find("</")]
            outfile.write("  <Style id=\"" + name + "\">\n")
            outfile.write("    <LineStyle>\n")
            outfile.write("      <color>28FF78F0</color>\n")
            outfile.write("      <width>5</width>\n")
            outfile.write("    </LineStyle>\n")
            outfile.write("  </Style>\n")
        for crab in crabs:
            name = crab[0]
            locs = crab[1]
            name = name[name.find("Uca")+4:name.find("</")]
            outfile.write("  <Placemark>\n")
            outfile.write("    <name>Uca " + name + "</name>\n")
            outfile.write("    <description/>\n")
            outfile.write("    <styleUrl>\n")
            outfile.write("      #" + name + "\n")
            outfile.write("    </styleUrl>\n")
            outfile.write("    <MultiGeometry>\n")
            for loc in locs:
                if loc[1]:
                    for x in loc[2]:
                        outfile.write("      <LineString>\n")
                        outfile.write("        <coordinates>\n")
                        outfile.write("          " + x + "\n")
                        outfile.write("        </coordinates>\n")
                        outfile.write("      </LineString>\n")
                else:
                    outfile.write("      <LineString>\n")
                    outfile.write("        <coordinates>\n")
                    outfile.write("          " + loc[2] + "\n")
                    outfile.write("        </coordinates>\n")
                    outfile.write("      </LineString>\n")
            outfile.write("    </MultiGeometry>\n")
            outfile.write("  </Placemark>\n")
        outfile.write(" </Document>\n")
        outfile.write("</kml>\n")
    with zipfile.ZipFile("uca.kmz", "w", zipfile.ZIP_DEFLATED) as myzip:
        myzip.write("doc.kml")
        myzip.close()

    
def main():
    crabs = readraw()
    for c in crabs:
        output_species_kml(c)
    output_all_kml(crabs)


if __name__ == "__main__":
    main()
