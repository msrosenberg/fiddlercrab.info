
import codecs
import datetime
import random

speciesURL = "uca_species.html"
refURL = "uca_references.html"
refsumURL = "uca_refsummary.html"
systURL = "uca_systematics.html"
commonURL = "uca_common_names.html"
photoURL = "uca_photos.html"
videoURL = "uca_videos.html"
mapURL = "uca_ranges.html"
lifeCycleURL = "uca_lifecycle.html"
treeURL = "uca_phylogeny.html"
# artURL = "uca_art.html"
artSciURL = "uca_art_science.html"
artStampURL = "uca_art_stamps.html"
artCraftURL = "uca_art_crafts.html"
morphURL = "uca_morphology.html"
citeURL = "citation.html"
namesumURL = "name_graphs.html"
# fossilImage = "<img class=\"fossilImg\" src=\"images/fossil.png\" alt=\" (fossil)\" title=\" (fossil)\" />"
fossilImage = " <span class=\"fossil-img\">&#9760;</span>"

randSeed = random.randint(0, 10000)


# ----classes----
class ReferenceClass:
    """ A class to hold references """
    def __init__(self):
        self.formatted_html = ""
        self.citation = ""
        self.cite_key = ""
        self.language = ""

    # def __init__(self):
    #     self.__formattedHTML = ""
    #     self.__citation = ""
    #     self.__citeKey = ""
    #     self.__language = ""
    #
    #
    # def citation(self):
    #     return self.__citation
    #
    #
    # def setCitation(self, x):
    #     self.__citation = x
    #
    #
    # def citeKey(self):
    #     return self.__citeKey
    #
    #
    # def setciteKey(self, x):
    #     self.__citeKey = x
    #
    #
    # def formattedHTML(self):
    #     return self.__formattedHTML
    #
    #
    # def setFormattedHTML(self, x):
    #     self.__formattedHTML = x
    #
    #
    # def language(self):
    #     return self.__language
    #
    #
    # def setLanguage(self, x):
    #     self.__language = x


class SpecificNameClass:
    """ a class to hold specific names """
    def __init__(self):
        self.name = ""
        self.variations = ""
        self.synonym = ""
        self.original_binomial = ""
        self.priority_source = ""
        self.meaning = ""
        self.notes = ""

    # def __init__(self):
    #     self.__name = ""
    #     self.__variations = ""
    #     self.__synonym = ""
    #     self.__originalBinomial = ""
    #     self.__prioritySource = ""
    #     self.__meaning = ""
    #     self.__notes = ""
    #
    # def name(self):
    #     return self.__name
    #
    # def setName(self,x):
    #     self.__name = x
    #
    # def variations(self):
    #     return self.__variations
    #
    # def setVariations(self,x):
    #     self.__variations = x
    #
    # def synonym(self):
    #     return self.__synonym
    #
    # def setSynonym(self,x):
    #     self.__synonym = x
    #
    # def originalBinomial(self):
    #     return self.__originalBinomial
    #
    # def setOriginalBinomial(self,x):
    #     self.__originalBinomial = x
    #
    # def prioritySource(self):
    #     return self.__prioritySource
    #
    # def setPrioritySource(self,x):
    #     self.__prioritySource = x
    #
    # def meaning(self):
    #     return self.__meaning
    #
    # def setMeaning(self,x):
    #     self.__meaning = x
    #
    # def notes(self):
    #     return self.__notes
    #
    # def setNotes(self,x):
    #     self.__notes = x


class SubgenusClass:
    """ a class to hold subgenera """
    def __init__(self):
        self.subgenus = ""
        self.author = ""
        self.type_species = ""
        self.notes = ""
        self.taxonid = ""
        self.eolid = ""
    # def __init__(self):
    #     self.__subgenus = ""
    #     self.__author = ""
    #     self.__typeSpecies = ""
    #     self.__notes = ""
    #     self.__taxonid = ""
    #     self.__EOLid = ""
    #
    # def subgenus(self):
    #     return self.__subgenus
    #
    # def setSubgenus(self,x):
    #     self.__subgenus = x
    #
    # def author(self):
    #     return self.__author
    #
    # def setAuthor(self,x):
    #     self.__author = x
    #
    # def typeSpecies(self):
    #     return self.__typespecies
    #
    # def setTypeSpecies(self,x):
    #     self.__typespecies = x
    #
    # def notes(self):
    #     return self.__notes
    #
    # def setNotes(self,x):
    #     self.__notes = x
    #
    # def taxonid(self):
    #     return self.__taxonid
    #
    # def setTaxonid(self,x):
    #     self.__taxonid = x
    #
    # def EOLid(self):
    #     return self.__EOLid
    #
    # def setEOLid(self,x):
    #     self.__EOLid = x


class VideoClass:
    """ a class to hold video information """
    def __init__(self):
        self.species = ""
        self.n = 0
        self.activity = ""
        self.caption = ""
        self.length = ""
        self.size = ""
        self.format = ""
        self.date_location = ""
        self.author = ""
        self.notes = ""
    # def __init__(self):
    #     self.__species = ""
    #     self.__n = 0
    #     self.__activity = ""
    #     self.__caption = ""
    #     self.__length = ""
    #     self.__size = ""
    #     self.__format = ""
    #     self.__dateLocation = ""
    #     self.__author = ""
    #     self.__notes = ""
    #
    # def species(self):
    #     return self.__species
    #
    # def setSpecies(self,x):
    #     self.__species = x
    #
    # def n(self):
    #     return self.__n
    #
    # def setn(self,x):
    #     self.__n = x
    #
    # def activity(self):
    #     return self.__activity
    #
    # def setActivity(self,x):
    #     self.__activity = x
    #
    # def caption(self):
    #     return self.__caption
    #
    # def setCaption(self,x):
    #     self.__caption = x
    #
    # def length(self):
    #     return self.__length
    #
    # def setLength(self,x):
    #     self.__length = x
    #
    # def size(self):
    #     return self.__size
    #
    # def setSize(self,x):
    #     self.__size = x
    #
    # def format(self):
    #     return self.__format
    #
    # def setFormat(self,x):
    #     self.__format = x
    #
    # def dateLocation(self):
    #     return self.__dateLocation
    #
    # def setDateLocation(self,x):
    #     self.__dateLocation = x
    #
    # def author(self):
    #     return self.__author
    #
    # def setAuthor(self,x):
    #     self.__author = x
    #
    # def notes(self):
    #     return self.__notes
    #
    # def setNotes(self,x):
    #     self.__notes = x


class PhotoClass:
    """ a class to hold photo information """
    def __init__(self):
        self.species = ""
        self.n = 0
        self.caption = ""
    # def __init__(self):
    #     self.__species = ""
    #     self.__n = 0
    #     self.__caption = ""
    #
    # def species(self):
    #     return self.__species
    #
    # def setSpecies(self,x):
    #     self.__species = x
    #
    # def n(self):
    #     return self.__n
    #
    # def setn(self,x):
    #     self.__n = x
    #
    # def caption(self):
    #     return self.__caption
    #
    # def setCaption(self,x):
    #     self.__caption = x


class ArtClass:
    """ a class to hold art information """
    def __init__(self):
        self.art_type = ""
        self.author = ""
        self.year = ""
        self.title = ""
        self.image = ""
        self.ext = ""
        self.species = ""
        self.notes = ""
        self.cite_key = ""

    # def __init__(self):
    #     self.__artType = ""
    #     self.__author = ""
    #     self.__year = ""
    #     self.__title = ""
    #     self.__image = ""
    #     self.__ext = ""
    #     self.__species = ""
    #     self.__notes = ""
    #     self.__citeKey = ""
    #
    # def artType(self):
    #     return self.__artType
    #
    # def setArtType(self,x):
    #     self.__artType = x
    #
    # def citeKey(self):
    #     return self.__citeKey
    #
    # def setCiteKey(self,x):
    #     self.__citeKey = x
    #
    # def author(self):
    #     return self.__author
    #
    # def setAuthor(self,x):
    #     self.__author = x
    #
    # def year(self):
    #     return self.__year
    #
    # def setYear(self,x):
    #     self.__year = x
    #
    # def title(self):
    #     return self.__title
    #
    # def setTitle(self,x):
    #     self.__title = x
    #
    # def image(self):
    #     return self.__image
    #
    # def setImage(self,x):
    #     self.__image = x
    #
    # def ext(self):
    #     return self.__ext
    #
    # def setExt(self,x):
    #     self.__ext = x
    #
    # def species(self):
    #     return self.__species
    #
    # def setSpecies(self,x):
    #     self.__species = x
    #
    # def notes(self):
    #     return self.__notes
    #
    # def setNotes(self,x):
    #     self.__notes = x


class MorphologyClass:
    def __init__(self):
        self.character = ""
        self.parent = ""
        self.image = ""
        self.description = ""
        self.caption = ""
    # def __init__(self):
    #     self.__character = ""
    #     self.__parent = ""
    #     self.__image = ""
    #     self.__description = ""
    #     self.__caption = ""
    #
    # def character(self):
    #     return self.__character
    #
    # def setCharacter(self,x):
    #     self.__character = x
    #
    # def parent(self):
    #     return self.__parent
    #
    # def setParent(self,x):
    #     self.__parent = x
    #
    # def image(self):
    #     return self.__image
    #
    # def setImage(self,x):
    #     self.__image = x
    #
    # def description(self):
    #     return self.__description
    #
    # def setDescription(self,x):
    #     self.__description = x
    #
    # def caption(self):
    #     return self.__caption
    #
    # def setCaption(self,x):
    #     self.__caption = x


class SpeciesClass:
    def __init__(self):
        self.species = ""
        self.subgenus = ""
        self.type_species = ""
        self.type_reference = ""
        self.common = ""
        self.commonext = ""
        self.range = ""
        self.range_references = ""
        self.region = ""
        self.status = ""
        self.taxonid = ""
        self.eolid = ""
        self.inatid = ""
        self.gbifid = ""
    # def __init__(self):
    #     self.__species = ""
    #     self.__subgenus = ""
    #     self.__typeSpecies = ""
    #     self.__typeRef = ""
    #     self.__common = ""
    #     self.__commonext = ""
    #     self.__range = ""
    #     self.__rangeRefs = ""
    #     self.__region = ""
    #     self.__status = ""
    #     self.__taxonid = ""
    #     self.__EOLid = ""
    #     self.__iNatid = ""
    #     self.__gbifid = ""
    # def species(self):
    #     return self.__species
    # def setSpecies(self, x):
    #     self.__species = x
    # def subgenus(self):
    #     return self.__subgenus
    # def setSubgenus(self, x):
    #     self.__subgenus = x
    # def typeSpecies(self):
    #     return self.__typeSpecies
    # def setTypeSpecies(self, x):
    #     self.__typeSpecies = x
    # def typeRef(self):
    #     return self.__typeRef
    # def setTypeRef(self, x):
    #     self.__typeRef = x
    # def common(self):
    #     return self.__common
    # def setCommon(self, x):
    #     self.__common = x
    # def commonext(self):
    #     return self.__commonext
    # def setCommonext(self, x):
    #     self.__commonext = x
    # def range(self):
    #     return self.__range
    # def setRange(self, x):
    #     self.__range = x
    # def rangeRefs(self):
    #     return self.__rangeRefs
    # def setRangeRefs(self, x):
    #     self.__rangeRefs = x
    # def region(self):
    #     return self.__region
    # def setRegion(self, x):
    #     self.__region = x
    # def status(self):
    #     return self.__status
    # def setStatus(self, x):
    #     self.__status = x
    # def taxonid(self):
    #     return self.__taxonid
    # def setTaxonid(self, x):
    #     self.__taxonid = x
    # def EOLid(self):
    #     return self.__EOLid
    # def setEOLid(self, x):
    #     self.__EOLid = x
    # def iNatid(self):
    #     return self.__iNatid
    # def setiNatid(self, x):
    #     self.__iNatid = x
    # def gbifid(self):
    #     return self.__gbifid
    # def setgbifid(self, x):
    #     self.__gbifid = x


class CitationClass:
    def __init__(self):
        self.cite_key = ""
        self.name_key = ""
        self.name = ""
        self.common = ""
        self.where = ""
        self.context = ""
        self.application = ""
        self.cite_n = ""
        self.actual = ""
        self.source = ""
        self.name_note = ""
        self.general_note = ""

    def __lt__(self, x):
        if self.name == x.name:
            if self.context == x.context:
                return self.application < x.application
            else:
                return self.context < x.context
        else:
            return self.name < x.name

    # def __init__(self):
    #     self.__citeKey = ""
    #     self.__nameKey = ""
    #     self.__name = ""
    #     self.__common = ""
    #     self.__where = ""
    #     self.__context = ""
    #     self.__application = ""
    #     self.__citeN = ""
    #     self.__actual = ""
    #     self.__source = ""
    #     self.__nameNote = ""
    #     self.__generalNote = ""
    # def citeKey(self):
    #     return self.__citeKey
    # def setCiteKey(self,x):
    #     self.__citeKey = x
    # def nameKey(self):
    #     return self.__nameKey
    # def setNameKey(self,x):
    #     self.__nameKey = x
    # def name(self):
    #     return self.__name
    # def setName(self,x):
    #     self.__name = x
    # def common(self):
    #     return self.__common
    # def setCommon(self,x):
    #     self.__common = x
    # def where(self):
    #     return self.__where
    # def setWhere(self,x):
    #     self.__where = x
    # def context(self):
    #     return self.__context
    # def setContext(self,x):
    #     self.__context = x
    # def application(self):
    #     return self.__application
    # def setApplication(self,x):
    #     self.__application = x
    # def citeN(self):
    #     return self.__citeN
    # def setCiteN(self,x):
    #     self.__citeN = x
    # def actual(self):
    #     return self.__actual
    # def setActual(self,x):
    #     self.__actual = x
    # def source(self):
    #     return self.__source
    # def setSource(self,x):
    #     self.__source = x
    # def nameNote(self):
    #     return self.__nameNote
    # def setNameNote(self,x):
    #     self.__nameNote = x
    # def generalNote(self):
    #     return self.__generalNote
    # def setGeneralNote(self, x):
    #     self.__generalNote = x
    # def __lt__(self, x):
    #     if self.name() == x.name():
    #         if self.context() == x.context():
    #             return self.application() < x.application()
    #         else:
    #             return self.context() < x.context()
    #     else:
    #         return self.name() < x.name()


# ----functions----
def report_error(logfile, outstr):
    print(outstr)
    logfile.write(outstr + "\n")


def get_references(logfile):
    """ read reference data """
    reflist = []
    year_dat = {}
    cite_done = {}
    # citation and species data from text
    with codecs.open("references_cites.txt", "r", "utf-8") as reffile:
        for line in reffile:
            line = line.replace("et al.", "<em>et al.</em>")
            ref = line.strip().split("\t")
            while len(ref) < 3:
                ref.append("")
            newref = ReferenceClass()
            newref.citation = ref[0]
            newref.cite_key = ref[1]
            newref.language = ref[2]
            # calculate publishing trend
            y = ref[0]
            y = y[y.find("(")+1:y.find(")")]
            if (y != "?") and (y.lower() != "in press"):
                if y[0] == "~":
                    y = y[1:]
                if len(y) > 4:
                    y = y[:4]
                y = int(y)
                if y in year_dat:
                    year_dat[y] += 1
                else:
                    year_dat[y] = 1
            cite_done[ref[1]] = [False, y]
            reflist.append(newref)

    # formatted references from html
    with codecs.open("references.html", "r", "utf-8") as reffile:
        c = -1
        for line in reffile:
            line = line.strip()
            if line.endswith("<p>"):
                line = line[:line.find("<p>")]
                line = line.replace("<i>", "<em>")
                line = line.replace("</i>", "</em>")
                c += 1
                newref = reflist[c]
                newref.formatted_html = line
    refdict = {}
    for ref in reflist:
        if ref.cite_key in refdict and ref.cite_key != "<pending>":
            report_error(logfile, "Duplicate reference key:" + ref.cite_key)
        refdict[ref.cite_key] = ref
    # citation info
    with open("citeinfo.txt", "r") as reffile:
        citelist = []
        got_header = False
        for line in reffile:
            if not got_header:
                got_header = True
            else:
                line = line.replace("\"\"", "\"")
                cite = line.strip().split("\t")
                for i, x in enumerate(cite):
                    if x.startswith("\"") and x.endswith("\""):
                        cite[i] = x[1:len(x)-1]
                newcite = CitationClass()
                newcite.cite_key = cite[0]
                newcite.name_key = cite[1]
                newcite.name = cite[2]
                newcite.common = cite[3]
                newcite.where = cite[4]
                newcite.context = cite[5]
                newcite.application = cite[6]
                newcite.cite_n = cite[7]
                newcite.actual = cite[8]
                newcite.source = cite[9]
                newcite.name_note = cite[10]
                newcite.general_note = cite[11]
                citelist.append(newcite)
                cite_done[cite[0]][0] = True

    cite_count = 0
    for y in year_dat:
        year_dat[y] = [year_dat[y], 0]
    for x in cite_done:
        c = cite_done[x]
        if c[0]:
            cite_count += 1
            if c[1] in year_dat:
                year_dat[c[1]][1] += 1
        # if c[1] in yearDat and c[0]:
        #    yearDat[c[1]][1] += 1    
    return reflist, refdict, citelist, year_dat, cite_count


def read_simple_file(fname):
    """ read data from generic flatfile """
    with open(fname, "r") as infile:
        # infile = codecs.open(fname, "r")
        splist = []
        got_header = False
        for line in infile:
            if got_header:
                line = line.strip()
                line = line.replace("\"\"", "\"")
                spinfo = line.split("\t")
                for i, x in enumerate(spinfo):
                    if x.startswith("\"") and x.endswith("\""):
                        spinfo[i] = x[1:len(x)-1]
                splist.append(spinfo)
            else:
                got_header = True
    return splist


def get_species():
    """ read data from species flatfile """
    tmplist = read_simple_file("species_info.txt")
    slist = []
    for s in tmplist:
        newspecies = SpeciesClass()
        newspecies.species = s[0]
        newspecies.subgenus = s[1]
        newspecies.type_species = s[2]
        newspecies.type_reference = s[3]
        newspecies.common = s[4]
        newspecies.commonext = s[5]
        newspecies.range = s[6]
        newspecies.range_references = s[7]
        newspecies.region = s[8]
        newspecies.status = s[9]
        newspecies.taxonid = s[10]
        newspecies.eolid = s[11]
        newspecies.inatid = s[12]
        newspecies.gbifid = s[13]
        slist.append(newspecies)
    return slist


def get_photos():
    """ read data from photo flatfile """
    tmplist = read_simple_file("photos.txt")
    plist = []
    for p in tmplist:
        newphoto = PhotoClass()
        newphoto.species = p[0]
        newphoto.n = p[1]
        newphoto.caption = p[2]
        plist.append(newphoto)
    return plist


def get_videos():
    """ read data from video flatfile """
    tmplist = read_simple_file("videos.txt")
    vlist = []
    for v in tmplist:
        newvideo = VideoClass()
        newvideo.species = v[0]
        newvideo.n = v[1]
        newvideo.activity = v[2]
        newvideo.caption = v[3]
        newvideo.length = v[4]
        newvideo.size = v[5]
        newvideo.format = v[6]
        newvideo.date_location = v[7]
        newvideo.author = v[8]
        newvideo.notes = v[9]
        vlist.append(newvideo)
    return vlist


def get_subgenera():
    """ read subgenera data """
    tmplist = read_simple_file("subgenera.txt")
    genlist = []
    for g in tmplist:
        newsubgenus = SubgenusClass()
        newsubgenus.subgenus = g[0]
        newsubgenus.author = g[1]
        newsubgenus.type_species = g[2]
        newsubgenus.notes = g[3]
        newsubgenus.taxonid = g[4]
        newsubgenus.eolid = g[5]
        genlist.append(newsubgenus)
    return genlist


def get_specific_names():
    """ read specific name data """
    tmplist = read_simple_file("specific_names.txt")
    splist = []
    for s in tmplist:
        newname = SpecificNameClass()
        newname.name = s[0]
        newname.variations = s[1]
        newname.synonym = s[2]
        newname.original_binomial = s[3]
        newname.priority_source = s[4]
        newname.meaning = s[5]
        newname.notes = s[6]
        splist.append(newname)
    return splist


def get_art():
    """ read art data """
    tmplist = read_simple_file("art.txt")
    artlist = []
    for a in tmplist:
        newart = ArtClass()
        newart.art_type = a[0]
        newart.cite_key = a[1]
        newart.author = a[2]
        newart.year = a[3]
        newart.title = a[4]
        newart.image = a[5]
        newart.ext = a[6]
        newart.species = a[7]
        newart.notes = a[8]
        artlist.append(newart)
    return artlist


def get_morphology():
    """ read morphology data """
    tmplist = read_simple_file("morphology.txt")
    morphlist = []
    for m in tmplist:
        newmorph = MorphologyClass()
        newmorph.character = m[0]
        newmorph.parent = m[1]
        newmorph.image = m[2]
        newmorph.caption = m[3]
        newmorph.description = m[4]
        morphlist.append(newmorph)
    return morphlist


# -----End input code---- #
def common_header_part1(outfile, title, indexpath):
    """ part 1 of the header for all html """
    outfile.write("<!DOCTYPE HTML>\n")
    outfile.write("<html lang=\"en\">\n")
    outfile.write("  <head>\n")
    outfile.write("    <meta charset=\"utf-8\" />\n")
    outfile.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n")
    outfile.write("    <title>" + title + "</title>\n")
    outfile.write("    <meta name=\"description\" content=\"Fiddler Crabs\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"128x128\" href=\"" + indexpath +
                  "favicon128.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"96x96\" href=\"" + indexpath +
                  "favicon96.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"72x72\" href=\"" + indexpath +
                  "favicon72.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"48x48\" href=\"" + indexpath +
                  "favicon48.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"32x32\" href=\"" + indexpath +
                  "favicon32.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"24x24\" href=\"" + indexpath +
                  "favicon24.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"16x16\" href=\"" + indexpath +
                  "favicon16.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" href=\"" + indexpath +
                  "apple-touch-icon-precomposed.png\">\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" sizes=\"72x72\" "
                  "href=\"" + indexpath + "apple-touch-icon-72x72-precomposed.png\">\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" sizes=\"114x114\" "
                  "href=\"" + indexpath + "apple-touch-icon-114x114-precomposed.png\">\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" sizes=\"144x144\" "
                  "href=\"" + indexpath + "apple-touch-icon-144x144-precomposed.png\">\n")
    outfile.write("    <link rel=\"stylesheet\" href=\"http://fonts.googleapis.com/css?family=Merienda+One|"
                  "Lora:400,700,400italic,700italic\" />\n")
    outfile.write("    <link rel=\"stylesheet\" href=\"" + indexpath + "uca_style.css\" />\n")
    # outfile.write("    <script src=\"https://use.fontawesome.com/3669ad7c2b.js\"></script>\n")
    outfile.write("    <link rel=\"stylesheet\" href=\"" + indexpath +
                  "images/font-awesome/css/font-awesome.min.css\">\n")
    outfile.write("    <link rel=\"author\" href=\"mailto:msr@asu.edu\" />\n")


def common_header_part2(outfile, indexpath, include_map):
    """ part 2 of the header for all html """
    outfile.write("  </head>\n")
    outfile.write("\n")
    if include_map:
        outfile.write("  <body onload=\"initialize()\">\n")
    else:
        outfile.write("  <body>\n")
    outfile.write("    <div id=\"home\">\n")
    outfile.write("      <a href=\"" + indexpath + "index.html\">Fiddler Crabs</a>\n")
    outfile.write("    </div>\n")


def common_species_html_header(outfile, title, indexpath, species):
    """ for species pages, insert the map scripts """
    common_header_part1(outfile, title, indexpath)
    outfile.write("    <script type=\"text/javascript\"\n")
    outfile.write("      src=\"http://maps.googleapis.com/maps/api/js?"
                  "key=AIzaSyAaITaFdh_own-ULkURNKtyeh2ZR_cpR74&sensor=false\">\n")
    outfile.write("    </script>\n")
    outfile.write("    <script type=\"text/javascript\">\n")
    outfile.write("      function initialize() {\n")
    outfile.write("        var mapOptions = {\n")
    outfile.write("          center: new google.maps.LatLng(0,0),\n")
    outfile.write("          zoom: 1,\n")
    outfile.write("          disableDefaultUI: true,\n")
    outfile.write("          panControl: false,\n")
    outfile.write("          zoomControl: true,\n")
    outfile.write("          mapTypeControl: true,\n")
    outfile.write("          scaleControl: false,\n")
    outfile.write("          streetViewControl: false,\n")
    outfile.write("          overviewMapControl: false,\n")
    outfile.write("          mapTypeId: google.maps.MapTypeId.TERRAIN\n")
    outfile.write("        };\n")
    # outfile.write("        var map = new google.maps.Map(document.getElementById(\"map_canvas_sp\"),mapOptions);\n")
    if species == "":
        outfile.write("        var map = new google.maps.Map(document.getElementById(\"map_canvas\"),mapOptions);\n")
        outfile.write("        var ctaLayer = new google.maps.KmlLayer(\"http://www.fiddlercrab.info/maps/uca.kmz\","
                      "{suppressInfoWindows: true});\n")
    else:
        outfile.write("        var map = new google.maps.Map(document.getElementById(\"map_canvas_sp\"),mapOptions);\n")
        outfile.write("        var ctaLayer = new google.maps.KmlLayer(\"http://www.fiddlercrab.info/maps/u_" +
                      species + ".kmz\",{suppressInfoWindows: true});\n")
    outfile.write("        ctaLayer.setMap(map);\n")
    outfile.write("      }\n")
    outfile.write("    </script>\n")
    common_header_part2(outfile, indexpath, True)


def common_html_header(outfile, title, indexpath):
    common_header_part1(outfile, title, indexpath)
    common_header_part2(outfile, indexpath, False)


def common_html_footer(outfile, indexpath):
    outfile.write("\n")
    outfile.write("    <footer>\n")
    outfile.write("       <figure id=\"footmap\"><script type=\"text/javascript\" "
                  "src=\"http://jf.revolvermaps.com/p.js\"></script><script type=\"text/javascript\">rm2d_ki101('0',"
                  "'150','75','5f9t1sywiez','ff0000',20);</script><figcaption>Visitors</figcaption></figure>\n")
    outfile.write("       <p id=\"citation\"><a href=\"" + indexpath + citeURL +
                  "\"><span class=\"fa fa-pencil\"></span> How to cite this site</a></p>\n")
    outfile.write("       <p id=\"contact\">Questions or comments about the site? Contact "
                  "<a href=\"mailto:msr@asu.edu\"><span class=\"fa fa-envelope-o\"></span> "
                  "Dr. Michael S. Rosenberg</a></p>\n")
    outfile.write("       <p id=\"copyright\">Copyright &copy; 2003&ndash;2016 All Rights Reserved</p>\n")
    outfile.write("    </footer>\n")
    outfile.write("  </body>\n")
    outfile.write("</html>\n")


def create_blank_index(fname):
    with open(fname, "w") as outfile:
        outfile.write("<!DOCTYPE HTML>\n")
        outfile.write("<html lang=\"en\">\n")
        outfile.write(" <head>\n")
        outfile.write("  <meta charset=\"utf-8\" />\n")
        outfile.write("  <title>n/a</title>\n")
        outfile.write("  <meta name=\"description\" content=\"n/a\" />\n")
        outfile.write(" </head>\n")
        outfile.write(" <body>\n")
        outfile.write(" </body>\n")
        outfile.write("</html>\n")


def format_reference(ref, logfile):
    if ref.cite_key == "<pending>":
        return "          <li>" + ref.formatted_html + "</li>\n"
    else:
        try:
            return ("          <li><a href=\"references/" + ref.cite_key + ".html\">" + ref.formatted_html +
                    "</a></li>\n")
        except LookupError:
            report_error(logfile, "missing label: " + ref.cite_key)


def reference_summary(nrefs, year_data, year_data_1900, cite_count, languages):
    with codecs.open(refsumURL, "w", "utf-8") as outfile:
        common_header_part1(outfile, "Fiddler Crab Reference Summary", "")
        outfile.write("    <script type=\"text/javascript\" src=\"https://www.google.com/jsapi\"></script>\n")
        outfile.write("    <script type=\"text/javascript\">\n")
        outfile.write("      google.load(\"visualization\", \"1\", {packages:[\"corechart\"]});\n")
        outfile.write("      google.setOnLoadCallback(drawChart);\n")
        outfile.write("      function drawChart() {\n")
        outfile.write("        var data1 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'Cumulative Publications'],\n")
        for y in year_data:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[2]) + "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        outfile.write("        var data2 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'Publications'],\n")
        for y in year_data:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[1]) + "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        """
        outfile.write("        var data3 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'Citations in DB', 'Pending'],\n")
        for y in yearData:
            outfile.write("          ['"+str(y[0])+"', "+str(y[3])+", "+str(y[1]-y[3])+"],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        """
        outfile.write("        var data4 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'Publications'],\n")
        for y in year_data_1900:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[1]) + "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        outfile.write("        var data5 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'Citations in DB', 'Pending'],\n")
        for y in year_data_1900:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[2]) + ", " + str(y[1]-y[2]) + "],\n")
        outfile.write("        ]);\n")

        outfile.write("        var data6 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Language', 'Count'],\n")
        langlist = list(languages.keys())
        langlist.sort()
        for l in langlist:
            outfile.write("          ['" + l + "', " + str(languages[l]) + "],\n")
        outfile.write("        ]);\n")

        outfile.write("\n")
        outfile.write("        var options1 = {\n")
        outfile.write("          title: \"Cumulative References by Year\", \n")
        outfile.write("          legend: { position: 'none' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        outfile.write("        var options2 = {\n")
        outfile.write("          title: \"References by Year\", \n")
        outfile.write("          legend: { position: 'none' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        """
        outfile.write("        var options3 = {\n")
        outfile.write("          title: \"References with Citation Data in Database\", \n")
        outfile.write("          legend: { position: 'bottom' },\n")
        outfile.write("          isStacked: true\n")
        outfile.write("        };\n")
        outfile.write("\n")
        """
        outfile.write("        var options4 = {\n")
        outfile.write("          title: \"References by Year (since 1900)\", \n")
        outfile.write("          legend: { position: 'none' },\n")
        outfile.write("          bar: { groupWidth: '80%' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        outfile.write("        var options5 = {\n")
        outfile.write("          title: \"References with Citation Data in Database (since 1900; all pre-1900 "
                      "literature is complete)\", \n")
        outfile.write("          legend: { position: 'bottom' },\n")
        outfile.write("          isStacked: true,\n")
        outfile.write("          bar: { groupWidth: '80%' }\n")
        outfile.write("        };\n")
        outfile.write("\n")

        outfile.write("        var options6 = {\n")
        outfile.write("          title: \"Primary Language of References\", \n")
        outfile.write("          titleTextStle: { fontSize: '16' },\n")
        # outfile.write("          isStacked: true,\n")
        # outfile.write("          bar: { groupWidth: '80%' }\n")
        outfile.write("        };\n")
        outfile.write("\n")

        outfile.write("        var chart = new google.visualization.LineChart"
                      "(document.getElementById('chart_div'));\n")
        outfile.write("        chart.draw(data1, options1);\n")
        outfile.write("        var chart2 = new google.visualization.ColumnChart"
                      "(document.getElementById('chart2_div'));\n")
        outfile.write("        chart2.draw(data2, options2);\n")
        # outfile.write("        var chart3 = new google.visualization.ColumnChart
        #               "(document.getElementById('chart3_div'));\n")
        # outfile.write("        chart3.draw(data3, options3);\n")
        outfile.write("        var chart4 = new google.visualization.ColumnChart"
                      "(document.getElementById('chart4_div'));\n")
        outfile.write("        chart4.draw(data4, options4);\n")
        outfile.write("        var chart5 = new google.visualization.ColumnChart"
                      "(document.getElementById('chart5_div'));\n")
        outfile.write("        chart5.draw(data5, options5);\n")
        outfile.write("        var chart6 = new google.visualization.PieChart"
                      "(document.getElementById('chart6_div'));\n")
        outfile.write("        chart6.draw(data6, options6);\n")
        outfile.write("      }\n")
        outfile.write("    </script>\n")
        common_header_part2(outfile, "", False)

        outfile.write("    <header>\n")
        outfile.write("      <h1>Summary of References</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"" + refURL +
                      "\"><span class=\"fa fa-list\"></span> Full Reference List</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      A summary of the references  in the database (last updated {}).\n".
                      format(datetime.date.isoformat(datetime.date.today())))
        outfile.write("      " + str(cite_count) + " of " + str(nrefs) +
                      " references  have had citation data recorded.\n")
        outfile.write("      See also the <a href=\"names/" + namesumURL + "\">name summary page</a> for information "
                      "on reference patterns to specific species.\n")
        outfile.write("    </p>\n")
        outfile.write("    <div id=\"chart6_div\"></div>\n")
        outfile.write("    <div id=\"chart2_div\"></div>\n")
        outfile.write("    <div id=\"chart4_div\"></div>\n")
        # outfile.write("    <div id=\"chart3_div\"></div>\n")
        outfile.write("    <div id=\"chart5_div\"></div>\n")
        outfile.write("    <div id=\"chart_div\"></div>\n")
        common_html_footer(outfile, "")

    
def references_to_html(reflist, logfile):
    with codecs.open(refURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Publications", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Publications</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"" + refsumURL +
                      "\"><span class=\"fa fa-line-chart\"></span> Reference/Citation Summary</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")

        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      Following is a fairly comprehensive list of papers, books, and theses that deal or refer "
                      "to fiddler crabs. The list currently contains {:0,} references (last updated {}). Many of these "
                      "papers (particularly the older ones) are primarily "
                      "taxonomic lists.\n".format(len(reflist), datetime.date.isoformat(datetime.date.today())))
        outfile.write("    </p>\n")
        outfile.write("    <p>\n")
        outfile.write("      The references can also be downloaded as "
                      "<a href=\"references/Uca_references.enlx\">compressed Endnote</a>, "
                      "<a href=\"references/Uca_references_RIS.txt\">RIS (text)</a>, or "
                      "<a href=\"references/Uca_references_RIS.xml\">RIS (XML)</a>.\n")
        outfile.write("    </p>\n")
        outfile.write("    <p>\n")
        outfile.write("      Linked references contain information on every name applied to fiddler crabs within "
                      "the publication, including context and the correct name as we currently understand it. These "
                      "data are in the process of being compiled (chronologically for all publications I have access "
                      "to a copy of), with most references still incomplete.\n")
        outfile.write("    </p>\n")
        outfile.write("    <p>\n")
        outfile.write("      In a list of this size, there are bound to be errors, omissions, and mistaken "
                      "inclusions. Please feel free to send me corrections.\n")
        outfile.write("    </p>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <div id=\"citation\">\n")
        outfile.write("        <ul>\n")
        # for i, ref in enumerate(reflist):
        for ref in reflist:
            outfile.write(format_reference(ref, logfile))
        outfile.write("        </ul>\n")
        outfile.write("      </div>\n")
        outfile.write("    </section>\n")
        common_html_footer(outfile, "")


def create_name_table(citelist):
    name_refs = {}
    for c in citelist:
        nstr = c.name_key
        if "." in nstr:
            nstr = nstr[:nstr.find(".")]
        i = int(nstr)
        if c.cite_key in name_refs:
            namelist = name_refs[c.cite_key]
        else:
            namelist = {}
        namelist[i] = c.name
        if "." in c.name_key:
            namelist[c.name_key] = [c.name, c.application]
        name_refs[c.cite_key] = namelist
    return name_refs


def match_num_ref(x, y):
    if (("." in x) and ("." in y)) or (("." not in x) and ("." not in y)):
        return x == y
    elif "." in x:
        return x[:x.find(".")] == y
    else:
        return y[:y.find(".")] == x


def update_cite_list(citelist):
    """ function to update correct species citations through cross-references to earlier works """
    for i, cite in enumerate(citelist):
        if cite.actual == "=":
            crossnames = {}
            for j in range(i):
                tmp = citelist[j]
                if (tmp.cite_key == cite.application) and match_num_ref(tmp.name_key, cite.cite_n):
                    cname = tmp.name
                    if tmp.actual in crossnames:
                        crossnames[tmp.actual] += 1
                    else:
                        crossnames[tmp.actual] = 1
            if len(crossnames) == 0:
                pass
            elif len(crossnames) == 1:
                for tmp in crossnames:
                    cite.actual = tmp
            else:
                mcnt = max(crossnames.values())

                keylist = []
                for key in crossnames:
                    if crossnames[key] == mcnt:
                        keylist.append(key)

                if len(keylist) == 1:
                    cite.actual = keylist[0]
                else:
                    cite_name = cite.name.lower()
                    while cite_name.find(" ") > -1:
                        cite_name = cite_name[cite_name.find(" ")+1:]
                    while cname.find(" ") > -1:
                        cname = cname[cname.find(" ")+1:]

                    if cite_name in keylist:
                        cite.actual = cite_name
                    elif cname in keylist:
                        cite.actual = cname
                    else:
                        cite.actual = keylist[0]

                if cite.name_note == ".":
                    cite.name_note = "in part"
                else:
                    cite.name_note = "in part; " + cite.name_note


def create_species_link(species, status, path):
    if status == "fossil":
        sc = fossilImage
    else:
        sc = ""
    return "<a href=\"" + path + "u_" + species + ".html\"><em class=\"species\">Uca " + species + "</em></a>" + sc


def format_name_string(x):
    """ properly emphasize species names, but not non-name signifiers """
    # get rid of [#] when present
    if "{" in x:
        x = x[:x.find("{")-1]
    if "var." in x.lower():
        p = x.lower().find("var.")
        return "<em class=\"species\">" + x[:p] + "</em> " + x[p:p+4] + " <em class=\"species\">" + x[p+4:] + "</em>"
    elif " var " in x.lower():
        p = x.lower().find(" var ")
        return "<em class=\"species\">" + x[:p] + "</em> " + x[p:p+4] + " <em class=\"species\">" + x[p+4:] + "</em>"
    elif "subsp." in x.lower():
        p = x.lower().find("subsp.")
        return "<em class=\"species\">" + x[:p] + "</em> " + x[p:p+6] + " <em class=\"species\">" + x[p+6:] + "</em>"
    elif " forme " in x.lower():
        p = x.lower().find(" forme ")
        return "<em class=\"species\">" + x[:p] + "</em> " + x[p:p+6] + " <em class=\"species\">" + x[p+6:] + "</em>"
    elif " f. " in x.lower():
        p = x.lower().find(" f. ")
        return "<em class=\"species\">" + x[:p] + "</em> " + x[p:p+3] + " <em class=\"species\">" + x[p+3:] + "</em>"
    else:
        return "<em class=\"species\">" + x + "</em>"


def name_to_filename(x):
    """ Convert a full species name into a valid file name """
    x = x.replace(" ", "_")
    x = x.replace("(", "")
    x = x.replace(")", "")
    x = x.replace(",", "")
    x = x.replace(".", "")
    x = x.replace("æ", "_ae_")
    x = x.replace("ö", "_o_")
    x = x.replace("œ", "_oe_")
    x = x.replace("ç", "_c_")
    x = x.replace("[", "_")
    x = x.replace("]", "_")
    return x


def clean_specific_name(x):
    """
    function to extract the specific names from binomials

    this is a list of terms that are not actual species names or specific names that have never been part of
    a fiddler genus
    """
    skip_list = ("sp.",
                 "spp.",
                 "var.",
                 "a",
                 "ete",
                 "panema",
                 "pagurus",
                 "quadratus",
                 "albidus",
                 "vociferans",
                 "(gelasimus)",
                 "raniformis",
                 "nigra",
                 "albicans",
                 "arenarius",
                 "raninus",
                 "serratus",
                 "spec.")

    if " " not in x:
        return ""
    else:
        if "{" in x:
            x = x[:x.find("{")-1]        
        y = x.split(" ")
        x = y[len(y)-1].lower()
        if x in skip_list or ("gruppe" in x):
            return ""
        else:
            return x.lower()


def outputn_name_table(is_name, outfile, itemlist, uniquelist, notecnt, comcnt, refdict, name_table, logfile):
    first_name = True
    ncols = 5
    if notecnt > 0:
        ncols += 1
    if comcnt > 0:
        ncols += 1

    for n in itemlist:
        outfile.write("    <tr>\n")
        if is_name:
            nref = n.cite_key
        else:
            nref = n.name
        if nref in uniquelist:
            if first_name:
                first_name = False
            else:
                outfile.write("      <td class=\"rowspacer\" colspan=\"" + str(ncols) + "\">&nbsp;</td>\n")
                outfile.write("    </tr>\n")
                outfile.write("    <tr>\n")

            if nref == ".":
                outfile.write("      <td>&nbsp;</td>\n")
            elif is_name:  # output citation
                crossref = refdict[nref]
                outfile.write("      <td><a href=\"../references/" + crossref.cite_key + ".html\">" +
                              crossref.citation + "</a></td>\n")
            else:  # output species name
                outfile.write("      <td><a href=\"../names/" + name_to_filename(nref) + ".html\">" +
                              format_name_string(nref) + "</a></td>\n")

            # common names
            if comcnt > 0:
                if n.common == ".":
                    outfile.write("      <td>&nbsp;</td>\n")
                else:
                    outfile.write("      <td>" + n.common + "</td>\n")
            outfile.write("      <td>" + n.where + "</td>\n")
            uniquelist = uniquelist - {nref}
        else:
            outfile.write("      <td>&nbsp;</td>\n")
            if comcnt > 0:
                outfile.write("      <td>&nbsp;</td>\n")
            outfile.write("      <td>&nbsp;</td>\n")
        # applies to...
        if n.context == "location":
            outfile.write("      <td>location: " + n.application + "</td>\n")
        elif n.context == "citation":
            if n.application in refdict:
                crossref = refdict[n.application]
                if n.application in name_table:
                    nstr = n.cite_n
                    if nstr == "0":
                        outfile.write("      <td>citation: <a href=\"../references/" + crossref.cite_key +
                                      ".html\">" + crossref.citation + "</a></td>\n")
                    else:
                        if "." in nstr:
                            try:
                                extraref = " [" + name_table[n.application][nstr][1] + "]"
                                refname = name_table[n.application][nstr][0]
                            except LookupError:
                                if is_name:  # only print errors on one pass
                                    report_error(logfile, "Error in citation: " +
                                                 n.cite_key + " cites" + nstr +
                                                 " in " + n.application)
                                extraref = ""
                                refname = ""
                        else:
                            extraref = ""                                
                            # print(nstr, n.cite_key, n.application)
                            refname = name_table[n.application][int(nstr)]
                        outfile.write("      <td>citation: <a href=\"../references/" + crossref.cite_key +
                                      ".html\">" + crossref.citation + "</a> → " + format_name_string(refname) +
                                      extraref + "</td>\n")
                else:
                    outfile.write("      <td>citation: <a href=\"../references/" + crossref.cite_key +
                                  ".html\">" + crossref.citation + "</a></td>\n")
            else:
                outfile.write("      <td>citation: " + n.application +
                              "</td>\n")
                if is_name:  # only print on one pass
                    report_error(logfile, "Citation not in DB: " +
                                 n.cite_key + " cites " + n.application)
        elif n.context == "specimen":
            if n.application == "?":
                outfile.write("      <td>specimen: unknown locality</td>\n")
            else:
                outfile.write("      <td>specimen: " + n.application +
                              "</td>\n")
        elif n.context == "unpublished":
            outfile.write("      <td>unpublished name <em class=\"species\">" +
                          n.application + "</em></td>\n")
        else:  # "n/a"
            outfile.write("      <td>&nbsp;</td>\n")

        # accepted species name                                
        if n.actual == "?":
            outfile.write("      <td>?</td>\n")
        elif n.actual in {".", "="}:
            outfile.write("      <td>TBD</td>\n")
        elif n.actual == "n/a":
            outfile.write("      <td>&nbsp;</td>\n")                    
        elif n.actual[0] == ">":
            outfile.write("      <td><em class=\"species\">" + n.actual[1:] +
                          "</em></td>\n")
        else:
            outfile.write("      <td><a href=\"../u_" + n.actual +
                          ".html\"><em class=\"species\">Uca " + n.actual +
                          "</em></a></td>\n")

        # source of accepted species
        if n.source == ".":  # currently not listed
            outfile.write("      <td>&nbsp;</td>\n")                   
        elif n.source == "<":  # original name retained
            outfile.write("      <td>Original</td>\n")                                
        elif n.source == "=":  # automatically computer
            # outfile.write("      <td>Computed</td>\n")
            # outfile.write("      <td style=\"text-align: center\"><img src=\"../images/gears.png\" alt=\"Computed\" "
            #               "title=\"Computed\" /></td>\n")
            outfile.write("      <td><span class=\"fa fa-gears\"></span> Computed</td>\n")
        elif n.source in refdict:  # another reference
            crossref = refdict[n.source]
            outfile.write("      <td><a href=\"../references/" +
                          crossref.cite_key + ".html\">" +
                          crossref.citation + "</a></td>\n")
        else:  # should start with a >
            outfile.write("      <td>" + n.source[1:] + "</td>\n")

        # notes
        if notecnt > 0:
            if n.name_note == ".":
                outfile.write("      <td>&nbsp;</td>\n")
            else:
                outfile.write("      <td>" + n.name_note + "</td>\n")
        outfile.write("    </tr>\n")
    outfile.write("    </table>\n")
    

def reference_pages(reflist, refdict, citelist, logfile):
    create_blank_index("references/index.html")
    name_table = create_name_table(citelist)
    update_cite_list(citelist)
    for ref in reflist:
        if ref.cite_key != "<pending>":
            with codecs.open("references/" + ref.cite_key + ".html", "w", "utf-8") as outfile:
                common_html_header(outfile, ref.citation, "../")
                outfile.write("    <header>\n")
                outfile.write("      <h1>" + ref.citation + "</h1>\n")
                outfile.write("      <h2>" + ref.formatted_html + "</h2>\n")
                outfile.write("      <nav>\n")
                outfile.write("        <ul>\n")
                outfile.write("          <li><a href=\"../" + refURL +
                              "\"><span class=\"fa fa-list\"></span> Full Reference List</a></li>\n")
                outfile.write("        </ul>\n")
                outfile.write("      </nav>\n")
                outfile.write("    </header>\n")
                outfile.write("\n")
                # find names for this citation
                names = []
                cites_to = []
                for c in citelist:
                    if c.cite_key == ref.cite_key:
                        names.append(c)
                    if c.application == ref.cite_key:
                        cites_to.append(c)
                started_note = False
                comcnt = 0
                notecnt = 0
                uniquenames = set()
                for n in names:
                    if n.general_note != ".":
                        if not started_note:
                            outfile.write("    <p>\n")
                            started_note = True
                        outfile.write("      " + n.general_note + "\n")
                    if n.common != ".":
                        comcnt += 1
                    if n.name_note != ".":
                        notecnt += 1
                    uniquenames = uniquenames | {n.name}
                if started_note:
                    outfile.write("    </p>\n")

                # write name table
                outfile.write("    <h3>Names Appearing in this Publication</h3>\n")
                if len(names) > 0:
                    outfile.write("    <table class=\"citetable\">\n")
                    outfile.write("      <tr>\n")
                    outfile.write("        <th>Name Used</th>\n")
                    if comcnt > 0:
                        outfile.write("        <th>Common Name(s)</th>\n")
                    outfile.write("        <th>Where</th>\n")
                    outfile.write("        <th>Applied to...</th>\n")
                    outfile.write("        <th>Accepted Species</th>\n")
                    outfile.write("        <th>Source of Accepted</th>\n")
                    if notecnt > 0:
                        outfile.write("        <th>Note(s)</th>\n")
                    outfile.write("      </tr>\n")
                    names.sort()
                    outputn_name_table(False, outfile, names, uniquenames, notecnt, comcnt, refdict, name_table,
                                       logfile)
                else:
                    outfile.write("    Data not yet available.\n")

                if len(cites_to) > 0:
                    outfile.write("    <h3>This Publication is Cited By</h3>\n")
                    outfile.write("    <p>\n")
                    cs = set()
                    for c in cites_to:
                        if c.cite_key in refdict:
                            crossref = refdict[c.cite_key]
                            cs = cs | {"<a href=\"" + crossref.cite_key + ".html\">" + crossref.citation + "</a>"}
                        else:
                            cs = cs | {c.cite_key}
                    cl = []
                    for x in cs:
                        cl.append(x)
                    cl.sort()
                    outfile.write("     " + ", ".join(cl) + "\n")
                    outfile.write("    </p>\n")
                else:
                    outfile.write("    <p>\n")
                outfile.write("    </p>\n")

                common_html_footer(outfile, "../")


def clean_name(x):
    """ function to clean up names so that variation such as punctuation does not prevent a match """
    x = x.replace(", var.", " var.")
    if "{" in x:
        x = x[:x.find("{")-1]
    return x


def create_binomial_name_page(name, namefile, refdict, citelist, name_table, species_name, logfile):
    """ create a page listing all citations using a specific binomial """
    with codecs.open("names/" + namefile + ".html", "w", "utf-8") as outfile:
        common_html_header(outfile, name, "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1>" + format_name_string(name) + "</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        if species_name != "":
            outfile.write("          <li><a href=\"sn_" + species_name +
                          ".html\"><span class=\"fa fa-window-minimize\"></span> " + format_name_string(species_name) +
                          "</a></li>\n")
        outfile.write("          <li><a href=\"index.html\"><span class=\"fa fa-list\"></span> "
                      "Full Name Index</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")

        # find citations for this name
        cites = []
        for c in citelist:
            clean = clean_name(c.name)
            if clean.lower() == name.lower():
                cites.append(c)
        comcnt = 0
        notecnt = 0
        uniquecites = set()
        for c in cites:
            if c.common != ".":
                comcnt += 1
            if c.name_note != ".":
                notecnt += 1
            uniquecites = uniquecites | {c.cite_key}

        # write name table
        outfile.write("    <h3>Publications Using this Name</h3>\n")
        outfile.write("    <table class=\"citetable\">\n")
        outfile.write("      <tr>\n")
        outfile.write("        <th>Citation</th>\n")
        if comcnt > 0:
            outfile.write("        <th>Common Name(s)</th>\n")
        outfile.write("        <th>Where</th>\n")
        outfile.write("        <th>Applied to...</th>\n")
        outfile.write("        <th>Accepted Species</th>\n")
        outfile.write("        <th>Source of Accepted</th>\n")
        if notecnt > 0:
            outfile.write("        <th>Note(s)</th>\n")
        outfile.write("      </tr>\n")
        outputn_name_table(True, outfile, cites, uniquecites, notecnt, comcnt, refdict, name_table, logfile)
        outfile.write("    <p>\n")
        outfile.write("    </p>\n")
        common_html_footer(outfile, "../")


def create_specific_name_page(name, binomial_names, refdict, logfile):
    """ create a page with the history of a specific name """
    with codecs.open("names/sn_" + name.name + ".html", "w", "utf-8") as outfile:
        common_html_header(outfile, name.name, "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1>" + format_name_string(name.name) + "</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"index.html\"><span class=\"fa fa-list\"></span> "
                      "Full Name Index</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"topspsection\">\n")
        outfile.write("      <h3>History</h3>\n")
        outfile.write("      <dl>\n")
        if name.synonym != ".":
            if name.synonym in name.variations:
                outfile.write("        <dt>Species</dt>\n")
            else:
                outfile.write("        <dt>Primary Senior Synonym</dt>\n")
            if name.synonym == "?":
                outfile.write("          <dd>Unknown</dd>\n")
            elif name.synonym.startswith(">"):
                outfile.write("          <dd><em class=\"species\">" +
                              name.synonym[1:] + "</em></dd>\n")
            else:
                outfile.write("          <dd>" +
                              create_species_link(name.synonym, "", "../") +
                              "</dd>\n")
        outfile.write("        <dt>Original Usage</dt>\n")
        outfile.write("          <dd>" +
                      format_name_string(name.original_binomial) + "</dd>\n")
        outfile.write("        <dt>Original Source with Priority</dt>\n")
        refname = ""
        if name.priority_source != ".":
            try:
                ref = refdict[name.priority_source]
                refname = ref.formatted_html
            except LookupError:
                # print(name.priority_source)
                report_error(logfile, name.priority_source)
        else:
            refname = "unknown"
        outfile.write("          <dd>" + refname + "</dd>\n")
        outfile.write("        <dt>Derivation</dt>\n")
        if name.meaning == ".":
            outfile.write("          <dd>unknown</dd>\n")
        else:
            outfile.write("          <dd>" + name.meaning + "</dd>\n")
        outfile.write("      <dl>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")
        if name.notes != ".":
            outfile.write("    <section class=\"spsection\">\n")
            outfile.write("      <h3>Notes/Comments</h3>\n")
            outfile.write("      <p>\n")
            outfile.write("        " + name.notes + "\n")
            outfile.write("      </p>\n")
            outfile.write("    </section>\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h3>Binomials Using this Specific Name</h3>\n")
        outfile.write("      <ul>\n")
        for n in binomial_names:
            x = clean_specific_name(n)
            tmpnamelist = name.variations.split(";")
            if (x != "") and (x in tmpnamelist):
                namefile = name_to_filename(n)
                outfile.write("      <li><a href=\"" + namefile + ".html\">" +
                              format_name_string(n) + "</a></li>\n")
        outfile.write("      </ul>\n")
        outfile.write("    </section>\n")

        common_html_footer(outfile, "../")


def match_specific_name(name, specific_names):
    """ match the specific name from a binomial to the list of accepted specific names """
    c = clean_specific_name(name)
    if c == "":
        return c
    else:
        y = ""
        for x in specific_names:
            matchlist = x.variations.split(";")
            if c in matchlist:
                y = x.name
        return y


def create_name_summary(binomial_year_cnts, specific_year_cnts, species_refs):
    with codecs.open("names/" + namesumURL, "w", "utf-8") as outfile:
        common_header_part1(outfile, "Fiddler Crab Name Summary", "../")
        outfile.write("    <script type=\"text/javascript\" src=\"https://www.google.com/jsapi\"></script>\n")
        outfile.write("    <script type=\"text/javascript\">\n")
        outfile.write("      google.load(\"visualization\", \"1\", {packages:[\"corechart\"]});\n")
        outfile.write("      google.setOnLoadCallback(drawChart);\n")
        outfile.write("      function drawChart() {\n")
        miny = 2014
        maxy = 0
        for y in binomial_year_cnts:
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        byears = []
        c = 0
        for y in range(miny, maxy+1):
            if y in binomial_year_cnts:
                c = c + binomial_year_cnts[y]
                byears.append([y, binomial_year_cnts[y], c])
            else:
                byears.append([y, 0, c])

        miny = 2014
        maxy = 0
        for y in specific_year_cnts:
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
        syears = []
        c = 0
        for y in range(miny, maxy+1):
            if y in specific_year_cnts:
                c = c + specific_year_cnts[y]
                syears.append([y, specific_year_cnts[y], c])
            else:
                syears.append([y, 0, c])

        outfile.write("        var data1 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'Cumulative Unique Binomial/Compound Names'],\n")
        for y in byears:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[2]) + "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        outfile.write("        var data2 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'New Unique Binomial/Compound Names'],\n")
        for y in byears:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[1]) + "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        outfile.write("        var data3 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'Cumulative Unique Specific Names'],\n")
        for y in syears:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[2]) + "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        outfile.write("        var data4 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Year', 'New Unique Specific Names'],\n")
        for y in syears:
            outfile.write("          ['" + str(y[0]) + "', " + str(y[1]) + "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        outfile.write("        var data5 = google.visualization.arrayToDataTable([\n")
        outfile.write("          ['Species', 'Referring References'],\n")
        tmpslist = list(species_refs.keys())
        tmpslist.sort()
        for s in tmpslist:
            outfile.write("          ['" + s + "', " + str(len(species_refs[s])) +
                          "],\n")
        outfile.write("        ]);\n")
        outfile.write("\n")
        outfile.write("        var options1 = {\n")
        outfile.write("          title: \"Cumulative Unique Binomial/Compound Names by Year\", \n")
        outfile.write("          legend: { position: 'none' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        outfile.write("        var options2 = {\n")
        outfile.write("          title: \"Unique Binomial/Compound Names by Year\", \n")
        outfile.write("          legend: { position: 'none' },\n")
        outfile.write("          bar: { groupWidth: '80%' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        outfile.write("        var options3 = {\n")
        outfile.write("          title: \"Cumulative Unique Specific Names by Year\", \n")
        outfile.write("          legend: { position: 'none' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        outfile.write("        var options4 = {\n")
        outfile.write("          title: \"Unique Specific Names by Year\", \n")
        outfile.write("          legend: { position: 'none' },\n")
        outfile.write("          bar: { groupWidth: '80%' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        outfile.write("        var options5 = {\n")
        outfile.write("          title: \"Number of References Referring to Accepted Species\", \n")
        outfile.write("          legend: { position: 'none' },\n")
        outfile.write("          bar: { groupWidth: '80%' }\n")
        outfile.write("        };\n")
        outfile.write("\n")
        outfile.write("        var chart1 = new google.visualization.LineChart(document.getElementById"
                      "('namechart1_div'));\n")
        outfile.write("        chart1.draw(data1, options1);\n")
        outfile.write("        var chart2 = new google.visualization.ColumnChart(document.getElementById"
                      "('namechart2_div'));\n")
        outfile.write("        chart2.draw(data2, options2);\n")
        outfile.write("        var chart3 = new google.visualization.LineChart(document.getElementById"
                      "('namechart3_div'));\n")
        outfile.write("        chart3.draw(data3, options3);\n")
        outfile.write("        var chart4 = new google.visualization.ColumnChart(document.getElementById"
                      "('namechart4_div'));\n")
        outfile.write("        chart4.draw(data4, options4);\n")
        outfile.write("        var chart5 = new google.visualization.ColumnChart(document.getElementById"
                      "('namechart5_div'));\n")
        outfile.write("        chart5.draw(data5, options5);\n")
        outfile.write("      }\n")
        outfile.write("    </script>\n")
        common_header_part2(outfile, "", False)
        outfile.write("    <header>\n")
        outfile.write("      <h1>Summary of Names</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\".\"><span class=\"fa fa-list\"></span> Name Index</a></li>\n")
        outfile.write("          <li><a href=\"../" + speciesURL +
                      "\"><span class=\"fa fa-check-circle\"></span> Accepted Species</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      A summary of the names in the database (last updated {}).\n".
                      format(datetime.date.isoformat(datetime.date.today())))
        outfile.write("      Most of these data are only based on <a href=\"../" + refsumURL +
                      "\">references whose citation data is already included in the database</a>.\n")
        # outfile.write("      "+str(citeCount)+" of "+str(nrefs)+" references  have had citation data recorded.\n")
        outfile.write("    </p>\n")
        outfile.write("    <div id=\"namechart1_div\"></div>\n")
        outfile.write("    <div id=\"namechart2_div\"></div>\n")
        outfile.write("    <div id=\"namechart3_div\"></div>\n")
        outfile.write("    <div id=\"namechart4_div\"></div>\n")
        outfile.write("    <div id=\"namechart5_div\"></div>\n")
        common_html_footer(outfile, "../")


def index_name_pages(refdict, citelist, specific_names, species_refs, logfile):
    """ create an index of binomials and specific names """
    name_table = create_name_table(citelist)
    unique_names = list()
    nameset = set()
    binomial_year_cnts = {}
    for c in citelist:
        if c.name != ".":
            clean = clean_name(c.name)
            if not clean.lower() in nameset:
                nameset = nameset | {clean.lower()}
                unique_names.append(clean)
                y = refdict[c.cite_key].citation
                y = y[y.find("(")+1:y.find(")")]
                if (y != "?") and (y.lower() != "in press"):
                    if y[0] == "~":
                        y = y[1:]
                    if len(y) > 4:
                        y = y[:4]
                    y = int(y)
                    if y in binomial_year_cnts:
                        binomial_year_cnts[y] += 1
                    else:
                        binomial_year_cnts[y] = 1
    unique_names.sort(key=lambda s: s.lower())

    # create name index
    with codecs.open("names/index.html", "w", "utf-8") as outfile:
        common_html_header(outfile, "Name Index", "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Name Index</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"" + namesumURL +
                      "\"><span class=\"fa fa-line-chart\"></span> Name Summary</a></li>\n")
        outfile.write("          <li><a href=\"../" + speciesURL +
                      "\"><span class=\"fa fa-check-circle\"></span> Accepted Species</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("    <p>\n")
        outfile.write("      This is an index of every scientific name (including all alternate spellings) which have "
                      "been applied to fiddler crabs or placed in the fiddler crab genus.\n")
        outfile.write("    </p>\n")
        outfile.write("    <p>\n")
        outfile.write("      For the binomials, every publication which used that name is provided, as well as the "
                      "best estimate as to which species, as we understand them today, the author was actually "
                      "referring.\n")
        outfile.write("    </p>\n")
        outfile.write("    <p>\n")
        outfile.write("      For the specific names, only the primary spelling is listed below, but all alternate "
                      "spellings and inclusive binomials are included on the linked page, as well as general "
                      "information on the status of each specific name.\n")
        outfile.write("    </p>\n")
        outfile.write("    <div class=\"namecol\">\n")
        outfile.write("      <h3>Binomials (and other Compound Names)</h3>\n")
        outfile.write("      <ul>\n")
        outfile.write("\n")
        for name in unique_names:
            sname = match_specific_name(name, specific_names)
            namefile = name_to_filename(name)
            outfile.write("        <li><a href=\"" + namefile + ".html\">" + format_name_string(name) + "</a></li>\n")
            create_binomial_name_page(name, namefile, refdict, citelist, name_table, sname, logfile)
        outfile.write("      </ul>\n")
        outfile.write("    </div>\n")
        outfile.write("    <div class=\"namecol\">\n")
        outfile.write("      <h3>Specific Names</h3>\n")
        outfile.write("      <ul>\n")
        outfile.write("\n")
        specific_year_cnts = {}
        for name in specific_names:
            outfile.write("        <li><a href=\"sn_" + name.name + ".html\">" +
                          format_name_string(name.name) + "</a></li>\n")
            create_specific_name_page(name, unique_names, refdict, logfile)
            tmpkey = name.priority_source
            if tmpkey != ".":
                y = refdict[tmpkey].citation
                y = y[y.find("(")+1:y.find(")")]
                if (y != "?") and (y.lower() != "in press"):
                    if y[0] == "~":
                        y = y[1:]
                    if len(y) > 4:
                        y = y[:4]
                    y = int(y)
                    if y in specific_year_cnts:
                        specific_year_cnts[y] += 1
                    else:
                        specific_year_cnts[y] = 1
        outfile.write("      </ul>\n")
        outfile.write("    </div>\n")
        common_html_footer(outfile, "../")
    create_name_summary(binomial_year_cnts, specific_year_cnts, species_refs)
    return unique_names


def specific_name_pages(citelist, specific_names, logfile):
    """ produces a list of specific names not in the accepted list """
    unique_names = list()
    nameset = set()
    for c in citelist:
        if c.name != ".":
            clean = clean_specific_name(c.name)
            if (not (clean in nameset)) and (clean != ""):
                nameset = nameset | {clean}
                unique_names.append(clean)
    unique_names.sort()
    for n in unique_names:
        is_found = False
        for s in specific_names:
            if n in s.variations:
                is_found = True
        if not is_found:
            report_error(logfile, "Missing specific name: " + n)


def create_map_html(species):
    """ output geographic ranges to HTML """
    regions = ("Eastern Atlantic",
               "Western Atlantic",
               "Eastern Pacific",
               "Indo-West Pacific")
    with codecs.open(mapURL, "w", "utf-8") as outfile:
        common_species_html_header(outfile, "Fiddler Crab Geographic Ranges", "", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Geographic Ranges</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"topspsection\">\n")
        outfile.write("      <p class=\"map_section\">\n")
        outfile.write("        <div id=\"map_canvas\"></div>\n")
        outfile.write("      </p>\n")
        outfile.write("      <p>\n")
        outfile.write("        The above map shows the approximate density of species richness, with denser color "
                      "where more species are found. The range for each individual species can be found on its page, "
                      "including specific citations for the range information. Below, species are grouped by broad "
                      "geographic region.\n")
        outfile.write("      </p>\n")
        outfile.write("    </section>\n")
        for r in regions:
            outfile.write("\n")
            outfile.write("    <section class=\"spsection\">\n")
            outfile.write("      <h2>" + r + "</h2>\n")
            outfile.write("      <ul id=\"splist\">\n")
            for s in species:
                if s.region == r:
                    if s.status != "fossil":
                        outfile.write("        <li>" +
                                      create_species_link(s.species, "", "") +
                                      "</li>\n")
            outfile.write("      </ul>\n")
            outfile.write("    </section>\n")
        common_html_footer(outfile, "")


def create_common_names_html():
    """ output common names to HTML """
    with codecs.open("common_names.txt", "r", "utf-8") as infile:
        lines = infile.readlines()
    with codecs.open(commonURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Common Names of Fiddler Crabs", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Common Names of Fiddler Crabs</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      Following is a summery of common names for crabs in the genus "
                      "<em class=\"species\">Uca</em>. See <a href=\"uca_species.html\">individual species</a> for "
                      "more information on the common names of a particular species.\n")
        outfile.write("    </p>\n")
        outfile.write("    <dl class=\"common\">\n")
        first_level = True
        for line in lines[1:]:
            line = line.strip()
            if line != "":
                text_level, text = line.split("\t")
                if text_level == "T":
                    if not first_level:
                        outfile.write("        </dd>\n")
                    else:
                        first_level = False
                    outfile.write("      <dt>" + text + "</dt>\n")
                    outfile.write("        <dd>\n")
                elif text_level == "P":
                    outfile.write("          <p>\n")
                    outfile.write("            " + text + "\n")
                    outfile.write("          </p>\n")
                elif text_level == "B":
                    outfile.write("          <blockquote>\n")
                    outfile.write("            " + text + "\n")
                    outfile.write("          </blockquote>\n")
        outfile.write("        </dd>\n")
        outfile.write("    </dl>\n")
        common_html_footer(outfile, "")


def connect_refs_to_species(species, citelist):
    """ create list of references for each species """
    # create dictionary with empty reference lists
    species_refs = {}
    for s in species:
        reflist = set()
        species_refs[s.species] = reflist
    # go through all citations
    for c in citelist:
        if c.actual in species_refs:
            reflist = species_refs[c.actual]
            reflist = reflist | {c.cite_key}
            species_refs[c.actual] = reflist
    return species_refs


def write_species_list(specieslist):
    """ output species index HTML """
    with codecs.open(speciesURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Species", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Species</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>")
        nf = 0
        for s in specieslist:
            if s.status == "fossil":
                nf += 1
        tstr = ("      The following lists all {} of the currently recognized species of fiddler crab, as well as "
                "{} fossil species (marked with" + fossilImage + ").\n")
        outfile.write(tstr.format(len(specieslist) - nf, nf))
        outfile.write("      See the <a href=\"/names\">complete name index</a> for alternate species names and "
                      "spellings.\n")
        outfile.write("    </p>")
        outfile.write("\n")
        outfile.write("    <ul id=\"splist\">\n")
        for species in specieslist:
            outfile.write("      <li>" + create_species_link(species.species, species.status, "") + "</li>\n")
        outfile.write("    </ul>\n")
        common_html_footer(outfile, "")


def write_species_photo_page(fname, species, common_name, caption, pn, pspecies):
    """ create page for a specific photo """
    with open(fname, "w") as outfile:
        if ";" in pspecies:
            spname = pspecies.replace(";", "_")
            ptitle = "Uca " + pspecies.replace(";", " & Uca ")
            is_multi = True
        else:
            spname = species
            ptitle = "Uca " + species
            is_multi = False
        common_html_header(outfile, ptitle + " Photo", "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1><em class=\"species\">" + ptitle + "</em> Photo</h1>\n")
        if not is_multi:
            if common_name != "#":
                outfile.write("      <h2>" + common_name + "</h2>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        if is_multi:
            splist = pspecies.split(";")
            for s in splist:
                outfile.write("          <li><a href=\"../u_" + s + ".html\"><em class=\"species\">Uca " + s +
                              "</em> page</a></li>\n")
        else:
            outfile.write("          <li><a href=\"../u_" + species + ".html\">Species page</a></li>\n")
        outfile.write("          <li><a href=\"../" + photoURL + "\">All species photos</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <figure class=\"fullpic\">\n")
        outfile.write("      <picture><img src=\"U_" + spname + format(pn, "0>2") + ".jpg\" alt=\"Uca " + species +
                      "\" title=\"Uca " + species + "\" /></picture>\n")
        outfile.write("      <figcaption>" + caption + "</figcaption>\n")
        outfile.write("    </figure>\n")
        common_html_footer(outfile, "../")


def write_species_video_page(fname, species, common_name, video, vn):
    """ create page for a specific video """
    with codecs.open(fname, "w", "utf-8") as outfile:
        if ";" in video.species:
            spname = video.species.replace(";", "_")
            vtitle = "Uca " + video.species.replace(";", " & Uca ")
            is_multi = True
        else:
            spname = species
            vtitle = "Uca " + species
            is_multi = False
        common_html_header(outfile, vtitle + " Video", "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1><em class=\"species\">" + vtitle + "</em> Video</h1>\n")
        if not is_multi:
            outfile.write("      <h2>" + common_name + "</h2>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        if is_multi:
            splist = video.species.split(";")
            for s in splist:
                outfile.write("          <li><a href=\"../u_" + s + ".html\"><em class=\"species\">Uca " + s +
                              "</em> page</a></li>\n")
        else:
            outfile.write("          <li><a href=\"../u_" + species + ".html\">Species page</a></li>\n")
        outfile.write("          <li><a href=\"../" + videoURL + "\">All species videos</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <h2>" + video.caption + "</h2>\n")
        outfile.write("    <video width=\"352\" height=\"240\" controls>\n")
        outfile.write("      <source src=\"U_" + spname + format(vn, "0>2") + "." + video.format.lower() +
                      "\" type=\"video/mp4\">\n")
        outfile.write("      Your browser does not support the video tag.\n")
        outfile.write("    </video>\n")
        outfile.write("    <p class=\"vidcaption\">\n")
        outfile.write("      " + video.date_location + "<br />\n")
        outfile.write("      " + video.author + "<br />\n")
        outfile.write("    </p>\n")
        outfile.write("    <dl class=\"viddetails\">\n")
        outfile.write("      <dt>Length</dt>\n")
        outfile.write("        <dd>" + video.length + "</dd>\n")
        outfile.write("      <dt>Size</dt>\n")
        outfile.write("        <dd>" + video.size + "</dd>\n")
        outfile.write("      <dt>Format</dt>\n")
        outfile.write("        <dd>" + video.format + "</dd>\n")
        if video.notes != "#":
            outfile.write("      <dt>Notes</dt>\n")
            outfile.write("        <dd>" + video.notes + "</dd>\n")
        outfile.write("    </dl>\n")
        common_html_footer(outfile, "../")


def write_species_page(species, references, specific_names, all_names, photos, videos, artlist, sprefs, refdict,
                       logfile):
    """ create the master page for a species """
    if species.status == "fossil":
        is_fossil = True
    else:
        is_fossil = False
    with codecs.open("u_" + species.species + ".html", "w", "utf-8") as outfile:
        if is_fossil:
            common_html_header(outfile, "Uca " + species.species + " / Fossil", "")
        else:
            common_species_html_header(outfile, "Uca " + species.species + " / " + species.common, "",
                                       species.species)
        outfile.write("    <header>\n")
        if is_fossil:
            sc = fossilImage
        else:
            sc = ""
        outfile.write("      <h1 class=\"species\">Uca " + species.species + sc + "</h1>\n")
        if is_fossil:
            outfile.write("      <h2>Fossil</h2>\n")
        else:
            outfile.write("      <h2>" + species.common + "</h2>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"#type\">Type</a></li>\n")
        outfile.write("          <li><a href=\"#info\"><span class=\"fa fa-info-circle\"></span> "
                      "Information</a></li>\n")
        outfile.write("          <li><a href=\"#pics\"><span class=\"fa fa-camera\"></span> Photos</a></li>\n")
        if not is_fossil:
            outfile.write("          <li><a href=\"#video\"><span class=\"fa fa-video-camera\"></span> "
                          "Video</a></li>\n")
            outfile.write("          <li><a href=\"#art\"><span class=\"fa fa-paint-brush\"></span> Art</a></li>\n")
        outfile.write("          <li><a href=\"#refs\"><span class=\"fa fa-book\"></span> References</a></li>\n")
        outfile.write("          <li><a href=\"uca_species.html\"><span class=\"fa fa-list\"></span> "
                      "Species List</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"topspsection\">\n")
        outfile.write("      <h2><a name=\"type\">Type Description</a></h2>\n")
        outfile.write("      <dl>\n")
        outfile.write("        <dt><em class=\"species\">" + species.type_species + "</em></dt>\n")
        tref = refdict[species.type_reference]
        outfile.write("        <dd>" + tref.formatted_html + "</dd>\n")
        outfile.write("      </dl>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"info\"><span class=\"fa fa-info-circle\"></span> Information</a></h2>\n")
        outfile.write("      <dl>\n")
        outfile.write("       <dt>Subgenus</dt>\n")
        outfile.write("         <dd><a href=\"" + systURL + "#" + species.subgenus + "\"><em class=\"species\">" +
                      species.subgenus + "</em></a></dd>\n")
        if not is_fossil:
            outfile.write("       <dt>Common Names</dt>\n")
            outfile.write("         <dd>" + species.commonext + "</dd>\n")

        # Synonyms
        synlist = []
        for spname in specific_names:
            if spname.synonym == species.species:
                varlist = spname.variations.split(";")
                for varname in varlist:
                    for uname in all_names:
                        cleanname = clean_specific_name(uname)
                        if varname == cleanname:
                            synlist.append(uname)
        if len(synlist) > 0:
            synlist.sort(key=lambda s: s.lower())
            llist = []
            for n in synlist:
                namefile = name_to_filename(n)
                llist.append("<a href=\"names/" + namefile + ".html\">" + format_name_string(n) + "</a>")
            outfile.write("       <dt>Synonyms, Alternate Spellings, &amp; Name Forms</dt>\n")
            outfile.write("         <dd><em class=\"species\">" + ", ".join(llist) + "</em></dd>\n")

        # Geographic Range
        outfile.write("       <dt>Geographic Range</dt>\n")
        outfile.write("         <dd>" + species.region + ": " + species.range + "</dd>\n")
        if not is_fossil:
            outfile.write("         <dd>\n")
            outfile.write("           <div id=\"map_canvas_sp\"></div>\n")
            outfile.write("         </dd>\n")
            outfile.write("         <dd class=\"map_data\">\n")
            maprefkeylist = species.range_references.split(";")
            maprefkeylist.sort(key=lambda s: s.lower())
            mapcitelist = []
            for m in maprefkeylist:
                if m in refdict:
                    mref = refdict[m]
                    mapcitelist.append("<a href=\"references/" + mref.cite_key + ".html\">" + mref.citation+"</a>")
                else:
                    mapcitelist.append(m)
            outfile.write("           Map data derived from: " + "; ".join(mapcitelist) + "\n")
            outfile.write("         </dd>\n")

        # External links
        outfile.write("       <dt>External Links</dt>\n")
        if species.eolid != ".":
            outfile.write("         <dd><a href=\"http://eol.org/pages/" + species.eolid +
                          "/overview\">Encyclopedia of Life</a></dd>\n")
        outfile.write("         <dd><a href=\"http://en.wikipedia.org/wiki/Uca_" + species.species +
                      "\">Wikipedia</a></dd>\n")
        if species.inatid != ".":
            outfile.write("         <dd><a href=\"http://www.inaturalist.org/taxa/" + species.inatid +
                          "\">iNaturalist</a></dd>\n")
        if species.taxonid != ".":
            outfile.write("         <dd><a href=\"http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=" +
                          species.taxonid + "\">NCBI Taxonomy Browser/Genbank</a></dd>\n")
        if species.gbifid != ".":
            outfile.write("         <dd><a href=\"http://www.gbif.org/species/" + species.gbifid +
                          "\">GBIF</a></dd>\n")

        outfile.write("      </dl>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"pics\"><span class=\"fa fa-camera\"></span> Photos</a></h2>\n")
        photo_n = 0
        for photo in photos:
            slist = photo.species.split(";")
            if species.species in slist:
                pn = int(photo.n)
                if ";" in photo.species:
                    nl = photo.species.replace(";", "_")
                    pfname = "photos/u_" + nl + format(pn, "0>2") + ".html"
                    tname = nl
                else:
                    pfname = "photos/u_" + species.species + format(pn, "0>2") + ".html"
                    tname = species.species
                outfile.write("      <figure class=\"sppic\">\n")
                outfile.write("        <a href=\"" + pfname + "\"><picture><img src=\"photos/U_" + tname +
                              format(pn, "0>2") + "tn.jpg\" alt=\"Uca " + species.species + "\" title=\"Uca " +
                              species.species + "\" /></picture></a>\n")
                outfile.write("      </figure>\n")
                write_species_photo_page(pfname, species.species, species.common, photo.caption, pn,
                                         photo.species)
                photo_n += 1
        if photo_n == 0:
            outfile.write("      <p>\n")
            outfile.write("        <em>No pictures available at this time.</em>\n")
            outfile.write("      </p>\n")

        outfile.write("\n")
        if not is_fossil:
            outfile.write("    <section class=\"spsection\">\n")
            outfile.write("      <h2><a name=\"video\"><span class=\"fa fa-video-camera\"></span> Video</a></h2>\n")
            videon = 0
            for video in videos:
                slist = video.species.split(";")
                if species.species in slist:
                    vn = int(video.n)
                    if ";" in video.species:
                        nl = video.species.replace(";", "_")
                        vfname = "video/u_" + nl + format(vn, "0>2") + ".html"
                    else:
                        vfname = "video/u_" + species.species + format(vn, "0>2") + ".html"
                    videon += 1
                    if videon == 1:
                        outfile.write("      <dl class=\"vidlist\">\n")
                    outfile.write("            <dt><a class=\"vidlink\" href=\"" + vfname + "\">" +
                                  video.caption + "</a></dt>\n")
                    outfile.write("              <dd>" + video.length + ", " + video.size + ", " +
                                  video.format + "</dd>\n")
                    write_species_video_page(vfname, species.species, species.common, video, vn)
            if videon == 0:
                outfile.write("      <p>\n")
                outfile.write("        <em>No videos available at this time.</em>\n")
                outfile.write("      </p>\n")
            else:
                outfile.write("      </dl>\n")
            outfile.write("    </section>\n")
            outfile.write("\n")

            outfile.write("    <section class=\"spsection\">\n")
            outfile.write("      <h2><a name=\"art\"><span class=\"fa fa-paint-brush\"></span> Art</a></h2>\n")
            artn = 0
            for art in artlist:
                slist = art.species.split(";")
                if species.species in slist:
                    pfname = "art/" + art.image + ".html"
                    outfile.write("      <figure class=\"sppic\">\n")
                    outfile.write("        <a href=\"" + pfname + "\"><picture><img src=\"art/" + art.image +
                                  "_tn." + art.ext + "\" alt=\"" + art.title + "\" title=\"" +
                                  art.title + "\" /></picture></a>\n")
                    outfile.write("      </figure>\n")
                    artn += 1
            if artn == 0:
                outfile.write("      <p>\n")
                outfile.write("        <em>No art available at this time.</em>\n")
                outfile.write("      </p>\n")
            else:
                outfile.write("      </dl>\n")
            outfile.write("    </section>\n")
            outfile.write("\n")

        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"refs\"><span class=\"fa fa-book\"></span> References</a></h2>\n")
        outfile.write("      <div id=\"citation\">\n")
        outfile.write("        <ul>\n")
        # for i, ref in enumerate(references):
        for ref in references:
            if ref.cite_key in sprefs:
                outfile.write(format_reference(ref, logfile))
        outfile.write("        </ul>\n")
        outfile.write("      </div>\n")
        outfile.write("    </section>\n")
        common_html_footer(outfile, "")


def create_photos_html(specieslist, photos):
    create_blank_index("photos/index.html")
    """ create the photos index page """
    with codecs.open(photoURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Photos", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Photos</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      Note: many photos of supposed fiddler crabs on the web are actually from other genera "
                      "(ghost crabs are a common error). Lay-people often assume any crab with asymmetric claws is a "
                      "fiddler crab.\n")
        outfile.write("    </p>\n")
        outfile.write("    <p>\n")
        outfile.write("      Total photo count is " + str(len(photos)) + ".\n")
        outfile.write("    </p>\n")
        for sp in specieslist:
            species = sp.species
            status = sp.status
            outfile.write("    <section class=\"photosection\">\n")
            outfile.write("      <h2>" + create_species_link(species, status, "") + "</h2>\n")
            photo_n = 0
            for photo in photos:
                splist = photo.species.split(";")
                if species in splist:
                    pn = int(photo.n)
                    if ";" in photo.species:
                        spname = photo.species.replace(";", "_")
                    else:
                        spname = photo.species
                    pfname = "photos/u_" + spname + format(pn, "0>2") + ".html"
                    outfile.write("      <figure class=\"sppic\">\n")
                    outfile.write("        <a href=\"" + pfname + "\"><picture><img src=\"photos/U_" +
                                  spname + format(pn, "0>2") + "tn.jpg\" alt=\"Uca " + spname + "\" title=\"Uca " +
                                  spname + "\" /></picture></a>\n")
                    outfile.write("      </figure>\n")
                    photo_n += 1
            if photo_n == 0:
                outfile.write("      <p>\n")
                outfile.write("        <em>No pictures available at this time.</em>\n")
                outfile.write("      </p>\n")
            outfile.write("    </section>\n")
        common_html_footer(outfile, "")


def create_videos_html(videos):
    create_blank_index("video/index.html")
    """ create the videos page """
    sectitle = ("Feeding", "Male Waving and Other Displays", "Female Display", "Fighting", "Mating", "Miscellaneous")
    secshort = ("Feeding", "Male Display", "Female Display", "Fighting", "Mating", "Miscellaneous")
    secanchor = ("feeding", "display", "female", "fighting", "mating", "misc")

    with codecs.open(videoURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Videos", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Videos</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        for i, x in enumerate(secshort):
            outfile.write("          <li><a href=\"#" + secanchor[i] + "\">" + x + "</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      Most of these videos predate digital video (let alone HD) and were recorded on Hi8 tape. "
                      "Hopefully they will eventually be replaced by higher quality video. These are grouped by "
                      "activity. Videos for specific species can be found on the "
                      "<a href=\"" + speciesURL + "\">individual species' page</a>.\n")
        outfile.write("    </p>\n")
        outfile.write("    <p>\n")
        outfile.write("      Total video count is " + str(len(videos)) + "\n")
        outfile.write("    </p>\n")
        for i, x in enumerate(sectitle):
            outfile.write("\n")
            outfile.write("    <section class=\"spsection\">\n")
            outfile.write("      <h2><a name=\"" + secanchor[i] + "\">" + x + "</a></h2>\n")
            outfile.write("      <dl class=\"vidlist\">\n")
            for video in videos:
                if video.activity == secanchor[i]:
                    vn = int(video.n)
                    if ";" in video.species:
                        spname = video.species.replace(";", "_")
                    else:
                        spname = video.species
                    vfname = "video/u_" + spname + format(vn, "0>2") + ".html"
                    outfile.write("            <dt><a class=\"vidlink\" href=\"" + vfname + "\">" + video.caption +
                                  "</a></dt>\n")
                    outfile.write("              <dd>" + video.length + ", " + video.size + ", " + video.format +
                                  "</dd>\n")
            outfile.write("      </dl>\n")
            outfile.write("    </section>\n")
        common_html_footer(outfile, "")


def write_science_art_page(fname, art, backurl, backtext):
    """ create the individual page for each piece of art """
    with codecs.open(fname, "w", "utf-8") as outfile:
        ptitle = art.title + " (" + art.author + " " + art.year + ")"
        common_html_header(outfile, ptitle, "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1><em class=\"species\">" + art.title + "</em></h1>\n")
        outfile.write("      <h2>" + art.author + " (" + art.year + ")</h2>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        if art.species != "n/a":
            outfile.write("          <li><a href=\"../u_" + art.species + ".html\">Species page</a></li>\n")
        if art.cite_key != "n/a":
            outfile.write("          <li><a href=\"../references/" + art.cite_key + ".html\">Reference</a></li>\n")
        outfile.write("          <li><a href=\"../" + backurl + "\">" + backtext + "</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <figure class=\"fullpic\">\n")
        outfile.write("      <picture><img src=\"" + art.image + "." + art.ext + "\" alt=\"" + ptitle +
                      "\" title=\"" + ptitle + "\" /></picture>\n")
        outfile.write("      <figcaption>" + art.notes + "</figcaption>\n")
        outfile.write("    </figure>\n")
        common_html_footer(outfile, "../")


def create_art_science_html(artlist):
    """ create the art science index """
    with codecs.open(artSciURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Art - Scientific", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Scientific Drawings</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        artsource = []
        cnt = 0
        for art in artlist:
            if art.art_type == "science":
                cnt += 1
                artist = art.author + " (" + art.year + ")"
                try:
                    artsource.index(artist)
                except ValueError:
                    artsource.append(artist)
        outfile.write("      <p>\n")
        outfile.write("        Formal scientific drawings are often works of art as well as scientific illustration. "
                      "These are ordered chronologically.\n")
        outfile.write("      </p>\n")
        outfile.write("      <p>\n")
        outfile.write("        Total scientific drawing count is " + str(cnt) + ".\n")
        outfile.write("      </p>\n")
        create_blank_index("art/index.html")
        for a in artsource:
            outfile.write("      <h3>"+a+"</h3>\n")
            for art in artlist:
                if art.art_type == "science":
                    artist = art.author + " (" + art.year + ")"
                    if artist == a:
                        pfname = "art/" + art.image + ".html"
                        outfile.write("      <figure class=\"sppic\">\n")
                        outfile.write("        <a href=\"" + pfname + "\"><picture><img src=\"art/" + art.image +
                                      "_tn." + art.ext + "\" alt=\"" + art.title + "\" title=\"" + art.title +
                                      "\" /></picture></a>\n")
                        outfile.write("      </figure>\n")
                        write_science_art_page(pfname, art, artSciURL, "All Scientific Drawings")
        common_html_footer(outfile, "")


def create_art_stamps_html(artlist):
    """ create the art stamps index """
    with codecs.open(artStampURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Stamps", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Postage Stamps</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        artsource = []
        cnt = 0
        for art in artlist:
            if art.art_type == "stamp":
                cnt += 1
                try:
                    artsource.index(art.author)
                except ValueError:
                    artsource.append(art.author)
        outfile.write("      <p>\n")
        outfile.write("        Fiddler crabs have been featured on postage stamps surprisingly often. Quality "
                      "control leaves something to be desired, however, as misidentifications are common "
                      "(<em>e.g.</em>, see The Gambia and the Solomon Islands). Omori &amp; Holthuis (2000, 2005) "
                      "have actually written papers about crustacea on postage stamps.\n")
        outfile.write("      </p>\n")
        outfile.write("      <p>\n")
        outfile.write("        Total fiddler crab stamps is " + str(cnt) + ".\n")
        outfile.write("      </p>\n")
        for a in artsource:
            outfile.write("      <h3>"+a+"</h3>\n")
            for art in artlist:
                if art.art_type == "stamp":
                    if art.author == a:
                        pfname = "art/" + art.image + ".html"
                        outfile.write("      <figure class=\"sppic\">\n")
                        outfile.write("        <a href=\"" + pfname+"\"><picture><img src=\"art/" + art.image +
                                      "_tn." + art.ext + "\" alt=\"" + art.title + "\" title=\"" + art.title +
                                      "\" /></picture></a>\n")
                        outfile.write("      </figure>\n")
                        write_science_art_page(pfname, art, artStampURL, "All Stamps")
        common_html_footer(outfile, "")

    
def create_art_crafts_html(artlist):
    """ create the art craft index """
    with codecs.open(artCraftURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Crafts", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Art</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"#origami\">Origami</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("      <h2><a name=\"origami\">Origami</a></h2>\n")
        artsource = []
        cnt = 0
        for art in artlist:
            if art.art_type == "origami":
                cnt += 1
                try:
                    artsource.index(art.author)
                except ValueError:
                    artsource.append(art.author)
        outfile.write("      <p>\n")
        outfile.write("        Male fiddler crabs are a particular challenge for origami because of the asymmetry, "
                      "but a number of origami experts have developed fiddler crab models.\n")
        outfile.write("      </p>\n")
        outfile.write("      <p>\n")
        outfile.write("        Total fiddler crab origami models is "+str(cnt)+".\n")
        outfile.write("      </p>\n")
        for a in artsource:
            outfile.write("      <h3>"+a+"</h3>\n")
            for art in artlist:
                if art.art_type == "origami":
                    if art.author == a:
                        pfname = "art/" + art.image + ".html"
                        outfile.write("      <figure class=\"sppic\">\n")
                        outfile.write("        <a href=\"" + pfname + "\"><picture><img src=\"art/" + art.image +
                                      "_tn." + art.ext + "\" alt=\"" + art.title + "\" title=\"" +
                                      art.title + "\" /></picture></a>\n")
                        outfile.write("      </figure>\n")
                        write_science_art_page(pfname, art, artCraftURL, "All Crafts")
        common_html_footer(outfile, "")


def create_art_html(artlist):
    """ create the art pages """
    create_art_science_html(artlist)
    create_art_stamps_html(artlist)
    create_art_crafts_html(artlist)


def species_to_html(specieslist, references, specific_names, all_names, photos, videos, art, species_refs, refdict,
                    logfile):
    """ output species list and individual species pages """
    write_species_list(specieslist)
    for species in specieslist:
        """
        species = specData[0]
        specInfo = specData[1:]
        spRefs = speciesRefs[species]
        writeSpeciesPage(species,specInfo,references,specificNames,allNames,photos,videos,art,spRefs)
        """
        sprefs = species_refs[species.species]
        write_species_page(species, references, specific_names, all_names, photos, videos, art, sprefs, refdict,
                           logfile)


def create_systematics_html(subgenlist, specieslist):
    """ create the systematics page """
    with codecs.open(systURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Systematics", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Systematics</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"#genus\">Genus</a></li>\n")
        outfile.write("          <li><a href=\"#subgenera\">Subgenera</a></li>\n")
        outfile.write("          <li><a href=\"#species\">Species</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <div class=\"topsection\">\n")
        outfile.write("    <p>The following information is an expansion and update of that found in:</p>\n")
        outfile.write("    <blockquote>\n")
        outfile.write("      Rosenberg, M.S. 2001. The systematics and taxonomy of fiddler crabs: A phylogeny of the "
                      "genus <em class=\"species\">Uca.</em> <em>Journal of Crustacean Biology</em> 21(3):839-869.\n")
        outfile.write("    </blockquote>\n")
        outfile.write("    <p>Additional references for updated information will be detailed below.</p>")
        outfile.write("    </div>\n")
        outfile.write("\n")

        # genus section
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"genus\">Genus <em class=\"species\">Uca</em> Leach, 1814</a></h2>\n")
        outfile.write("      <h3>Type species: <em class=\"species\">Cancer vocans major</em> Herbst, 1782</h3>\n")
        outfile.write("      <p>\n")
        outfile.write("         The earliest description of the type species of <em class=\"species\">Uca</em> is from "
                      "a drawing in <a href=\"references/Seba1758.html\">Seba (1758)</a>, which he called "
                      "<em class=\"species\">Cancer uka una, Brasiliensibus</em> (shown below).\n")
        outfile.write("      </p>\n")
        outfile.write("      <figure>\n")
        outfile.write("        <picture><img src=\"art/Seba_Uca_una.jpg\" style=\"padding-left: 0; padding-right: 0; "
                      "margin-left: 0; margin-right: 0; text-align: center\" alt=\"Seba's fiddler crab\" "
                      "title=\"Seba's fiddler crab\" /></picture>\n")
        outfile.write("      </figure>\n")
        outfile.write("      <p>\n")
        outfile.write("        A number of authors subsequently used this same picture as a basis for naming the "
                      "species (<a href=\"references/Manning1981.html\">Manning and Holthuis 1981</a>).  "
                      "<em class=\"species\">Cancer vocans major</em> Herbst, 1782; "
                      "<em class=\"species\">Ocypode heterochelos</em> Lamarck, 1801; "
                      "<em class=\"species\">Cancer uka</em> Shaw and Nodder, 1802; and "
                      "<em class=\"species\">Uca una</em> Leach, 1814, are  all objective synonyms, because they are "
                      "all based on the picture and  description from Seba. Because of this, the official type "
                      "specimen of the  genus <em class=\"species\">Uca</em> is <em class=\"species\">Cancer vocans "
                      "major.</em>  The earliest description of  this species based on actual specimens and not on "
                      "Seba's drawing was <em class=\"species\"> Gelasimus platydactylus</em> Milne-Edwards, 1837.\n")
        outfile.write("      </p>\n")
        outfile.write("      <blockquote>\n")
        outfile.write("        As an aside, Seba's name, <em class=\"species\">Cancer uka una</em> comes from the "
                      "nomenclature of <a href=\"references/Marcgrave1648.html\">Marcgrave (1648)</a>, who mispelled "
                      "&ldquo;u&ccedil;a una&rdquo; as &ldquo;uca una&rdquo;. Not only did Seba copy the mispelling, "
                      "but he applied it to the fiddler crab instead of the mangrove crab (which is today called "
                      "<em class=\"species\">Ucides</em>) to which Marcgrave applied the name (see below). "
                      "<a href=\"references/Latreille1817.2.html\">Latreille's (1817)</a> proposal of the generic "
                      "name <em class=\"species\">Gelasimus</em> for fiddler crabs was so that "
                      "<em class=\"species\">Uca</em> could be applied to mangrove crabs; as this was an invalid "
                      "proposal, <em class=\"species\">Uca</em> is retained for fiddlers, despite being due to a "
                      "pair of errors (<a href=\"references/Tavares1993.html\">Tavares 1993</a>).\n")
        outfile.write("        <figure class=\"syspic\">\n")
        outfile.write("          <picture><img src=\"art/Marcgrave_Maracoani.png\" alt=\"Marcgrave's Maracoani\" "
                      "title=\"Marcgrave's Maracoani\"></picture>\n")
        outfile.write("          <figcaption>Oldest known drawing of a fiddler crab "
                      "(<a href=\"references/Marcgrave1648.html\">Marcgrave, 1648</a>). He labeled it "
                      "&ldquo;Maracoani&rdquo;, and it represents the namesake of the species "
                      "<em class=\"species\">Uca maracoani.</em></figcaption>\n")
        outfile.write("        </figure>\n")
        outfile.write("        <figure class=\"syspic\">\n")
        outfile.write("          <picture><img src=\"art/Marcgrave_Uca_una.png\" alt=\"Marcgrave's Uca una\" "
                      "title=\"Marcgrave's Uca una\"></picture>\n")
        outfile.write("          <figcaption>The drawing actually labeled &ldquo;Uca Una&rdquo; by "
                      "<a href=\"references/Marcgrave1648.html\">Marcgrave (1648)</a> is not a fiddler crab. "
                      "Today this species is known as the mangrove crab <em class=\"species\">Ucides "
                      "cordatus.</em></figcaption>\n")
        outfile.write("        </figure>\n")
        outfile.write("        <figure class=\"syspic\">\n")
        outfile.write("          <picture><img src=\"art/Marcgrave_Ciecie_Ete.png\" alt=\"Marcgrave's Ciecie Ete\" "
                      "title=\"Marcgrave's Ciecie Ete\"></picture>\n")
        outfile.write("          <figcaption>The other fiddler crab drawing found in "
                      "<a href=\"references/Marcgrave1648.html\">Marcrgrave (1648)</a>, labeled "
                      "&ldquo;Ciecie Ete&rdquo; (he also refers to a very similar species called "
                      "&ldquo;Ciecie Panema&rdquo;). This figure is believed to most likely represent "
                      "<em class=\"species\">Uca thayeri.</em></figcaption>\n")
        outfile.write("        </figure>\n")
        outfile.write("      </blockquote>\n")
        outfile.write("      <p>\n")
        outfile.write("        For about 60 years, the genus was known as <em class=\"species\">Gelasimus,</em> "
                      "until <a href=\"references/Rathbun1897.1.html\">Rathbun (1897)</a> showed that the abandonment "
                      "of the older name <em class=\"species\">Uca</em> did not conform to zoological naming "
                      "conventions. The type species of <em class=\"species\">Uca</em> was known as both "
                      "<em class=\"species\">Uca heterochelos</em> and <em class=\"species\">U. platydactylus,</em> "
                      "until <a href=\"references/Rathbun1918.2.html\">Rathbun (1918)</a> suggested the adoption of "
                      "<em class=\"species\">U. heterochelos</em> as the valid name. Almost 50 years later, "
                      "<a href=\"references/Holthuis1962.html\">Holthuis (1962)</a> pointed out that "
                      "<em class=\"species\">U. heterochelos</em> was an objective junior synonym of "
                      "<em class=\"species\">U. major,</em> thus the type species has been referred to as "
                      "<em class=\"species\">U. major</em> ever since.\n")
        outfile.write("      <p>\n")
        outfile.write("      <p>\n")
        outfile.write("        However, <a href=\"references/Bott1973.1.html\">Bott (1973)</a> discovered that there "
                      "has been a universal  misinterpretation of the type species; the species pictured by Seba is "
                      "not the American species commonly referred to as "
                      "<em class=\"species\">U. major,</em> but rather the West African/Portuguese species called "
                      "<em class=\"species\">U. tangeri</em> (Eydoux, 1835). Correcting this error would have caused "
                      "a somewhat painful change of names (<a href=\"references/Holthuis1979.html\">Holthuis 1979</a>; "
                      "<a href=\"references/Manning1981.html\">Manning and Holthuis 1981</a>). The type species "
                      "would still be called <em class=\"species\">U. major</em>, but would refer to the West "
                      "African/European species rather than the American one; the American species, "
                      "which has been called <em class=\"species\">U. major</em> since 1962, would be called "
                      "<em class=\"species\">U. platydactylus,</em> a name not used since 1918.\n")
        outfile.write("      <p>\n")
        outfile.write("      <p>\n")
        outfile.write("         To deal with this dilemma, the Society of Zoological Nomenclature officially "
                      "designated the holotype of <em class=\"species\">Gelasimus platydactylus</em> as a neotype "
                      "of <em class=\"species\">Cancer vocans major</em> "
                      "(<a href=\"references/Holthuis1979.html\">Holthuis 1979</a>; "
                      "<a href=\"references/ICZN1983.html\">ICZN Opinion 1262</a>). The result of this decision is "
                      "that we retain the names <em class=\"species\">U. major</em> for the American species and "
                      "<em class=\"species\">U. tangeri</em> for the West African/European species. It also means "
                      "that although <em class=\"species\">U. tangeri</em> is technically the species upon which "
                      "the genus is named, <em class=\"species\">U. major</em> "
                      "(<em class=\"species\">Cancer vocans major</em>) is still the official type species of the "
                      "genus <em class=\"species\">Uca.</em>\n")
        outfile.write("      <p>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")

        # subgenera section
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"subgenera\">Subgenera</a></h2>\n")
        outfile.write("      <p>")
        outfile.write("       There have been two major proposals for splitting up the genus, one by "
                      "<a href=\"references/Bott1973.2.html\">Bott (1973)</a> and the other by "
                      "<a href=\"references/Crane1975.html\">Crane (1975)</a>. Neither is based on a numerical "
                      "phylogeny. Crane's descriptions are very complete. Bott's descriptions are poor, but have "
                      "priority. For a long time, scientists actively ignored both subdivisions and when there "
                      "was a reference in the literature, it almost always used Crane's names and not Bott's. "
                      "Bott also split the genus into multiple genera rather than subgenera, an unnecessary "
                      "complication in most researcher's minds.\n")
        outfile.write("      </p>")
        outfile.write("      <p>")
        outfile.write("       <a href=\"references/Rosenberg2001.html\">Rosenberg (2001)</a> partly cleared up the "
                      "confusion between the two systems. More recent work by "
                      "<a href=\"references/Beinlich2006.html\">Beinlich &amp; von Hagen (2006)</a>, "
                      "<a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009), "
                      "<a href=\"references/Spivak2009.html\">Spivak &amp; Cuesta (2009)</a>, "
                      "<a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> (2010)</a>, "
                      "<a href=\"references/Landstorfer2010.html\">Landstorfer &amp; Schbart (2010)</a>, and "
                      "<a href=\"references/Shih2015.2.html\">Shih (2015)</a> have continued to refine the subgenera "
                      "as detailed below.\n")
        outfile.write("      </p>")
        outfile.write("      <ul>\n")
        for subgen in subgenlist:
            outfile.write("        <li><a href=\"#"+subgen.subgenus + "\">Subgenus <em class=\"species\">" +
                          subgen.subgenus + "</em></a></li>\n")
        outfile.write("      </ul>\n")

        for subgen in subgenlist:
            outfile.write("      <hr />")
            outfile.write("      <h3>Subgenus <a name=\"" + subgen.subgenus + "\"><em class=\"species\">" +
                          subgen.subgenus + "</em> " + subgen.author + "</a></h3>\n")
            outfile.write("      <dl>\n")
            outfile.write("        <dt>Type</dt>\n")
            outfile.write("        <dd>" + create_species_link(subgen.type_species, "", "") + "</dd>\n")
            outfile.write("        <dt>All Species</dt>\n")
            splist = []
            for s in specieslist:
                if s.subgenus == subgen.subgenus:
                    splist.append(create_species_link(s.species, s.status, ""))
            outfile.write("        <dd>" + ", ".join(splist) + "</dd>\n")
            outfile.write("      </dl>\n")
            outfile.write("      <p>\n")
            outfile.write("      " + subgen.notes + "\n")
            outfile.write("      </p>\n")
            outfile.write("\n")

        outfile.write("    </section>\n")
        outfile.write("\n")

        # species section
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"species\">Species Level Systematics</a></h2>\n")
        outfile.write("      <ul>\n")
        outfile.write("        <li><a href=\"" + speciesURL + "\">Currently recognized species</a></li>\n")
        outfile.write("      </ul>\n")
        outfile.write("      <p>\n")
        outfile.write("For an overview of all <em class=\"species\">Uca</em> species, the best reference is "
                      "<a href=\"references/Crane1975.html\">Crane (1975)</a>; any earlier major work would be "
                      "overridden by Crane's descriptions. For the most part, the taxa recognized by Crane are still "
                      "accepted today. A number of new species have been described since the publication of her "
                      "monograph, a few species has been discovered to be invalid, and two of her new species were "
                      "previously described by <a href=\"references/Bott1973.2.html\">Bott (1973)</a>; as with the "
                      "subgenera, his names have priority and take precedence. These changes are summarized below.\n")
        outfile.write("      </p>\n")
        outfile.write("      <h3>Changes to the species level taxonomy of the genus "
                      "<em class=\"species\">Uca</em> since Crane (1975)</h3>\n")
        outfile.write("      <table>\n")
        outfile.write("        <thead>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <th>New/Validated Extant Species</th><th>Reference(s)</th>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </thead>\n")
        outfile.write("        <tfoot>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td colspan=\"2\"><strong>Note:</strong> The newly described (relative to Crane) "
                      "species <em class=\"species\">Uca pavo</em> George &amp; Jones (1982), is a junior subsynonym "
                      "of <em class=\"species\">Uca capricornis</em> (see "
                      "<a href=\"references/vonHagen1989.html\">von Hagen &amp; Jones 1989</a>)</td>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </tfoot>\n")
        outfile.write("        <tbody>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca panacea</em></td>\n")
        outfile.write("            <td><a href=\"references/Novak1974.html\">Novak &amp; Salmon (1974)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca marguerita</em></td>\n")
        outfile.write("            <td><a href=\"references/Thurman1981.1.html\">Thurman (1981)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca elegans</em></td>\n")
        outfile.write("            <td><a href=\"references/George1982.html\">George &amp; Jones (1982)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca hirsutimanus</em></td>\n")
        outfile.write("            <td><a href=\"references/George1982.html\">George &amp; Jones (1982)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca intermedia</em></td>\n")
        outfile.write("            <td><a href=\"references/vonPrahl1985.html\">von Prahl &amp; Toro (1985)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca victoriana</em></td>\n")
        outfile.write("            <td><a href=\"references/vonHagen1987.1.html\">von Hagen (1987)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca albimana</em></td>\n")
        outfile.write("            <td><a href=\"references/Kossmann1877.html\">Kossmann (1877)</a>, "
                      "<a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009)</a>, "
                      "<a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> (2010)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca iranica</em></td>\n")
        outfile.write("            <td><a href=\"references/Pretzmann1971.html\">Pretzmann (1971)</a>, "
                      "<a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009)</a>, "
                      "<a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> (2010)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca cryptica</em></td>\n")
        outfile.write("            <td><a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> "
                      "(2010)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca osa</em></td>\n")
        outfile.write("            <td><a href=\"references/Landstorfer2010.html\">Landstorfer &amp; Schubart "
                      "(2010)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca jocelynae</em></td>\n")
        outfile.write("            <td><a href=\"references/Shih2010.1.html\">Shih <em>et al.</em> (2010</a>)</td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca splendida</em></td>\n")
        outfile.write("            <td><a href=\"references/Stimpson1858.html\">Stimpson (1858)</a>, "
                      "<a href=\"references/Shih2012.html\">Shih <em>et al.</em> (2012)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca boninensis</em></td>\n")
        outfile.write("            <td><a href=\"references/Shih2013.2.html\">Shih <em>et al.</em> (2013)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </tbody>\n")
        outfile.write("      </table>\n")
        outfile.write("      </p>\n")
        outfile.write("      <table>\n")
        outfile.write("        <thead>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <th>Junior Subsynonym</th><th>Correct Name</th><th>Reference(s)</th>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </thead>\n")
        outfile.write("        <tfoot>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td colspan=\"3\"><strong>Note:</strong> <em class=\"species\">Uca australiae</em> "
                      "is probably not a valid species; it is based on a single specimen found washed up on the "
                      "Australian shore (<a href=\"references/George1982.html\">George &amp; Jones 1982</a>, "
                      "among others)</td>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </tfoot>\n")
        outfile.write("        <tbody>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca minima</em></td>\n")
        outfile.write("            <td><em class=\"species\">Uca signata</em></td>\n")
        outfile.write("            <td><a href=\"references/George1982.html\">George &amp; Jones (1982)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca spinata</em></td>\n")
        outfile.write("            <td><em class=\"species\">Uca paradussumieri</em></td>\n")
        outfile.write("            <td><a href=\"references/Dai1991.html\">Dai &amp; Yang (1991)</a>; "
                      "<a href=\"references/Jones1994.html\">Jones &amp; Morton (1994)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca pacificensis</em></td>\n")
        outfile.write("            <td><em class=\"species\">Uca excisa</em></td>\n")
        outfile.write("            <td>Unpublished\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca leptochela</em></td>\n")
        outfile.write("            <td><em class=\"species\">Uca festae</em></td>\n")
        outfile.write("            <td><a href=\"references/Beinlich2006.html\">Beinlich &amp; von Hagen (2006)</td>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </tbody>\n")
        outfile.write("      </table>\n")
        outfile.write("      </p>\n")
        outfile.write("      <table>\n")
        outfile.write("        <thead>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <th>Incorrect Spelling</th>\n")
        outfile.write("            <th>Correct Spelling</th>\n")
        outfile.write("            <th>Reference(s)</th>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </thead>\n")
        outfile.write("        <tbody>\n")
        outfile.write("          <tr> \n")
        outfile.write("            <td><em class=\"species\">Uca longidigita</em></td>\n")
        outfile.write("            <td><em class=\"species\">Uca longidigitum</em></td>\n")
        outfile.write("            <td><a href=\"references/vonHagen1989.html\">von Hagen and Jones (1989)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("          <tr>\n")
        outfile.write("            <td><em class=\"species\">Uca mjobergi</em></td>\n")
        outfile.write("            <td><em class=\"species\">Uca mjoebergi</em></td>\n")
        outfile.write("            <td><a href=\"references/vonHagen1989.html\">von Hagen and Jones (1989)</a></td>\n")
        outfile.write("          </tr>\n")
        outfile.write("        </tbody>\n")
        outfile.write("      </table>\n")
        outfile.write("      <p>\n")
        outfile.write("<a href=\"references/Crane1975.html\">Crane (1975)</a> tended to lump related taxa into "
                      "subspecies rather than treat them as distinct species. A number of studies since that time "
                      "have raised virtually all of her subspecies to specific status (<em>e.g.,</em> "
                      "<a href=\"references/Barnwell1980.html\">Barnwell 1980</a>; "
                      "<a href=\"references/Barnwell1984.1.html\">Barnwell and Thurman 1984</a>; "
                      "<a href=\"references/Collins1984.html\">Collins <em>et al.</em> 1984</a>; "
                      "<a href=\"references/Green1980.html\">Green 1980</a>; "
                      "<a href=\"references/Salmon1979.2.html\">Salmon <em>et al.</em> 1979</a>; "
                      "<a href=\"references/Salmon1987.2.html\">Salmon and Kettler 1987</a>; "
                      "<a href=\"references/Thurman1979.html\">Thurman 1979</a>, "
                      "<a href=\"references/Thurman1982.html\">Thurman 1982</a>; "
                      "<a href=\"references/vonHagen1989.html\">von Hagen and Jones 1989)</a>. "
                      "It has become common practice with many authors to ignore all of the subspecific designations "
                      "and treat each as a separate species (<em>e.g.,</em> "
                      "<a href=\"references/George1982.html\">George and Jones 1982</a>; "
                      "<a href=\"references/Jones1994.html\">Jones and Morton 1994</a>; "
                      "<a href=\"references/vonHagen1989.html\">von Hagen and Jones 1989</a>). "
                      "I follow this practice throughout this website.\n")
        outfile.write("      </p>\n")
        outfile.write("    </section>\n")
        common_html_footer(outfile, "")


def summarize_year(yeardict):
    miny = 2014
    maxy = 0
    for y in yeardict:
        if y < miny:
            miny = y
        elif y > maxy:
            maxy = y
    datalist = []
    c = 0
    # year, total pubs, cumulative pubs, pubs with cite info
    for y in range(miny, maxy+1):
        if y in yeardict:
            c = c + yeardict[y][0]
            datalist.append([y, yeardict[y][0], c, yeardict[y][1]])
        else:
            datalist.append([y, 0, c, 0])

    datalist1900 = []
    for y in range(1900, maxy+1):
        if y in yeardict:
            datalist1900.append([y, yeardict[y][0], yeardict[y][1]])
        else:
            datalist1900.append([y, 0, 0])
    return datalist, datalist1900


def summarize_languages(refs):
    languages = {}
    for ref in refs:
        l = ref.language
        if l != "":
            s = l.find(" ")
            if s > -1:
                l = l[:s]
            if l in languages:
                languages[l] += 1
            else:
                languages[l] = 1
    return languages


def create_life_cycle():
    """ create the life cycle page """
    with codecs.open(lifeCycleURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Life Cycle", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Life Cycle</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      Following is a rough outline of the stages of the life of a fiddler crab. "
                      "The photographs are from a mix of species.\n")
        outfile.write("    </p>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2>Egg</h2>\n")
        outfile.write("      <p>\n")
        outfile.write("      Fertilized female fiddler crabs carry hundreds to thousands of eggs under their abdomen. "
                      "These are sometimes known as &ldquo;sponge&rdquo; crabs.\n")
        outfile.write("      </p>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_rapax10.html\"><picture><img src=\"photos/U_rapax10tn.jpg\" "
                      "alt=\"Gravid female\" title=\"Gravid female\" /></picture></a>\n")
        outfile.write("        <figcaption>Gravid female</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_rapax11.html\"><picture><img src=\"photos/U_rapax11tn.jpg\" "
                      "alt=\"Gravid female\" title=\"Gravid female\" /></picture></a>\n")
        outfile.write("        <figcaption>Close up of eggs</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2>Zoea</h2>\n")
        outfile.write("      <p>\n")
        outfile.write("        When the eggs are ready, the mother goes into the water and allows the eggs to hatch "
                      "into microscopic free-swimming larvae. The early stage larvae are known as zoea.\n")
        outfile.write("      </p>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_ecuadoriensis07.html\"><picture>"
                      "<img src=\"photos/U_ecuadoriensis07tn.jpg\" alt=\"zoea\" title=\"zoea\" /></picture></a>\n")
        outfile.write("        <figcaption>Zoea</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_ecuadoriensis08.html\">"
                      "<picture><img src=\"photos/U_ecuadoriensis08tn.jpg\" alt=\"zoea\" "
                      "title=\"zoea\" /></picture></a>\n")
        outfile.write("        <figcaption>Zoea</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("    <h2>Megalopa</h2>\n")
        outfile.write("      <p>\n")
        outfile.write("        The larvae live in the open water as part of the plankton. "
                      "As they grow and go through a number of molt stages. Older larvae are known as megalopa.\n")
        outfile.write("      </p>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_ecuadoriensis09.html\"><picture>"
                      "<img src=\"photos/U_ecuadoriensis09tn.jpg\" alt=\"megalopa\" "
                      "title=\"megalopa\" /></picture></a>\n")
        outfile.write("        <figcaption>Megalopa</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("    <h2>Crab</h2>\n")
        outfile.write("      <p>\n")
        outfile.write("        At the end of the final larval stage, the larvae molt into immature crabs. "
                      "The amount of time spent as a swimming larvae (hatching to true crab stage) varies among "
                      "species, but ranges from a few weeks to a few months.\n")
        outfile.write("      </p>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_ecuadoriensis10.html\"><picture>"
                      "<img src=\"photos/U_ecuadoriensis10tn.jpg\" alt=\"early stage crab\" title=\"early stage "
                      "crab\" /></picture></a>\n")
        outfile.write("        <figcaption>Early Stage Full Crab</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("      <p style=\"clear: both\">\n")
        outfile.write("        The crabs return to land and begin to grow; juvenile male and female crabs look "
                      "alike.\n")
        outfile.write("      </p>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_pugilator21.html\"><picture>"
                      "<img src=\"photos/U_pugilator21tn.jpg\" alt=\"juveniles\" "
                      "title=\"juveniles\" /></picture></a>\n")
        outfile.write("        <figcaption>Juvenile Crabs</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("      <p style=\"clear: both\">\n")
        outfile.write("        As they grown larger and turn into adults, the secondary-sexual characteristics "
                      "(<em>e.g.</em>, the asymmetric claws) begin to develop. "
                      "Adult crabs mate and the cycle starts over.\n")
        outfile.write("      </p>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_tangeri10.html\"><picture>"
                      "<img src=\"photos/U_tangeri10tn.jpg\" alt=\"adult female\" "
                      "title=\"adult female\" /></picture></a>\n")
        outfile.write("        <figcaption>Adult Female</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("      <figure class=\"sppic\">\n")
        outfile.write("        <a href=\"photos\\u_tangeri12.html\"><picture>"
                      "<img src=\"photos/U_tangeri12tn.jpg\" alt=\"adult male\" "
                      "title=\"adult male\" /></picture></a>\n")
        outfile.write("        <figcaption>Adult Male</figcaption>")
        outfile.write("      </figure>\n")
        outfile.write("    </section>\n")
        common_html_footer(outfile, "")


def create_phylogeny():
    """ create the phylogeny page """
    with codecs.open(treeURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Phylogeny", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Phylogeny</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("     The phylogeny of fiddler crabs is still largely unresolved. Two trees are shown below: one "
                      "just the subgenera and one including all species. These are both rough, conservative estimates "
                      "based on combining information from <a href=\"references/Levinton1996.html\">Levinton <em>et "
                      "al.</em> (1996)</a>, <a href=\"references/Sturmbauer1996.html\">Sturmbauer <em>et al.</em> "
                      "(1996)</a>, <a href=\"references/Rosenberg2001.html\">Rosenberg (2001)</a>, "
                      "<a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009)</a>, "
                      "<a href=\"references/Shih2010.1.html\">Shih <em>et al.</em> (2010)</a>, "
                      "<a href=\"references/Landstorfer2010.html\">Landstorfer &amp; Schubart (2010)</a>, "
                      "<a href=\"references/Shih2012.html\">Shih <em>et al.</em> (2012)</a>, "
                      "<a href=\"references/Shih2013.html\">Shih <em>et al.</em> (2013a)</a>, "
                      "<a href=\"references/Shih2013.2.html\">Shih <em>et al.</em> (2013b)</a>, "
                      "and <a href=\"references/Shih2015.2.html\">Shih (2015)</a>.\n")
        outfile.write("    </p>\n")
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2>Subgenera Phylogeny</h2>\n")
        outfile.write("      <object id=\"subgenera_phylogeny\" data=\"images/tree_subgenera.svg\" "
                      "type=\"image/svg+xml\"></object>\n")
        outfile.write("    </section>\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2>Species Phylogeny</h2>\n")
        outfile.write("      <object id=\"species_phylogeny\" data=\"images/tree_species.svg\" "
                      "type=\"image/svg+xml\"></object>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")
        common_html_footer(outfile, "")


def morphology_link(parent, character):
    if parent == ".":
        return character.replace(" ", "_")
    else:
        return parent.replace(" ", "_") + "_" + character.replace(" ", "_")


def find_morphology_parent(p, mlist):
    x = ""
    for m in mlist:
        if p == m.character:
            x = morphology_link(m.parent, m.character)
    return x


def create_morphology_page(morph, morphlist):
    """ create individual pages for morphology descriptions """
    with codecs.open("morphology/" + morphology_link(morph.parent, morph.character) + ".html",
                     "w", "utf-8") as outfile:
        if morph.parent == ".":
            p = ""
        else:
            p = " (" + morph.parent + ")"
        common_html_header(outfile, "Fiddler Crab Morphology: " + morph.character + p, "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1>" + morph.character + "</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        if morph.parent != ".":
            outfile.write("          <li><a href=\"" + find_morphology_parent(morph.parent, morphlist) + ".html\">" +
                          morph.parent + "</a></li>\n")
        outfile.write("          <li><a href=\"../" + morphURL + "\">General Morphology</a></li>\n")
        outfile.write("          <li><a href=\".\"><span class=\"fa fa-list\"></span> Morphology Index</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <div class=\"morphdesc\">\n")
        outfile.write("     <p>\n")
        outfile.write("       " + morph.description + "\n")
        outfile.write("     </p>\n")
        c = 0
        for m in morphlist:
            if m.parent == morph.character:
                c += 1
        if c > 0:
            outfile.write("     <h2>More Detail</h2>\n")
            outfile.write("     <ul>\n")
            for m in morphlist:
                if m.parent == morph.character:
                    outfile.write("       <li><a href=\"" + morphology_link(m.parent, m.character) + ".html\">" +
                                  m.character + "</a></li>\n")
            outfile.write("     </ul>\n")
        outfile.write("    </div>\n")
        if "|" in morph.image:
            plist = morph.image.split("|")
            clist = morph.caption.split("|")
        else:
            plist = [morph.image]
            clist = [morph.caption]
        for i in range(len(plist)):
            outfile.write("    <figure class=\"morphimg\">\n")
            outfile.write("      <picture><img src=\"" + plist[i] + "\" alt=\"" + clist[i] + "\" title=\"" + clist[i] +
                          "\" /></picture>\n")
            outfile.write("      <figcaption>" + clist[i] + "</figcaption>\n")
            outfile.write("    </figure>\n")

        common_html_footer(outfile, "../")


def create_morphology_index(morphlist):
    """ create index for morphology pages """
    with codecs.open("morphology/index.html", "w", "utf-8") as outfile:
        common_html_header(outfile, "Morphology Index", "../")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Morphology Index</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"../" + morphURL + "\">General Morphology</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("     <ul>\n")
        uniquelist = {}
        for m in morphlist:
            if m.character in uniquelist:
                uniquelist[m.character] += 1
            else:
                uniquelist[m.character] = 1

        sortlist = []
        for m in morphlist:
            if uniquelist[m.character] > 1:
                sortlist.append([m.character + " (" + m.parent + ")", m])
            else:
                sortlist.append([m.character, m])
        sortlist.sort()
        for s in sortlist:
            m = s[1]
            if uniquelist[m.character] > 1:
                p = " ("+m.parent+")"
            else:
                p = ""
            outfile.write("      <li><a href=\"" + morphology_link(m.parent, m.character) + ".html\">" +
                          m.character + p + "</a></li>\n")
        outfile.write("     </ul>\n")
        common_html_footer(outfile, "../")


def create_morphology_pages(morphology):
    """ create page for general morphology descriptions """
    with codecs.open(morphURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Morphology", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Morphology</h1>\n")
        outfile.write("      <nav>\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"morphology/index.html\"><span class=\"fa fa-list\"></span> "
                      "Index</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </nav>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <div class=\"morphdesc\">\n")
        outfile.write("     <p>\n")
        outfile.write("      Fiddler crabs are decapod &ldquo;true crabs&rdquo; which much of the standard morphology "
                      "found within this group. The following sections briefly describe major morphological features "
                      "as well as characteristics that are often used to distinguish among species.\n")
        outfile.write("     </p>\n")
        outfile.write("      The morphology is organized hierarchically by major body component with further details "
                      "within each section.\n")
        outfile.write("     <p>\n")
        outfile.write("     </p>\n")
        outfile.write("     <h2>More Detail</h2>\n")
        outfile.write("     <ul>\n")
        for m in morphology:
            if m.parent == ".":
                outfile.write("      <li><a href=\"morphology/" + morphology_link(m.parent, m.character) +
                              ".html\">" + m.character + "</a></li>\n")
            create_morphology_page(m, morphology)
        create_morphology_index(morphology)
        outfile.write("     </ul>\n")
        outfile.write("    </div>\n")
        outfile.write("    <figure class=\"morphimg\">\n")
        outfile.write("      <picture><img src=\"morphology/dorsal_view.png\" alt=\"dorsal view of crab\" "
                      "title=\"dorsal view of crab\" /></picture>\n")
        outfile.write("      <figcaption>Figure modified from Crane (1975).</figcaption>\n")
        outfile.write("    </figure>\n")
        outfile.write("    <figure class=\"morphimg\">\n")
        outfile.write("      <picture><img src=\"morphology/ventral_view.png\" alt=\"ventral view of crab\" "
                      "title=\"ventral view of crab\" /></picture>\n")
        outfile.write("      <figcaption>Figure modified from Crane (1975).</figcaption>\n")
        outfile.write("    </figure>\n")
        outfile.write("    <figure class=\"morphimg\">\n")
        outfile.write("      <picture><img src=\"morphology/anterior_view.png\" alt=\"anterior view of crab\" "
                      "title=\"anterior view of crab\" /></picture>\n")
        outfile.write("      <figcaption>Figure modified from Crane (1975).</figcaption>\n")
        outfile.write("    </figure>\n")

        common_html_footer(outfile, "")


def create_citation_page(refdict):
    """ create page with site citation info """
    with codecs.open(citeURL, "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crab Website Citation", "")
        outfile.write("    <header>\n")
        outfile.write("      <h1>Citation Info</h1>\n")
        outfile.write("    </header>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      Generally it is best to cite the primary literature, whenever possible. However, the "
                      "following paper describes much of the data that is unique to this website:\n")
        outfile.write("    </p>\n")
        outfile.write("    <div id=\"citation\">\n")
        outfile.write("      <ul>\n")
        ref = refdict["Rosenberg2014"]  # citation describing the database
        outfile.write("        <li><a href=\"references/Rosenberg2014.html\">" + ref.formatted_html + "</a></li>\n")
        outfile.write("      </ul>\n")
        outfile.write("    </div>\n")
        outfile.write("    <ul class=\"fa-ul\">\n")
        outfile.write("      <li><span class=\"fa-li fa fa-file-pdf-o\"></span>"
                      "<a href=\"http://dx.plos.org/10.1371/journal.pone.0101704\">Read paper online at "
                      "PLoS ONE</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-github\"></span>"
                      "<a href=\"https://github.com/msrosenberg/fiddlercrab.info\">Website data repository on "
                      "Github</a></li>\n")
        outfile.write("    </ul>\n")
        common_html_footer(outfile, "")


def create_index(species):
    """ create the site index """
    with codecs.open("index.html", "w", "utf-8") as outfile:
        common_html_header(outfile, "Fiddler Crabs (Genus Uca)", "")
        outfile.write("    <p>\n")
        scnt = 0
        for s in species:
            if s.status != "fossil":
                scnt += 1
        outfile.write("      Fiddler crabs are small, semi-terrestrial crabs of the genus <em "
                      "class=\"species\">Uca</em> that are characterized by extreme cheliped asymmetry in males.  "
                      "They are most closely related to the <em class=\"species\">Ocypode</em> (ghost crabs). "
                      "<a href=\"" + speciesURL + "\">There are currently {} recognized extant "
                      "species</a>.\n".format(scnt))
        outfile.write("    </p>\n")
        outfile.write("    <div class=\"indeximages\">\n")
        outfile.write("      <picture><img src=\"photos/U_mjoebergi04tn.jpg\" /></picture>\n")
        outfile.write("      <picture><img src=\"photos/U_minax07tn.jpg\" /></picture>\n")
        outfile.write("      <picture><img src=\"photos/U_crassipes19tn.jpg\" /></picture>\n")
        outfile.write("    </div>\n")
        outfile.write("\n")
        outfile.write("    <h2>Classification</h2>\n")
        outfile.write("    <table>\n")
        outfile.write("      <tr><td class=\"classcol1\">Kingdom</td><td>Animalia</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Phylum</td><td>Arthropoda</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Class</td><td>Crustacea</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Sub-class</td><td>Malocostraca</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Order</td><td>Decapoda</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Infraorder</td><td>Brachyura</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Superfamily</td><td>Ocypodoidea</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Family</td><td>Ocypodidae</td></tr>\n")
        outfile.write("      <tr><td class=\"classcol1\">Subfamily</td><td>Ocypodinae</td>\n")
        outfile.write("      <tr><td class=\"classcol1\">Genus</td><td><em class=\"species\">Uca</em></td>\n")
        outfile.write("    </table>\n")
        outfile.write("\n")
        outfile.write("    <p>\n")
        outfile.write("      The common English name &ldquo;Fiddler Crab&rdquo; comes from the feeding of the "
                      "males, where the movement of the small claw from the ground to its mouth "
                      "resembles the motion of a someone moving a bow across a fiddle (the large claw).\n")
        outfile.write("    </p>\n")
        outfile.write("    <h2>Information</h2>\n")
        outfile.write("    <ul class=\"fa-ul\">\n")
        outfile.write("      <li><span class=\"fa-li fa fa-signal fa-rotate-270\"></span><a href=\"" + systURL +
                      "\">Systematics</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-share-alt fa-rotate-270\"></span><a href=\"" + treeURL +
                      "\">Phylogeny</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-list\"></span><a href=\"" + speciesURL + "\">Species</a>\n")
        outfile.write("        <ul>\n")
        outfile.write("           <li><a href=\"names\">Name Index</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-comments-o\"></span><a href=\"" + commonURL +
                      "\">Common Names</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-map-o\"></span><a href=\"" + mapURL +
                      "\">Geographic Ranges</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-refresh\"></span><a href=\"" + lifeCycleURL +
                      "\">Life Cycle</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-heart-o\"></span><a href=\"" + morphURL +
                      "\">Morphology</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-book\"></span><a href=\"" + refURL +
                      "\">Comprehensive Reference List</a></li>\n")
        outfile.write("    </ul>\n")
        outfile.write("    <h2>Multimedia</h2>\n")
        outfile.write("    <ul class=\"fa-ul\">\n")
        outfile.write("      <li><span class=\"fa-li fa fa-camera\"></span><a href=\"" + photoURL +
                      "\">Photos</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-video-camera\"></span><a href=\"" + videoURL +
                      "\">Videos</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-paint-brush\"></span>Art\n")
        outfile.write("        <ul>\n")
        outfile.write("          <li><a href=\"" + artSciURL + "\">Scientific Art</a></li>\n")
        outfile.write("          <li><a href=\"" + artStampURL + "\">Postage Stamps</a></li>\n")
        outfile.write("          <li><a href=\"" + artCraftURL + "\">Crafts</a></li>\n")
        outfile.write("        </ul>\n")
        outfile.write("      </li>\n")
        outfile.write("    </ul>\n")
        outfile.write("    <h2>Miscellania</h2>\n")
        outfile.write("    <ul class=\"fa-ul\">\n")
        outfile.write("      <li><span class=\"fa-li fa fa-pencil\"></span>"
                      "<a href=\"" + citeURL + "\">Citation info for this website</a></li>\n")
        outfile.write("      <li><span class=\"fa-li fa fa-github\"></span>"
                      "<a href=\"https://github.com/msrosenberg/fiddlercrab.info\">Website data on Github</a></li>\n")
        outfile.write("    </ul>\n")
        common_html_footer(outfile, "")


def main():
    with open("errorlog.txt", "w") as logfile:
        print("...Reading References...")
        references, refdict, citelist, yeardict, citecount = get_references(logfile)
        yeardat, yeardat1900 = summarize_year(yeardict)
        languages = summarize_languages(references)
        print("...Reading Species...")
        species = get_species()
        print("...Conneting References...")
        species_refs = connect_refs_to_species(species, citelist)
        print("...Writing References...")
        references_to_html(references, logfile)
        reference_summary(len(references), yeardat, yeardat1900, citecount, languages)
        reference_pages(references, refdict, citelist, logfile)
        print("...Reading Species Names...")
        specific_names = get_specific_names()
        all_names = index_name_pages(refdict, citelist, specific_names, species_refs, logfile)
        specific_name_pages(citelist, specific_names, logfile)
        print("...Reading Photos and Videos...")
        photos = get_photos()
        videos = get_videos()
        art = get_art()
        print("...Writing Species...")
        species_to_html(species, references, specific_names, all_names, photos, videos, art, species_refs, refdict,
                        logfile)
        subgenera = get_subgenera()
        create_systematics_html(subgenera, species)
        create_common_names_html()
        create_photos_html(species, photos)
        create_art_html(art)
        create_videos_html(videos)
        create_map_html(species)
        create_life_cycle()
        create_phylogeny()
        morphology = get_morphology()
        create_morphology_pages(morphology)
        create_index(species)
        create_citation_page(refdict)
    print("done")


if __name__ == "__main__":
    main()
