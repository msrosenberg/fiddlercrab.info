
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
artURL = "uca_art.html"
morphURL = "uca_morphology.html"
citeURL = "citation.html"
fossilImage = "<img class=\"fossilImg\" src=\"images/fossil.png\" alt=\" (fossil)\" />"

randSeed = random.randint(0,10000)

#----classes----

class ReferenceClass():
    """ A class to hold references """
    def __init__(self):
        self.__formattedHTML = ""
        self.__citation = ""
        self.__citeKey = ""
    def citation(self):
        return self.__citation
    def setCitation(self,x):
        self.__citation = x
    def citeKey(self):
        return self.__citeKey
    def setciteKey(self,x):
        self.__citeKey = x
    def formattedHTML(self):
        return self.__formattedHTML
    def setFormattedHTML(self,x):
        self.__formattedHTML = x


class SpecificNameClass():
    """ a class to hold specific names """
    def __init__(self):
        self.__name = ""
        self.__variations = ""
        self.__synonym = ""
        self.__originalBinomial = ""
        self.__prioritySource = ""
        self.__meaning = ""
        self.__notes = ""
    def name(self):
        return self.__name
    def setName(self,x):
        self.__name = x
    def variations(self):
        return self.__variations
    def setVariations(self,x):
        self.__variations = x
    def synonym(self):
        return self.__synonym
    def setSynonym(self,x):
        self.__synonym = x
    def originalBinomial(self):
        return self.__originalBinomial
    def setOriginalBinomial(self,x):
        self.__originalBinomial = x
    def prioritySource(self):
        return self.__prioritySource
    def setPrioritySource(self,x):
        self.__prioritySource = x
    def meaning(self):
        return self.__meaning
    def setMeaning(self,x):
        self.__meaning = x
    def notes(self):
        return self.__notes
    def setNotes(self,x):
        self.__notes = x


class SubgenusClass():
    """ a class to hold subgenera """
    def __init__(self):
        self.__subgenus = ""
        self.__author = ""
        self.__typeSpecies = ""
        self.__notes = ""
        self.__taxonid = ""
        self.__EOLid = ""
    def subgenus(self):
        return self.__subgenus
    def setSubgenus(self,x):
        self.__subgenus = x
    def author(self):
        return self.__author
    def setAuthor(self,x):
        self.__author = x
    def typeSpecies(self):
        return self.__typespecies
    def setTypeSpecies(self,x):
        self.__typespecies = x
    def notes(self):
        return self.__notes
    def setNotes(self,x):
        self.__notes = x
    def taxonid(self):
        return self.__taxonid
    def setTaxonid(self,x):
        self.__taxonid = x
    def EOLid(self):
        return self.__EOLid
    def setEOLid(self,x):
        self.__EOLid = x


class VideoClass():
    """ a class to hold video information """
    def __init__(self):
        self.__species = ""
        self.__n = 0
        self.__activity = ""
        self.__caption = ""
        self.__length = ""
        self.__size = ""
        self.__format = ""
        self.__dateLocation = ""
        self.__author = ""
        self.__notes = ""
    def species(self):
        return self.__species
    def setSpecies(self,x):
        self.__species = x
    def n(self):
        return self.__n
    def setn(self,x):
        self.__n = x
    def activity(self):
        return self.__activity
    def setActivity(self,x):
        self.__activity = x
    def caption(self):
        return self.__caption
    def setCaption(self,x):
        self.__caption = x
    def length(self):
        return self.__length
    def setLength(self,x):
        self.__length = x
    def size(self):
        return self.__size
    def setSize(self,x):
        self.__size = x
    def format(self):
        return self.__format
    def setFormat(self,x):
        self.__format = x
    def dateLocation(self):
        return self.__dateLocation
    def setDateLocation(self,x):
        self.__dateLocation = x
    def author(self):
        return self.__author
    def setAuthor(self,x):
        self.__author = x
    def notes(self):
        return self.__notes
    def setNotes(self,x):
        self.__notes = x


class PhotoClass():
    """ a class to hold photo information """
    def __init__(self):
        self.__species = ""
        self.__n = 0
        self.__caption = ""
    def species(self):
        return self.__species
    def setSpecies(self,x):
        self.__species = x
    def n(self):
        return self.__n
    def setn(self,x):
        self.__n = x
    def caption(self):
        return self.__caption
    def setCaption(self,x):
        self.__caption = x


class ArtClass():
    """ a class to hold art information """
    def __init__(self):
        self.__artType = ""
        self.__author = ""
        self.__year = ""
        self.__title = ""
        self.__image = ""
        self.__ext = ""
        self.__species = ""
        self.__notes = ""
        self.__citeKey = ""
    def artType(self):
        return self.__artType
    def setArtType(self,x):
        self.__artType = x
    def citeKey(self):
        return self.__citeKey
    def setCiteKey(self,x):
        self.__citeKey = x
    def author(self):
        return self.__author
    def setAuthor(self,x):
        self.__author = x
    def year(self):
        return self.__year
    def setYear(self,x):
        self.__year = x
    def title(self):
        return self.__title
    def setTitle(self,x):
        self.__title = x
    def image(self):
        return self.__image
    def setImage(self,x):
        self.__image = x
    def ext(self):
        return self.__ext
    def setExt(self,x):
        self.__ext = x
    def species(self):
        return self.__species
    def setSpecies(self,x):
        self.__species = x
    def notes(self):
        return self.__notes
    def setNotes(self,x):
        self.__notes = x


class MorphologyClass():
    def __init__(self):
        self.__character = ""
        self.__parent = ""
        self.__image = ""
        self.__description = ""
        self.__caption = ""
        #self.__maxHeight = "0"
    def character(self):
        return self.__character
    def setCharacter(self,x):
        self.__character = x
    def parent(self):
        return self.__parent
    def setParent(self,x):
        self.__parent = x
    def image(self):
        return self.__image
    def setImage(self,x):
        self.__image = x
    def description(self):
        return self.__description
    def setDescription(self,x):
        self.__description = x
    def caption(self):
        return self.__caption
    def setCaption(self,x):
        self.__caption = x
    #def maxHeight(self):
    #    return self.__maxHeight
    #def setMaxHeight(self,x):
    #   self.__maxHeight = x


class SpeciesClass():
    def __init__(self):
        self.__species = ""
        self.__subgenus = ""
        self.__typeSpecies = ""
        self.__typeRef = ""
        self.__common = ""
        self.__commonext = ""
        self.__range = ""
        self.__rangeRefs = ""
        self.__region = ""
        self.__status = ""
        self.__taxonid = ""
        self.__EOLid = ""
        self.__iNatid = ""
        self.__gbifid = ""
    def species(self):
        return self.__species
    def setSpecies(self,x):
        self.__species = x
    def subgenus(self):
        return self.__subgenus
    def setSubgenus(self,x):
        self.__subgenus = x
    def typeSpecies(self):
        return self.__typeSpecies
    def setTypeSpecies(self,x):
        self.__typeSpecies = x
    def typeRef(self):
        return self.__typeRef
    def setTypeRef(self,x):
        self.__typeRef = x
    def common(self):
        return self.__common
    def setCommon(self,x):
        self.__common = x
    def commonext(self):
        return self.__commonext
    def setCommonext(self,x):
        self.__commonext = x
    def range(self):
        return self.__range
    def setRange(self,x):
        self.__range = x
    def rangeRefs(self):
        return self.__rangeRefs
    def setRangeRefs(self,x):
        self.__rangeRefs = x
    def region(self):
        return self.__region
    def setRegion(self,x):
        self.__region = x
    def status(self):
        return self.__status
    def setStatus(self,x):
        self.__status = x
    def taxonid(self):
        return self.__taxonid
    def setTaxonid(self,x):
        self.__taxonid = x
    def EOLid(self):
        return self.__EOLid
    def setEOLid(self,x):
        self.__EOLid = x
    def iNatid(self):
        return self.__iNatid
    def setiNatid(self,x):
        self.__iNatid = x
    def gbifid(self):
        return self.__gbifid
    def setgbifid(self,x):
        self.__gbifid = x


class CitationClass():
    def __init__(self):
        self.__citeKey = ""
        self.__nameKey = ""
        self.__name = ""
        self.__common = ""
        self.__where = ""
        self.__context = ""
        self.__application = ""
        self.__citeN = ""
        self.__actual = ""
        self.__source = ""
        self.__nameNote = ""
        self.__generalNote = ""
    def citeKey(self):
        return self.__citeKey
    def setCiteKey(self,x):
        self.__citeKey = x
    def nameKey(self):
        return self.__nameKey
    def setNameKey(self,x):
        self.__nameKey = x
    def name(self):
        return self.__name
    def setName(self,x):
        self.__name = x
    def common(self):
        return self.__common
    def setCommon(self,x):
        self.__common = x
    def where(self):
        return self.__where
    def setWhere(self,x):
        self.__where = x
    def context(self):
        return self.__context
    def setContext(self,x):
        self.__context = x
    def application(self):
        return self.__application
    def setApplication(self,x):
        self.__application = x
    def citeN(self):
        return self.__citeN
    def setCiteN(self,x):
        self.__citeN = x
    def actual(self):
        return self.__actual
    def setActual(self,x):
        self.__actual = x
    def source(self):
        return self.__source
    def setSource(self,x):
        self.__source = x
    def nameNote(self):
        return self.__nameNote
    def setNameNote(self,x):
        self.__nameNote = x
    def generalNote(self):
        return self.__generalNote
    def setGeneralNote(self,x):
        self.__generalNote = x


#----functions----

def getReferences():
    """ read reference data """
    refList = []
    yearDat = {}
    citeDone = {}
    # citation and species data from text
    reffile = codecs.open("references_cites.txt","r","utf-8")
    for line in reffile:
        line = line.replace("et al.","<em>et al.</em>")
        ref = line.strip().split("\t")
        if len(ref) == 1:
            ref.append("")
        newRef = ReferenceClass()
        newRef.setCitation(ref[0])
        newRef.setciteKey(ref[1])
        # calculate publishing trend
        y = ref[0]
        y = y[y.find("(")+1:y.find(")")]
        if (y != "?") and (y.lower() != "in press"):
            if y[0] == "~":
                y = y[1:]
            if len(y) > 4:
                y = y[:4]
            y = int(y)
            if y in yearDat:
                yearDat[y] += 1
            else:
                yearDat[y] = 1
        citeDone[ref[1]] = [False,y]
        refList.append(newRef)
    reffile.close()
    # formatted references from html
    reffile = codecs.open("references.html", "r", "utf-8" )
    c = -1
    for line in reffile:
        line = line.strip()
        if line.endswith("<p>"):
            line = line[:line.find("<p>")]
            line = line.replace("<i>","<em>")
            line = line.replace("</i>","</em>")
            c += 1
            newRef = refList[c]
            newRef.setFormattedHTML(line)
    reffile.close()
    refDict = {}
    for ref in refList:
        refDict[ref.citeKey()] = ref    
    # citation info
    reffile = open("citeinfo.txt","r")
    citeList = []
    gotHeader = False
    for line in reffile:
        if not gotHeader:
            gotHeader = True
        else:
            line = line.replace("\"\"","\"")
            cite = line.strip().split("\t")
            for i,x in enumerate(cite):
                if x.startswith("\"") and x.endswith("\""):
                    cite[i] = x[1:len(x)-1]
            newCite = CitationClass()
            newCite.setCiteKey(cite[0])
            newCite.setNameKey(cite[1])
            newCite.setName(cite[2])
            newCite.setCommon(cite[3])
            newCite.setWhere(cite[4])
            newCite.setContext(cite[5])
            newCite.setApplication(cite[6])
            newCite.setCiteN(cite[7])
            newCite.setActual(cite[8])
            newCite.setSource(cite[9])
            newCite.setNameNote(cite[10])
            newCite.setGeneralNote(cite[11])
            citeList.append(newCite)
            citeDone[cite[0]][0] = True
    reffile.close()

    for y in yearDat:
        yearDat[y] = [yearDat[y],0]
    for x in citeDone:
        c = citeDone[x]
        if c[1] in yearDat and c[0]:
            yearDat[c[1]][1] += 1    
    return refList,refDict,citeList,yearDat


def readSimpleFile(fname):
    """ read data from generic flatfile """
    infile = open(fname,"r")
    #infile = codecs.open(fname,"r")
    spList= []
    gotHeader = False
    for line in infile:
        if gotHeader:
            line = line.strip()
            line = line.replace("\"\"","\"")
            spInfo = line.split("\t")
            for i,x in enumerate(spInfo):
                if x.startswith("\"") and x.endswith("\""):
                    spInfo[i] = x[1:len(x)-1]
            spList.append(spInfo)
        else:
            gotHeader = True
    infile.close()
    return spList


def getSpecies():
    """ read data from species flatfile """
    tmpList = readSimpleFile("species_info.txt")
    sList = []
    for s in tmpList:
        newSpecies = SpeciesClass()
        newSpecies.setSpecies(s[0])
        newSpecies.setSubgenus(s[1])
        newSpecies.setTypeSpecies(s[2])
        newSpecies.setTypeRef(s[3])
        newSpecies.setCommon(s[4])
        newSpecies.setCommonext(s[5])
        newSpecies.setRange(s[6])
        newSpecies.setRangeRefs(s[7])
        newSpecies.setRegion(s[8])
        newSpecies.setStatus(s[9])
        newSpecies.setTaxonid(s[10])
        newSpecies.setEOLid(s[11])
        newSpecies.setiNatid(s[12])
        newSpecies.setgbifid(s[13])
        sList.append(newSpecies)
    return sList


def getPhotos():
    """ read data from photo flatfile """
    tmpList = readSimpleFile("photos.txt")
    pList = []
    for p in tmpList:
        newPhoto = PhotoClass()
        newPhoto.setSpecies(p[0])
        newPhoto.setn(p[1])
        newPhoto.setCaption(p[2])
        pList.append(newPhoto)
    return pList


def getVideos():
    """ read data from video flatfile """
    tmpList = readSimpleFile("videos.txt")
    vList = []
    for v in tmpList:
        newVideo = VideoClass()
        newVideo.setSpecies(v[0])
        newVideo.setn(v[1])
        newVideo.setActivity(v[2])
        newVideo.setCaption(v[3])
        newVideo.setLength(v[4])
        newVideo.setSize(v[5])
        newVideo.setFormat(v[6])
        newVideo.setDateLocation(v[7])
        newVideo.setAuthor(v[8])
        newVideo.setNotes(v[9])
        vList.append(newVideo)
    return vList


def getSubgenera():
    """ read subgenera data """
    tmpList = readSimpleFile("subgenera.txt")
    genList = []
    for g in tmpList:
        newSubgenus = SubgenusClass()
        newSubgenus.setSubgenus(g[0])
        newSubgenus.setAuthor(g[1])
        newSubgenus.setTypeSpecies(g[2])
        newSubgenus.setNotes(g[3])
        newSubgenus.setTaxonid(g[4])
        newSubgenus.setEOLid(g[5])
        genList.append(newSubgenus)
    return genList


def getSpecificNames():
    """ read specific name data """
    tmpList = readSimpleFile("specific_names.txt")
    spList = []
    for s in tmpList:
        newName = SpecificNameClass()
        newName.setName(s[0])
        newName.setVariations(s[1])
        newName.setSynonym(s[2])
        newName.setOriginalBinomial(s[3])
        newName.setPrioritySource(s[4])
        newName.setMeaning(s[5])
        newName.setNotes(s[6])
        spList.append(newName)
    return spList


def getArt():
    """ read art data """
    tmpList = readSimpleFile("art.txt")
    artList = []
    for a in tmpList:
        newArt = ArtClass()
        newArt.setArtType(a[0])
        newArt.setCiteKey(a[1])
        newArt.setAuthor(a[2])
        newArt.setYear(a[3])
        newArt.setTitle(a[4])
        newArt.setImage(a[5])
        newArt.setExt(a[6])
        newArt.setSpecies(a[7])
        newArt.setNotes(a[8])
        artList.append(newArt)
    return artList


def getMorphology():
    """ read morphology data """
    tmpList = readSimpleFile("morphology.txt")
    morphList = []
    for m in tmpList:
        newMorph = MorphologyClass()
        newMorph.setCharacter(m[0])
        newMorph.setParent(m[1])
        newMorph.setImage(m[2])
        newMorph.setCaption(m[3])
        #newMorph.setMaxHeight(m[4])
        newMorph.setDescription(m[4])
        morphList.append(newMorph)
    return morphList


###-----End input code----###


def commonHeaderPart1(outfile,title,indexpath):
    """ part 1 of the header for all html """
    outfile.write("<!DOCTYPE HTML>\n")
    outfile.write("<html lang=\"en\">\n")
    outfile.write("  <head>\n")
    outfile.write("    <meta charset=\"utf-8\" />\n")
    outfile.write("    <title>"+title+"</title>\n")
    outfile.write("    <meta name=\"description\" content=\"Fiddler Crabs\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"128x128\" href=\"favicon128.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"96x96\" href=\"favicon96.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"72x72\" href=\"favicon72.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"48x48\" href=\"favicon48.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"32x32\" href=\"favicon32.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"24x24\" href=\"favicon24.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"icon\" sizes=\"16x16\" href=\"favicon16.png\" type=\"image/png\" />\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" href=\"apple-touch-icon-precomposed.png\">\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" sizes=\"72x72\" href=\"apple-touch-icon-72x72-precomposed.png\">\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" sizes=\"114x114\" href=\"apple-touch-icon-114x114-precomposed.png\">\n")
    outfile.write("    <link rel=\"apple-touch-icon-precomposed\" sizes=\"144x144\" href=\"apple-touch-icon-144x144-precomposed.png\">\n")
    outfile.write("    <link rel=\"stylesheet\" href=\"http://fonts.googleapis.com/css?family=Merienda+One|Lora:400,700,400italic,700italic\" />\n")
    outfile.write("    <link rel=\"stylesheet\" href=\""+indexpath+"uca_style.css?"+str(randSeed)+"\" />\n")
    outfile.write("    <link rel=\"author\" href=\"mailto:msr@asu.edu\" />\n")

def commonHeaderPart2(outfile,indexpath,incMap):
    """ part 2 of the header for all html """
    outfile.write("  </head>\n")
    outfile.write("\n")
    if incMap:
        outfile.write("  <body onload=\"initialize()\">\n")
    else:
        outfile.write("  <body>\n")
    outfile.write("    <div id=\"home\">\n")
    outfile.write("      <a href=\""+indexpath+"index.html\">Fiddler Crabs</a>\n")
    outfile.write("    </div>\n")

def commonSpeciesHTMLHeader(outfile,title,indexpath,species):
    """ for species pages, insert the map scripts """
    commonHeaderPart1(outfile,title,indexpath)
    outfile.write("    <script type=\"text/javascript\"\n")
    outfile.write("      src=\"http://maps.googleapis.com/maps/api/js?key=AIzaSyAaITaFdh_own-ULkURNKtyeh2ZR_cpR74&sensor=false\">\n")
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
    outfile.write("        var map = new google.maps.Map(document.getElementById(\"map_canvas\"),mapOptions);\n")
    if species == "":
        outfile.write("        var ctaLayer = new google.maps.KmlLayer(\"http://www.fiddlercrab.info/maps/uca.kmz\",{suppressInfoWindows: true});\n")
    else:
        outfile.write("        var ctaLayer = new google.maps.KmlLayer(\"http://www.fiddlercrab.info/maps/u_"+species+".kmz\",{suppressInfoWindows: true});\n")
    outfile.write("        ctaLayer.setMap(map);\n")
    outfile.write("      }\n")
    outfile.write("    </script>\n")
    commonHeaderPart2(outfile,indexpath,True)


def commonHTMLHeader(outfile,title,indexpath):
    commonHeaderPart1(outfile,title,indexpath)
    commonHeaderPart2(outfile,indexpath,False)


def commonHTMLFooter(outfile):
    outfile.write("\n")
    outfile.write("    <footer>\n")
    outfile.write("       <p id=\"footmap\">Visitors <script type=\"text/javascript\" src=\"http://jf.revolvermaps.com/p.js\"></script><script type=\"text/javascript\">rm2d_ki101('0','150','75','5f9t1sywiez','ff0000',20);</script></p>\n")
    outfile.write("       <p id=\"citation\"><a href=\""+citeURL+"\">How to cite this site</a></p>\n")
    outfile.write("       <p id=\"contact\">Questions or comments about the site? Contact <a href=\"mailto:msr@asu.edu\">Dr. Michael S. Rosenberg</a></p>\n")
    outfile.write("       <p id=\"copyright\">Copyright &copy; 2003&ndash;2014 All Rights Reserved</p>\n")
    outfile.write("    </footer>\n")
    outfile.write("  </body>\n")
    outfile.write("</html>\n")


def createBlankIndex(fname):
    outfile = open(fname,"w")
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
    outfile.close()


def formatReference(i,ref):
    if ref.citeKey() == "<pending>":
        return "          <li>" + ref.formattedHTML() + "</li>\n"
    else:
        try:
            return "          <li><a href=\"references/"+ref.citeKey()+".html\">" + ref.formattedHTML() + "</a></li>\n"
        except:
            print("missing label: ",ref.citeKey())


def referenceSummary(refList,yearData,yearData1900):
    outfile = codecs.open(refsumURL, "w", "utf-8")
    commonHeaderPart1(outfile,"Fiddler Crab Reference Summary","")
    outfile.write("    <script type=\"text/javascript\" src=\"https://www.google.com/jsapi\"></script>\n")
    outfile.write("    <script type=\"text/javascript\">\n")
    outfile.write("      google.load(\"visualization\", \"1\", {packages:[\"corechart\"]});\n")
    outfile.write("      google.setOnLoadCallback(drawChart);\n")
    outfile.write("      function drawChart() {\n")
    outfile.write("        var data = google.visualization.arrayToDataTable([\n")
    outfile.write("          ['Year', 'Cumulative Publications'],\n")
    for y in yearData:
        outfile.write("          ['"+str(y[0])+"', "+str(y[2])+"],\n")
    outfile.write("        ]);\n")
    outfile.write("\n")
    outfile.write("        var data2 = google.visualization.arrayToDataTable([\n")
    outfile.write("          ['Year', 'Publications'],\n")
    for y in yearData:
        outfile.write("          ['"+str(y[0])+"', "+str(y[1])+"],\n")
    outfile.write("        ]);\n")
    outfile.write("\n")
    outfile.write("        var data3 = google.visualization.arrayToDataTable([\n")
    outfile.write("          ['Year', 'Citations in DB', 'Pending'],\n")
    for y in yearData:
        outfile.write("          ['"+str(y[0])+"', "+str(y[3])+", "+str(y[1]-y[3])+"],\n")
    outfile.write("        ]);\n")
    outfile.write("\n")
    outfile.write("        var data4 = google.visualization.arrayToDataTable([\n")
    outfile.write("          ['Year', 'Publications'],\n")
    for y in yearData1900:
        outfile.write("          ['"+str(y[0])+"', "+str(y[1])+"],\n")
    outfile.write("        ]);\n")
    outfile.write("\n")
    outfile.write("        var data5 = google.visualization.arrayToDataTable([\n")
    outfile.write("          ['Year', 'Citations in DB', 'Pending'],\n")
    for y in yearData1900:
        outfile.write("          ['"+str(y[0])+"', "+str(y[2])+", "+str(y[1]-y[2])+"],\n")
    outfile.write("        ]);\n")
    outfile.write("\n")
    outfile.write("        var options = {\n")
    outfile.write("          title: \"Cumulative References by Year\", \n")
    outfile.write("          legend: { position: 'none' }\n")
    outfile.write("        };\n")
    outfile.write("\n")
    outfile.write("        var options2 = {\n")
    outfile.write("          title: \"References by Year\", \n")
    outfile.write("          legend: { position: 'none' }\n")
    outfile.write("        };\n")
    outfile.write("\n")
    outfile.write("        var options3 = {\n")
    outfile.write("          title: \"References with Citation Data in Database\", \n")
    outfile.write("          legend: { position: 'bottom' },\n")
    outfile.write("          isStacked: true,\n")
    outfile.write("        };\n")
    outfile.write("\n")
    outfile.write("        var options4 = {\n")
    outfile.write("          title: \"References by Year (since 1900)\", \n")
    outfile.write("          legend: { position: 'none' }\n")
    outfile.write("        };\n")
    outfile.write("\n")
    outfile.write("        var options5 = {\n")
    outfile.write("          title: \"References with Citation Data in Database (since 1900)\", \n")
    outfile.write("          legend: { position: 'bottom' },\n")
    outfile.write("          isStacked: true,\n")
    outfile.write("        };\n")
    outfile.write("\n")
    outfile.write("        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));\n")
    outfile.write("        chart.draw(data, options);\n")
    outfile.write("        var chart2 = new google.visualization.ColumnChart(document.getElementById('chart2_div'));\n")
    outfile.write("        chart2.draw(data2, options2);\n")
    outfile.write("        var chart3 = new google.visualization.ColumnChart(document.getElementById('chart3_div'));\n")
    outfile.write("        chart3.draw(data3, options3);\n")
    outfile.write("        var chart4 = new google.visualization.ColumnChart(document.getElementById('chart4_div'));\n")
    outfile.write("        chart4.draw(data4, options4);\n")
    outfile.write("        var chart5 = new google.visualization.ColumnChart(document.getElementById('chart5_div'));\n")
    outfile.write("        chart5.draw(data5, options5);\n")
    outfile.write("      }\n")
    outfile.write("    </script>\n")
    commonHeaderPart2(outfile,"",False)

    outfile.write("    <header>\n")
    outfile.write("      <h1>Summary of References</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    outfile.write("          <li><a href=\""+refURL+"\">Full Reference List</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <p>\n")
    outfile.write("      A summary of the {:0,} references  in the database (last updated {}).\n".format(len(refList),datetime.date.isoformat(datetime.date.today())))
    outfile.write("    </p>\n")    
    outfile.write("    <div id=\"chart2_div\" style=\"width: 1500px; height: 500px; \"></div>\n")
    outfile.write("    <div id=\"chart4_div\" style=\"width: 1500px; height: 500px; \"></div>\n")
    outfile.write("    <div id=\"chart3_div\" style=\"width: 1500px; height: 500px; \"></div>\n")
    outfile.write("    <div id=\"chart5_div\" style=\"width: 1500px; height: 500px; \"></div>\n")
    outfile.write("    <div id=\"chart_div\" style=\"width: 1500px; height: 500px; \"></div>\n")
    commonHTMLFooter(outfile)
    outfile.close()
    
    
def referencesToHTML(refList,yearData,yearData1900):
    referenceSummary(refList,yearData,yearData1900)
    outfile = codecs.open(refURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Publications","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Publications</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    outfile.write("          <li><a href=\""+refsumURL+"\">Reference/Citation Summary</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")

    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <p>\n")
    outfile.write("      Following is a fairly comprehensive list of papers, books, and theses that deal or refer to fiddler crabs.\n")
    outfile.write("      The list currently contains {:0,} references (last updated {}).\n".format(len(refList),datetime.date.isoformat(datetime.date.today())))
    outfile.write("      Many of these papers (particularly the older ones) are primarily taxonomic lists.\n")
    outfile.write("    </p>\n")    
    outfile.write("    <p>\n")
    outfile.write("      The references can also be downloaded as <a href=\"references/Uca_references.enlx\">compressed Endnote</a>, <a href=\"references/Uca_references_RIS.txt\">RIS (text)</a>, or <a href=\"references/Uca_references_RIS.xml\">RIS (XML)</a>.\n")
    outfile.write("    </p>\n")
    outfile.write("    <p>\n")
    outfile.write("      Linked references contain information on every name applied to fiddler crabs within the publication, including context and the correct name as we currently understand it.\n")
    outfile.write("      These data are in the process of being compiled (chronologically for all publications I have access to a copy of), with most references still incomplete.\n")
    outfile.write("    </p>\n")    
    outfile.write("    <p>\n")
    outfile.write("      In a list of this size, there are bound to be errors, omissions, and mistaken inclusions. Please feel free to send me corrections.\n")
    outfile.write("    </p>\n")    
    outfile.write("\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <div id=\"citation\">\n")
    outfile.write("        <ul>\n")
    for i,ref in enumerate(refList):
        outfile.write(formatReference(i+1,ref))
    outfile.write("        </ul>\n")
    outfile.write("      </div>\n")
    outfile.write("    </section>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createNameTable(citeList):
    nameRefs = {}
    for c in citeList:
        nstr = c.nameKey()
        if ("." in nstr):
            nstr = nstr[:nstr.find(".")]
        i = int(nstr)
        if c.citeKey() in nameRefs:
            nameList = nameRefs[c.citeKey()]
        else:
            nameList = {}
        nameList[i] = c.name()
        if ("." in c.nameKey()):
            nameList[c.nameKey()] = [c.name(),c.application()]
        nameRefs[c.citeKey()]= nameList
    return nameRefs


def matchNumRef(x,y):
    if (("." in x) and ("." in y)) or ((not ("." in x)) and (not ("." in y))):
        return x == y
    elif "." in x:
        return x[:x.find(".")] == y
    else:
        return y[:y.find(".")] == x


def updateCiteList(citeList):
    """ function to update correct species citations through cross-references to earlier works """
    for i,cite in enumerate(citeList):
        if cite.actual() == "=":
            crossnames = {}
            for j in range(i):
                tmp = citeList[j]
                if (tmp.citeKey() == cite.application()) and matchNumRef(tmp.nameKey(),cite.citeN()):
                    cname = tmp.name()
                    if tmp.actual() in crossnames:
                        crossnames[tmp.actual()] += 1
                    else:
                        crossnames[tmp.actual()] = 1
            if len(crossnames) == 0:
                pass
            elif len(crossnames) == 1:
                for tmp in crossnames:
                    cite.setActual(tmp)
            else:
                mcnt = max(crossnames.values())

                keylist = []
                for key in crossnames:
                    if crossnames[key] == mcnt:
                        keylist.append(key)

                if len(keylist) == 1:
                    cite.setActual(keylist[0])
                else:
                    citeName = cite.name().lower()
                    while citeName.find(" ") > -1:
                        citeName = citeName[citeName.find(" ")+1:]
                    while cname.find(" ") > -1:
                        cname = cname[cname.find(" ")+1:]

                    if citeName in keylist:
                        cite.setActual(citeName)
                    elif cname in keylist:
                        cite.setActual(cname)
                    else:
                        cite.setActual(keylist[0])

                if cite.nameNote() == ".":
                    cite.setNameNote("in part")
                else:
                    cite.setNameNote("in part; " + cite.nameNote())


def createSpeciesLink(species,status,path):
    if status == "fossil":
        sC = fossilImage
    else:
        sC = ""
    return "<a href=\""+path+"u_"+species+".html\"><em class=\"species\">Uca "+species+sC+"</em></a>"


def formatNameString(x):
    """ properly emphasize species names, but not non-name signifiers """
    # get rid of [#] when present
    if "{" in x:
        x = x[:x.find("{")-1]

    if "var." in x.lower():
        p = x.lower().find("var.")
        return "<em class=\"species\">"+x[:p]+"</em> "+x[p:p+4]+" <em class=\"species\">"+x[p+4:]+"</em>"
    elif " var " in x.lower():
        p = x.lower().find(" var ")
        return "<em class=\"species\">"+x[:p]+"</em> "+x[p:p+4]+" <em class=\"species\">"+x[p+4:]+"</em>"
    elif "subsp." in x.lower():
        p = x.lower().find("subsp.")
        return "<em class=\"species\">"+x[:p]+"</em> "+x[p:p+6]+" <em class=\"species\">"+x[p+6:]+"</em>"
    elif " forme " in x.lower():
        p = x.lower().find(" forme ")
        return "<em class=\"species\">"+x[:p]+"</em> "+x[p:p+6]+" <em class=\"species\">"+x[p+6:]+"</em>"
    elif " f. " in x.lower():
        p = x.lower().find(" f. ")
        return "<em class=\"species\">"+x[:p]+"</em> "+x[p:p+3]+" <em class=\"species\">"+x[p+3:]+"</em>"
    #elif "sp." in x.lower():
    #    p = x.lower().find("sp.")
    #    return "<em class=\"species\">"+x[:p]+"</em> "+x[p:p+3]+" <em class=\"species\">"+x[p+3:]+"</em>"
    #elif "spp." in x.lower():
    #    p = x.lower().find("spp.")
    #    return "<em class=\"species\">"+x[:p]+"</em> "+x[p:p+4]+" <em class=\"species\">"+x[p+4:]+"</em>"
    else:
        return "<em class=\"species\">"+x+"</em>"


def nameToFileName(x):
    """ Convert a full species name into a valid file name """
    x = x.replace(" ","_")
    x = x.replace("(","")
    x = x.replace(")","")
    x = x.replace(",","")
    x = x.replace(".","")
    x = x.replace("æ","_ae_")
    x = x.replace("ö","_o_")
    x = x.replace("œ","_oe_")
    x = x.replace("ç","_c_")
    return x


def cleanSpecificName(x):
    """ function to extract the specific names from binomials """
    if not " " in x:
        return ""
    else:
        if "{" in x:
            x = x[:x.find("{")-1]        
        y = x.split(" ")
        x = y[len(y)-1].lower()
        skipList = ["sp.","spp.","var.","a","ete","panema","pagurus","quadratus","albidus","vociferans","(gelasimus)","raniformis","nigra"]
        if x in skipList or ("gruppe" in x):
            return ""
        else:
            return x.lower()


def outputNameTable(IsName,outfile,itemList,uniqueList,notecnt,comcnt,refDict,nameTable):
    firstName = True
    ncols = 4
    if notecnt > 0:
        ncols += 1
    if comcnt > 0:
        ncols += 1

    for n in itemList:
        outfile.write("    <tr>\n")
        if IsName:
            nref = n.citeKey()
        else:
            nref = n.name()
        if nref in uniqueList:
            if firstName:
                firstName = False
            else:
                outfile.write("      <td class=\"rowspacer\" colspan=\""+str(ncols)+"\">&nbsp;</td>\n")                        
                outfile.write("    </tr>\n")
                outfile.write("    <tr>\n")

            if nref == ".":
                outfile.write("      <td>&nbsp;</td>\n")
            elif IsName: # output citation
                crossref = refDict[nref]
                outfile.write("      <td><a href=\"../references/"+crossref.citeKey()+".html\">"+crossref.citation()+"</a></td>\n")
            else: # output species name
                outfile.write("      <td><a href=\"../names/"+nameToFileName(nref)+".html\">"+formatNameString(nref)+"</a></td>\n")

            # common names
            if comcnt > 0:
                if n.common() == ".":
                    outfile.write("      <td>&nbsp;</td>\n")
                else:
                    outfile.write("      <td>"+n.common()+"</td>\n")
            outfile.write("      <td>"+n.where()+"</td>\n")
            uniqueList = uniqueList - {nref}
        else:
            outfile.write("      <td>&nbsp;</td>\n")
            if comcnt > 0:
                outfile.write("      <td>&nbsp;</td>\n")
            outfile.write("      <td>&nbsp;</td>\n")
        # applies to...
        if n.context() == "location":
            outfile.write("      <td>location: "+n.application()+"</td>\n")
        elif n.context() == "citation":
            if (n.application() in refDict) and (n.application() in nameTable):
                crossref = refDict[n.application()]
                nstr = n.citeN()
                if nstr == "0":
                    outfile.write("      <td>citation: <a href=\"../references/"+crossref.citeKey()+".html\">"+crossref.citation()+"</a></td>\n")
                else:
                    if "." in nstr:
                        #print(n[0],nstr,n[6])
                        extraref = " ["+nameTable[n.application()][nstr][1]+"]"
                        refname = nameTable[n.application()][nstr][0]
                    else:
                        extraref = ""                                
                        #print(nstr,n)
                        refname = nameTable[n.application()][int(nstr)]
                    outfile.write("      <td>citation: <a href=\"../references/"+crossref.citeKey()+".html\">"+crossref.citation()+"</a> → "+formatNameString(refname)+extraref+"</td>\n")
            else:
                outfile.write("      <td>citation: "+n.application()+"</td>\n")
        elif n.context() == "specimen":
            if n.application() == "?":
                outfile.write("      <td>specimen: unknown locality</td>\n")
            else:
                outfile.write("      <td>specimen: "+n.application()+"</td>\n")
        elif n.context() == "unpublished":
            outfile.write("      <td>unpublished name <em class=\"species\">"+n.application()+"</em></td>\n")
        else: # "n/a"
            outfile.write("      <td>&nbsp;</td>\n")

        # accepted species name                                
        if n.actual() in {"?","=","."}:
            outfile.write("      <td>"+n.actual()+"</td>\n")
        elif n.actual() == "n/a":
            outfile.write("      <td>&nbsp;</td>\n")                    
        elif n.actual()[0] == ">":
            outfile.write("      <td><em class=\"species\">"+n.actual()[1:]+"</em></td>\n")
        else:
            outfile.write("      <td><a href=\"../u_"+n.actual()+".html\"><em class=\"species\">Uca "+n.actual()+"</em></a></td>\n")
        # notes
        if notecnt > 0:
            if n.nameNote() == ".":
                outfile.write("      <td>&nbsp;</td>\n")
            else:
                outfile.write("      <td>"+n.nameNote()+"</td>\n")                 
        outfile.write("    </tr>\n")
    outfile.write("    </table>\n")
    

def referencePages(refList,refDict,citeList):
    createBlankIndex("references/index.html")
    nameTable = createNameTable(citeList)
    updateCiteList(citeList)
    for ref in refList:
        if ref.citeKey() != "<pending>":
            outfile = codecs.open("references/"+ref.citeKey()+".html", "w", "utf-8")
            commonHTMLHeader(outfile,ref.citation(),"../")
            outfile.write("    <header>\n")
            outfile.write("      <h1>"+ref.citation()+"</h1>\n")
            outfile.write("      <h2>"+ref.formattedHTML()+"</h2>\n")
            outfile.write("      <nav>\n")
            outfile.write("        <ul>\n")
            outfile.write("          <li><a href=\"../"+refURL+"\">Full Reference List</a></li>\n")
            outfile.write("        </ul>\n")
            outfile.write("      </nav>\n")
            outfile.write("    </header>\n")
            outfile.write("\n")
            # find names for this citation 
            names = []
            citesTo = []
            for c in citeList:
                if c.citeKey() == ref.citeKey():
                    names.append(c)
                if c.application() == ref.citeKey():
                    citesTo.append(c)
            startedNote = False
            comcnt = 0
            notecnt = 0
            uniquenames = set()
            for n in names:
                if n.generalNote() != ".":
                    if not startedNote:
                        outfile.write("    <p>\n")
                        startedNote = True
                    outfile.write("      "+n.generalNote()+"\n")
                if n.common() != ".":
                    comcnt += 1
                if n.nameNote() != ".":
                    notecnt += 1
                uniquenames = uniquenames | {n.name()}
            if startedNote:
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
                if notecnt > 0:
                    outfile.write("        <th>Note(s)</th>\n")
                outfile.write("      </tr>\n")

                outputNameTable(False,outfile,names,uniquenames,notecnt,comcnt,refDict,nameTable)
            else:
                outfile.write("    Data not yet available.\n")

            if len(citesTo) > 0:
                outfile.write("    <h3>This Publication is Cited By</h3>\n")
                outfile.write("    <p>\n")
                cs = set()
                for c in citesTo:
                    if c.citeKey() in refDict:
                        crossref = refDict[c.citeKey()]
                        cs = cs | {"<a href=\""+crossref.citeKey()+".html\">"+crossref.citation()+"</a>"}
                    else:
                        cs = cs | {c.citeKey()}
                cl = []
                for x in cs:
                    cl.append(x)
                cl.sort()
                outfile.write("     "+", ".join(cl)+"\n")                
                outfile.write("    </p>\n")
            else:
                outfile.write("    <p>\n")
            outfile.write("    </p>\n")

            commonHTMLFooter(outfile)
            outfile.close()


def cleanName(x):
    """ function to clean up names so that variation such as punctuation does not prevent a match """
    x = x.replace(", var."," var.")
    if "{" in x:
        x = x[:x.find("{")-1]
    return x


def createBinomialNamePage(name,namefile,refDict,citeList,nameTable,specName):
    """ create a page listing all citations using a specific binomial """
    outfile = codecs.open("names/"+namefile+".html", "w", "utf-8")
    commonHTMLHeader(outfile,name,"../")
    outfile.write("    <header>\n")
    outfile.write("      <h1>"+formatNameString(name)+"</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    if specName != "":
        outfile.write("          <li><a href=\"sn_"+specName+".html\">"+formatNameString(specName)+"</a></li>\n")
    outfile.write("          <li><a href=\"index.html\">Full Name Index</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")

    # find citations for this name 
    cites = []
    for c in citeList:
        clean = cleanName(c.name())
        if clean.lower() == name.lower():
            cites.append(c)
    comcnt = 0
    notecnt = 0
    uniquecites = set()
    for c in cites:
        if c.common() != ".":
            comcnt += 1
        if c.nameNote() != ".":
            notecnt += 1
        uniquecites = uniquecites | {c.citeKey()}

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
    if notecnt > 0:
        outfile.write("        <th>Note(s)</th>\n")
    outfile.write("      </tr>\n")
    outputNameTable(True,outfile,cites,uniquecites,notecnt,comcnt,refDict,nameTable)
    outfile.write("    <p>\n")
    outfile.write("    </p>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createSpecificNamePage(name,binomialNames,refDict):
    """ create a page with the history of a specific name """
    outfile = codecs.open("names/sn_"+name.name()+".html", "w", "utf-8")
    commonHTMLHeader(outfile,name.name(),"../")
    outfile.write("    <header>\n")
    outfile.write("      <h1>"+formatNameString(name.name())+"</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    outfile.write("          <li><a href=\"index.html\">Full Name Index</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <section class=\"topspsection\">\n")
    outfile.write("      <h3>History</h3>\n")
    outfile.write("      <dl>\n")
    if name.synonym() != ".":
        if (name.synonym() in name.variations()):
            outfile.write("        <dt>Species</dt>\n")
        else:
            outfile.write("        <dt>Primary Senior Synonym</dt>\n")
        if name.synonym() == "?":
            outfile.write("          <dd>Unknown</dd>\n")
        elif name.synonym().startswith(">"):
            outfile.write("          <dd><em class=\"species\">"+name.synonym()[1:]+"</em></dd>\n")
        else:
            outfile.write("          <dd>"+createSpeciesLink(name.synonym(),"","../")+"</dd>\n")
    outfile.write("        <dt>Original Usage</dt>\n")
    outfile.write("          <dd>"+formatNameString(name.originalBinomial())+"</dd>\n")
    outfile.write("        <dt>Original Source with Priority</dt>\n")
    if name.prioritySource() != ".":
        try:
            ref = refDict[name.prioritySource()]
            refname = ref.formattedHTML()
        except:
            print(name.prioritySource())
    else:
        refname = "."
    outfile.write("          <dd>"+refname+"</dd>\n")
    outfile.write("        <dt>Derivation</dt>\n")
    outfile.write("          <dd>"+name.meaning()+"</dd>\n")
    outfile.write("      <dl>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")
    if name.notes() != ".":
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h3>Notes/Comments</h3>\n")
        outfile.write("      <p>\n")
        outfile.write("        "+name.notes()+"\n")
        outfile.write("      </p>\n")
        outfile.write("    </section>\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h3>Binomials Using this Specific Name</h3>\n")
    outfile.write("      <ul>\n")
    for n in binomialNames:
        x = cleanSpecificName(n)
        tmpnamelist = name.variations().split(";")
        if (x != "") and (x in tmpnamelist):
            namefile = nameToFileName(n)
            outfile.write("      <li><a href=\""+namefile+".html\">"+formatNameString(n)+"</a></li>\n")
    outfile.write("      </ul>\n")
    outfile.write("    </section>\n")
    
    commonHTMLFooter(outfile)
    outfile.close()


def matchSpecificName(name,specificNames):
    """ match the specific name from a binomial to the list of accepted specific names """
    c = cleanSpecificName(name)
    if c == "":
        return c
    else:
        y = ""
        for x in specificNames:
            matchList = x.variations().split(";")
            if c in matchList:
                y = x.name()
        return y


def binomialNamePages(refDict,citeList,specificNames):
    """ create an index of binomials and specific names """
    nameTable = createNameTable(citeList)
    uniqueNames = list()    
    nameSet = set()
    for c in citeList:
        if c.name() != ".":
            clean = cleanName(c.name())
            if not clean.lower() in nameSet:
                nameSet = nameSet | {clean.lower()}
                uniqueNames.append(clean)
    uniqueNames.sort(key = lambda s: s.lower())

    # create name index
    outfile = codecs.open("names/index.html", "w", "utf-8")
    commonHTMLHeader(outfile,"Name Index","../")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Name Index</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("    <p>\n")
    outfile.write("      This is an index of every scientific name (including all alternate spellings) which have been\n")
    outfile.write("      applied to fiddler crabs or placed in the fiddler crab genus.\n")
    outfile.write("    </p>\n")
    outfile.write("    <p>\n")
    outfile.write("      For the binomials, every publication\n")
    outfile.write("      which used that name is provided, as well as the best estimate as to which species,\n")
    outfile.write("      as we understand them today, the author was actually referring.\n")
    outfile.write("    </p>\n")
    outfile.write("    <p>\n")
    outfile.write("      For the specific names, only the primary spelling is listed below\n")
    outfile.write("      but all alternate spellings and inclusive binomials are included on the linked page,\n")
    outfile.write("      as well as general information on the status of each specific name.\n")
    outfile.write("    </p>\n")
    outfile.write("    <div class=\"namecol\">\n")
    outfile.write("      <h3>Binomials (and other Compound Names)</h3>\n")
    outfile.write("      <ul>\n")
    outfile.write("\n")
    for name in uniqueNames:
        sName = matchSpecificName(name,specificNames)
        namefile = nameToFileName(name)
        outfile.write("        <li><a href=\""+namefile+".html\">"+formatNameString(name)+"</a></li>\n")
        createBinomialNamePage(name,namefile,refDict,citeList,nameTable,sName)
    outfile.write("      </ul>\n")
    outfile.write("    </div>\n")
    outfile.write("    <div class=\"namecol\">\n")
    outfile.write("      <h3>Specific Names</h3>\n")
    outfile.write("      <ul>\n")
    outfile.write("\n")
    for name in specificNames:
        outfile.write("        <li><a href=\"sn_"+name.name()+".html\">"+formatNameString(name.name())+"</a></li>\n")
        createSpecificNamePage(name,uniqueNames,refDict)
    outfile.write("      </ul>\n")
    outfile.write("    </div>\n")
    commonHTMLFooter(outfile)
    outfile.close()
    return uniqueNames


def specificNamePages(citeList,specificNames):
    """ produces a list of specific names not in the accepted list """
    uniqueNames = list()    
    nameSet = set()
    for c in citeList:
        if c.name() != ".":
            clean = cleanSpecificName(c.name())
            if (not (clean in nameSet)) and (clean != ""):
                nameSet = nameSet | {clean}
                uniqueNames.append(clean)
    uniqueNames.sort()

    outfile = open("missing specific names.txt","w")
    for n in uniqueNames:
        isFound = False
        for s in specificNames:
            if n in s.variations():
                isFound = True
        if not isFound:
            print("Missing: "+n)
            outfile.write(n+"\n")
    outfile.close()


def createMapHTML(species):
    """ output geopgraphic ranges to HTML """
    regions = ("Eastern Atlantic","Western Atlantic","Eastern Pacific","Indo-West Pacific")
    outfile = codecs.open(mapURL, "w", "utf-8")
    commonSpeciesHTMLHeader(outfile,"Fiddler Crab Geographic Ranges","","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Geographic Ranges</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <section class=\"topspsection\">\n")
    outfile.write("      <p class=\"map_section\">\n")
    outfile.write("        <div id=\"map_canvas\" style=\"width: 600px; height: 400px;\"></div>\n")
    outfile.write("      </p>\n")
    outfile.write("      <p>\n")
    outfile.write("        The above map shows the approximate density of species richness, with denser color where more species are found. "+\
                  "The range for each individual species can be found on its page, including specific citations for the range information. "+\
                  "Below, species are grouped by broad geographic region.\n")
    outfile.write("      </p>\n")
    outfile.write("    </section>\n")
    for r in regions:
        outfile.write("\n")  
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2>"+r+"</h2>\n")
        outfile.write("      <ul id=\"splist\">\n")
        for s in species:
            if s.region() == r:
                if s.status() != "fossil":
                    outfile.write("        <li>"+createSpeciesLink(s.species(),"","")+"</li>\n")                
        outfile.write("      </ul>\n")
        outfile.write("    </section>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createCommonNamesHTML(refDict):
    """ output common names to HTML """
    outfile = codecs.open(commonURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Common Names of Fiddler Crabs","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Common Names of Fiddler Crabs</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("    <p>\n")
    outfile.write("      Following is a summery of common names for crabs in the genus <em class=\"species\">Uca</em>.\n")
    outfile.write("      See <a href=\"uca_species.html\">individual species</a> for more information on the common names of a particular species.\n")
    outfile.write("    </p>\n")
    outfile.write("    <dl class=\"common\">\n")
    outfile.write("      <dt>Fiddler Crab</dt>\n")
    outfile.write("        <dd>\n")
    outfile.write("          The common English term &ldquo;fiddler crab&rdquo; appears to have originated\n")
    outfile.write("          on the East coast of the United States (or more precisely, among the English\n")
    outfile.write("          speaking residents of the British colonies that eventually becamse the U.S.).\n")
    outfile.write("          Although the name is commonly used in\n")
    outfile.write("          English, many people are unaware of why the name is applied to these\n")
    outfile.write("          crabs. Field observation makes it obvious that the name derives from the\n")
    outfile.write("          motion of the small claw when male crabs are feeding. The constant movement \n")
    outfile.write("          of the small claw from the surface to the mouth and back makes it appear as \n")
    outfile.write("          if the crab is moving a bow across the large claw (the fiddle).\n")
    outfile.write("          As is shown below, over time many scientists have struggled to come up with an explanation for\n")
    outfile.write("          this name, with mistaken interpretations at times carrying over from person to person.\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          The earliest mention of this name appears in <a href=\"references/Lawson1709.html\">John Lawson's <em>A New Voyage\n")
    outfile.write("          to Carolina</em></a>, published in 1709 (and republished as <a href=\"references/Lawson1714.html\"><em>The History of\n")
    outfile.write("          Carolina</em></a> in 1714) (p. 121):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            There is a sort of small Land-Crab, which we call a Fiddler, that runs into\n")
    outfile.write("            a Hole when any thing pursues him.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          and again (p. 162):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            Fidlars are a sort of small Crabs, that lie in Holes in the Marshes. The\n")
    outfile.write("            Raccoons eat them very much. I never knew any one try, whether they were\n")
    outfile.write("            good Meat or no.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          A century later, in discussing <em class=\"species\">Ocypode pugilator</em>\n")
    outfile.write("          (<em class=\"species\">Uca pugilator</em>), <a href=\"references/Say1817.html\">Thomas Say (1817)</a> reports (p. 72):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            This is the animal so well known to the inhabitants of the sea coast under the\n")
    outfile.write("            name of &ldquo;Fiddler,&rdquo; an appellation almost universal, and probably\n")
    outfile.write("            derived from a supposed similitude between the large hand of the male and the\n")
    outfile.write("            fiddler or violin.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          Note that he associates the name with the large claw, but without the motion&mdash;a half-correct answer we will see again.\n")
    outfile.write("          <a href=\"references/Gould1841.html\">Gould (1841)</a> has a similar explanation when discussing the crab <em class=\"species\">Gelasimus vocans</em>\n")
    outfile.write("          (likely both <em class=\"species\">Uca pugilator</em> and <em class=\"species\">U. pugnax</em>) in Massachusetts (p. 325):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            It is well distinguished by its large claw, which is\n")
    outfile.write("            sometimes on the right side and sometimes on the left, and has\n")
    outfile.write("            gained for it the name of the &ldquo;Fiddler Crab.&rdquo;\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          <a href=\"references/DeKay1844.html\">De Kay (1844)</a> uses the term with respect to the same species in New York, but with a slightly different explanation (p. 14):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The movable finger is curved, and extends somewhat beyond the tip of the other, which is\n")
    outfile.write("            almost straight ; from this results a figure somewhat resembling the bow of a violin, and\n")
    outfile.write("            has probably suggested its popular name of <em>Fiddler Crab.</em>\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          His explanation of the origin of the name is unusual:\n")
    outfile.write("          that the curving dactyl on the large claws looks like the bow over the violin (the pollex and manus).\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          In the book <a href=\"references/Lord1867.html\"><em>Crab, Shrimp, and Lobster Lore</em> (1867)</a>, William Lord reports\n")
    outfile.write("          a different spin on the fishermen's perception of the fiddler crab (p. 29-30):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            These are the <em>swimming Crabs,</em> of which there are numerous species.\n")
    outfile.write("            These differ materially from the kinds we have described, in habits, \n")
    outfile.write("            appearance, and structure. By the use of their powerful oar-like legs they\n")
    outfile.write("            are enabled to propel themselves through the water with great rapidity and\n")
    outfile.write("            precision, and by darting among the meshes of the fishing-nets they becomes\n")
    outfile.write("            so helplessly entangled, that\n")
    outfile.write("            a &ldquo;<em>Fiddler Crab</em>&rdquo; (as it is sometimes called from\n")
    outfile.write("            the rapidity with which it works its elbows) in a <em>transel net</em>, is\n")
    outfile.write("            often used by fishermen as a standard with which to compare the cases of the\n")
    outfile.write("            most utter bewilderment.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          Mark Twain also references them in Chapter 48 of <a href=\"references/Twain1883.html\"><em>Life on the Mississippi</em>\n")
    outfile.write("          (1883)</a>:\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The drainage-ditches were everywhere alive with little\n")
    outfile.write("            crabs&mdash;&lsquo;fiddlers.&rsquo;\n")
    outfile.write("            One saw them scampering sidewise in every direction whenever they heard a\n")
    outfile.write("            disturbing noise. Expensive pests, these crabs; for they bore into the\n")
    outfile.write("            levees, and ruin them.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          At some point a number of authors come to the erroneous conclusion that the name comes from the waving of the large claw (a concept that makes little sense if one thinks about it).\n")
    outfile.write("          In his 1886 book <a href=\"references/Kingsley1886.html\"><em>The Standard Natural History</em></a>, John S. Kingsley states (p. 64):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            When these crabs are disturbed their claws are brandished in an amusing manner, strikingly suggestive of the motions of a violinist, whence these forms have received the common name of &ldquo;Fiddler Crabs.&rdquo;\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          Angelo Heilprin makes an even more confusing explanation in his 1888 book <a href=\"references/Heilprin1888.html\"><em>The Animal Life of Our Sea-Shore</em></a> (p. 82).\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            When provoked, the animal brandishes this claw in a somewhat threatening manner, which has been likened to the pulling of a violin-bow&mdash;hence the name of 'fiddler'&mdash;and by others to the action of beckoning or calling (hence 'calling crabs').\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          And again in Johnson and Snook's book, <a href=\"references/Johnson1927.html\"><em>Seashore Animals of the Pacific Cost</em> (1927)</a>, p. 400:\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The males are frequently seen to brandish the large claw in a peculiar way. First, they reach out with it as far as it will go, then they bring it toward the body with a sudden movement.\n")
    outfile.write("            This motion which has probably suggested the name &ldquo;fiddler&rdquo; crab is carried on during the breeding season and is presecuted more vigorously when a female crab is nearby.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          Similar confusing claims are made by <a href=\"references/Boyce1924.html\">Boyce (1924)</a>, while <a href=\"references/Boone1927.html\">Boone (1927)</a> returns to the resemblance of the large claw (without associated motion) (see quotes under &ldquo;Calling Crab&rdquo; below).\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          By 1888, Kingsley changes his explanation to a more sensible one in in a paper in <a href=\"references/Kingsley1888.html\"><em>The American Naturalist</em>\n")
    outfile.write("          (p. 889-890)</a>:\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            When you draw near the beach where these crabs are abundant, no matter how cautiously you have\n")
    outfile.write("            approached, there is a hurried rush of myraids of these crabs, each scuttling away as fast as four\n")
    outfile.write("            pairs of legs will carry it, to a a place of safety.\n")
    outfile.write("            At such a time the appropriateness of the common name is seen.\n")
    outfile.write("            In every direction are the fiddlers, each playing its small claw across the enormous fellow\n")
    outfile.write("            in the most amusing manner. No matter how often seen,\n")
    outfile.write("            one cannot help thinking of the musician&mdash;usually bald-headed&mdash;away down to the left of\n")
    outfile.write("            the orchestra, who so vigorously saws the bass notes from the viol.\n")
    outfile.write("            Let the latter scamper awasy, viol and all, as rapidly as does the crab, and the simile would be complete.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          <a href=\"references/Paulmier1905.html\">Paulmier (1905)</a> gives a similar explanation (p. 148):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            These three species are commonly known as &ldquo;fiddlers&rdquo;; for, when running over the beach with the large\n")
    outfile.write("            claw held out in front of them and the small one sawing in front of it, they lucicrously resemble a man carrying a bass viol.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          Some non-English speakers have picked up this term and translated fiddler\n")
    outfile.write("          crab into their own language, such as <b>Cangrejo Violinista</b> in\n")
    outfile.write("          Latin-American Spanish and <b>Caranguejo Violinista</b> in Brazilian\n")
    outfile.write("          Portuguese.\n")
    outfile.write("        </dd>\n")

    outfile.write("\n")
    outfile.write("      <dt>Calling Crab</dt>\n")
    outfile.write("        <dd>\n")
    outfile.write("          Less commonly used in English, the term &ldquo;Calling Crab&rdquo; derives\n")
    outfile.write("          from one of the earliest scientific papers to include these crabs, <a href=\"references/Rumphius1705.html\">Rumphius\n")
    outfile.write("          (1705)</a>. Rumphius names one of his species <em class=\"species\">Cancer vocans</em>\n")
    outfile.write("          which is Latin for &ldquo;calling crab&rdquo; or &ldquo;gesturing crab.&rdquo; He also reports the name\n")
    outfile.write("          &ldquo;Cattam Pangel&rdquo; which appears to most likely be a form of Malay \n")
    outfile.write("          meaning &ldquo;summoning crab,&rdquo; and is probably from where he derived the Latin name.\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          The Latin name <em class=\"species\">Cancer vocans</em> (today <em class=\"species\">\n")
    outfile.write("          Uca vocans</em>) was adopted by <a href=\"references/Linnaeus1758.html\">Linnaeus\n")
    outfile.write("          (1758)</a> and became the general name under which this group was known in\n")
    outfile.write("          Continental Europe. By 1778, writing in French, <a href=\"references/DeGeer1778.html\">DeGeer</a> uses the French\n")
    outfile.write("          translation of this term &ldquo;Crabe appellant,&rdquo; which appears to\n")
    outfile.write("          become a general term for all of these crabs, not just the single species.\n")
    outfile.write("          Similarly, writing in German, <a href=\"references/Herbst1782.html\">Herbst (1782)</a> builds off the German word\n")
    outfile.write("          &ldquo;winken&rdquo; (which means wave, beckon, signal or hail) to call\n")
    outfile.write("          two versions of these crabs &ldquo;Der kleine Winker&rdquo; and\n")
    outfile.write("          &ldquo;Der grosse Winker&rdquo; (essentially &ldquo;the little waver&rdquo; and &ldquo;the\n")
    outfile.write("          great waver&rdquo;). Eventually, the entire group of crabs becomes \n")
    outfile.write("          becomes known as <b>Winkerkrabbe</b> (waving crabs) in German.\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          The term does find its way into English, such as <a href=\"references/Gosse1851.html\">Gosse (1851)</a> discussing Jamaica (p. 50-51):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            At this time it is seen to be pierced with innumerable little holes; and hundres of a tiny Calling-crab\n")
    outfile.write("            (<em class=\"species\">Gelasimus vocans</em>) are running over its surface, the males of which hold up their enormous claws in front, as if in defiance.\n")
    outfile.write("            At the approach of an intruder, every one hastens into his burrow, and in a moment the muddy bank, that was alive with the moving\n")
    outfile.write("            atoms, is perfectly still&hellip;The little Crabs are very swift and wary, so that it is difficult to capture them, except by making a\n")
    outfile.write("            sudden rush from a distance among them.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          or <a href=\"references/Tennent1861.html\">Tennent (1861)</a> in Sri Lanka (p. 477-478):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            ...the nimble little Calling Crabs scamper over moist sands, carrying aloft the\n")
    outfile.write("            enormous hand (sometimes larger than the rest of the body), which is their peculiar\n")
    outfile.write("            characteristic, and which, from its beckoning gesture has suggested their popular name.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          or <a href=\"references/Paulmier1905.html\">Paulmier (1905)</a> in New York (p. 148):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The old specific name vocans was given them because, when the tide was out, they\n")
    outfile.write("            appeared to stand on the beach and wave their great claws, calling it back again.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          <a href=\"references/Boyce1924.html\">Boyce (1924)</a> prefers &ldquo;Calling Crab&ldquo; to &ldquo;Fiddler Crab&rdquo;, at least in part\n")
    outfile.write("          due to his misunderstanding of where &ldquo;Fiddler Crab&rdquo; comes from (p. 250):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The enlarged chela is constantly being waived in the air as if beckoning or calling, and this has suggested the term Calling Crab. The alternate name, Fiddler Crab,\n")
    outfile.write("            is less appropriate, for the movement is really not suggestive of the action of a violinist drawing the bow across the strings.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          <a href=\"references/Boone1927.html\">Boone (1927)</a> also explains both names:\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The odd aspect of this group of crabs, resulting from the strikingly disproportionate size attained by one of the claws in the male\n")
    outfile.write("            and the curious manner in which the little creatures handle the claw, has been a source of comment among the peoples of many lands,\n")
    outfile.write("            which has found expression in a series of quaint common names. Among English-speaking folk, it is known as the &ldquo;calling crab&rdquo; because\n")
    outfile.write("            it seems to be forever beckoning with its huge claws. Another name, and the one by the way, most widely used among the coasts of the southern United States is &ldquo;fiddler&rdquo; crab, from the fancied resemblance of the great claw to this musical instrument.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")

    outfile.write("\n")
    outfile.write("      <dt>シオマネキ (Shio-maneki)</dt>\n")
    outfile.write("        <dd>\n")
    outfile.write("          In 1835, <a href=\"references/deHaan1835.html\">de Haan</a> (writing in Latin) reports that the crab he calls\n")
    outfile.write("          <em class=\"species\">Ocypode (Gelasimus) arcuata</em> (today <em class=\"species\">Uca \n")
    outfile.write("          arcuata</em>) is known\n")
    outfile.write("          as &ldquo;Siho maneki&rdquo; in Japanese (シホマネキ). He translates this into Latin as\n")
    outfile.write("          &ldquo;maris refluxum annuens.&rdquo; This has generally been translated into\n")
    outfile.write("          English as &ldquo;beckoning for the return of the tide&rdquo; or &ldquo;tide\n")
    outfile.write("          caller.&rdquo;\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          This term is first mentioned in English by <a href=\"references/Boone1927.html\">Boone (1927)</a> (p. 273):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The Japanese have woven a legend around the species of <em class=\"species\">Uca</em> common in Japan, and give it the name <em>Siho maneki,</em> which means &ldquo;beckoning for the return of the tide.&rdquo;\n")
    outfile.write("          </blockquote>\n")
    outfile.write("          Ricketts &amp; Calvin copy this in their book\n")
    outfile.write("          <em>Between Pacific Tides</em> (probably in the original 1939 edition, but\n")
    outfile.write("          definitely by the revised edition of 1948). For example, in the <a href=\"references/Ricketts1985.html\">fifth edition (1985)</a>, on p. 356:\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            The Japanese call the fiddler crab <em>siho maneki,</em> which translates as\n")
    outfile.write("            &ldquo;beckoning for the return of the tide.&rdquo; It is too picturesque a\n")
    outfile.write("            name to quibble over, but one might reasonably ask why Mahomet does not go to\n")
    outfile.write("            the mountain, for the presumably free-willed fiddler digs its burrow as far\n")
    outfile.write("            away from the tide as it can get without abandoning the sea entirely.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          Today there is a slight difference in the Japanese spelling (シオマネキ vs. シホマネキ) (note 2<sup>nd</sup> character) and English transliteration\n")
    outfile.write("          (&ldquo;shio-maneki&rdquo; vs. &ldquo;siho-maneki&rdquo;) than presented by de Haan and subsequent authors. I do not know if this change is due to the way\n")
    outfile.write("          we transliterate or represents an error by <a href=\"references/deHaan1835.html\">de Haan (1835)</a> which carried over\n")
    outfile.write("          to later authors.\n")
    outfile.write("        </dd>\n")
    outfile.write("\n")
    outfile.write("      <dt>Chama-maré</dt>\n")
    outfile.write("        <dd>\n")
    outfile.write("          Brazilian Portuguese, translating to &ldquo;tide recaller&rdquo; in English.\n")
    outfile.write("          Not sure if this derives from the Japanese or if it independently evolved.\n")
    outfile.write("        </dd>\n")
    outfile.write("\n")
    outfile.write("      <dt>Maestro-sastre</dt>\n")
    outfile.write("        <dd>\n")
    outfile.write("          Translates to &ldquo;master tailor&rdquo; in English. Rathbun (<a href=\"references/Rathbun1911.html\">1911</a>, <a href=\"references/Rathbun1918.2.html\">1918</a>) reports this as a local name for <em class=\species\">Uca princeps</em> in Peru.\n")
    outfile.write("          Likely derives from the same feeding motion that gave rise to &ldquo;fiddler crab,&rdquo;\n")
    outfile.write("          with the motion of the small claw looking like someone rapidly sewing stitches.\n")
    outfile.write("        </dd>\n")
    outfile.write("        <dd>\n")
    outfile.write("          <a href=\"references/Boone1927.html\">Boone (1927)</a> also reports on this term (p. 273):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            To the Peruvians these crabs are known as &ldquo;<em>maestro-sastre,</em>&rdquo; (master-tailor). Long before the coming of Columbus to the New World, these little crabs were woven in the folk-lore of the Indians who dwelt along the coast.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")
    outfile.write("\n")
    outfile.write("      <dt>Deaf Ear Crabs</dt>\n")
    outfile.write("        <dd>\n")
    outfile.write("          Common name on Jamaica. Appears to come from the superstition that deafness\n")
    outfile.write("          and earache could be cured by pouring the juice from a crushed living crab into\n")
    outfile.write("          the ear. <a href=\"references/Rathbun1918.2.html\">Rathbun (1918)</a> reported hearing this story from P.W. Jarvis of\n")
    outfile.write("          Kingston, specifically in reference to <em class=\"species\">Uca rapax.</em>\n")
    outfile.write("          <a href=\"references/Barnwell1986.1.html\">Barnwell (1986)</a> reported that the name was generally applied to all fiddler\n")
    outfile.write("          crabs, although modern day residents didn't know the significance, the name\n")
    outfile.write("          apparently having stuck while the folklore apparently was lost.\n")
    outfile.write("        </dd>\n")

    outfile.write("      <dt>Dhobi Crabs</dt>\n")
    outfile.write("        <dd>\n")
    outfile.write("          <a href=\"references/Henderson1893.html\">Henderson (1893)</a> reports this as the local name on the eastern coast of India, near Madras (p. 329):\n")
    outfile.write("          <blockquote>\n")
    outfile.write("            Locally the Gelasimi are known as &ldquo;dhobi crabs,&rdquo; doubtless from the resemblance\n")
    outfile.write("            of their beckoning movement to the manner in which the native washerman swings\n")
    outfile.write("            the clothes over his head in the act of pounding them against a flat stone.\n")
    outfile.write("          </blockquote>\n")
    outfile.write("        </dd>\n")

    outfile.write("    </dl>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def connectRefsToSpecies(species,citeList):
    """ create list of references for each species """
    # create dictionary with empty reference lists
    speciesRefs = {}
    for s in species:
        reflist = set()
        speciesRefs[s.species()] = reflist
    # go through all citations
    for c in citeList:
        if c.actual() in speciesRefs:
            reflist = speciesRefs[c.actual()]
            reflist = reflist | {c.citeKey()}
            speciesRefs[c.actual()] = reflist
    return speciesRefs


def writeSpeciesList(speciesList):
    """ output species index HTML """
    outfile = codecs.open(speciesURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Species","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Species</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("    <p>")  
    nf = 0
    for s in speciesList:
        if s.status() == "fossil":
            nf += 1
    tstr = "      The following lists all {} of the currently recognized species of fiddler crab, as well as {} fossil species (marked with"+fossilImage+").\n"
    outfile.write(tstr.format(len(speciesList)-nf,nf))
    outfile.write("      See the <a href=\"/names\">complete name index</a> for alternate species names and spellings.\n")
    outfile.write("    </p>")  
    outfile.write("\n")  
    outfile.write("    <ul id=\"splist\">\n")
    for species in speciesList:
        outfile.write("      <li>"+createSpeciesLink(species.species(),species.status(),"")+"</li>\n")
    outfile.write("    </ul>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def writeSpeciesPhotoPage(fname,species,commonName,caption,pn,pspecies):
    """ create page for a specific photo """
    outfile = open(fname,"w")
    if ";" in pspecies:
        spname = pspecies.replace(";","_")
        ptitle = "Uca " + pspecies.replace(";"," & Uca ")
        isMulti = True
    else:
        spname = species
        ptitle = "Uca " + species
        isMulti = False
    commonHTMLHeader(outfile,ptitle+" Photo","../")
    outfile.write("    <header>\n")
    outfile.write("      <h1><em class=\"species\">"+ptitle+"</em> Photo</h1>\n")
    if not isMulti:
        if commonName != "#":
            outfile.write("      <h2>"+commonName+"</h2>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    if isMulti:
        spList = pspecies.split(";")
        for s in spList:
            outfile.write("          <li><a href=\"../u_"+s+".html\"><em class=\"species\">Uca "+s+"</em> page</a></li>\n")
    else:
        outfile.write("          <li><a href=\"../u_"+species+".html\">Species page</a></li>\n")
    outfile.write("          <li><a href=\"../"+photoURL+"\">All species photos</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <figure class=\"fullpic\">\n")
    outfile.write("      <img src=\"U_"+spname+format(pn,"0>2")+".jpg\" alt=\"Uca "+species+"\" />\n")
    outfile.write("      <figcaption>"+caption+"</figcaption>\n")
    outfile.write("    </figure>\n")
    commonHTMLFooter(outfile)            
    outfile.close()


def writeSpeciesVideoPage(fname,species,commonName,video,vn):    
    """ create page for a specific video """
    outfile = codecs.open(fname,"w","utf-8")
    if ";" in video.species():
        spname = video.species().replace(";","_")
        vtitle = "Uca " + video.species().replace(";"," & Uca ")
        isMulti = True
    else:
        spname = species
        vtitle = "Uca " + species
        isMulti = False
    commonHTMLHeader(outfile,vtitle+" Video","../")
    outfile.write("    <header>\n")
    outfile.write("      <h1><em class=\"species\">"+vtitle+"</em> Video</h1>\n")
    if not isMulti:
        outfile.write("      <h2>"+commonName+"</h2>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    if isMulti:
        spList = video.species().split(";")
        for s in spList:
            outfile.write("          <li><a href=\"../u_"+s+".html\"><em class=\"species\">Uca "+s+"</em> page</a></li>\n")
    else:
        outfile.write("          <li><a href=\"../u_"+species+".html\">Species page</a></li>\n")
    outfile.write("          <li><a href=\"../"+videoURL+"\">All species videos</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <h2>"+video.caption()+"</h2>\n")
    outfile.write("    <video width=\"352\" height=\"240\" controls>\n")
    outfile.write("      <source src=\"U_"+spname+format(vn,"0>2")+"."+video.format().lower()+"\" type=\"video/mp4\">\n")
    outfile.write("      Your browser does not support the video tag.\n")
    outfile.write("    </video>\n")
    outfile.write("    <p class=\"vidcaption\">\n")
    outfile.write("      "+video.dateLocation()+"<br />\n")
    outfile.write("      "+video.author()+"<br />\n")
    outfile.write("    </p>\n")
    outfile.write("    <dl class=\"viddetails\">\n")
    outfile.write("      <dt>Length</dt>\n")
    outfile.write("        <dd>"+video.length()+"</dd>\n")
    outfile.write("      <dt>Size</dt>\n")
    outfile.write("        <dd>"+video.size()+"</dd>\n")
    outfile.write("      <dt>Format</dt>\n")
    outfile.write("        <dd>"+video.format()+"</dd>\n")
    if video.notes() != "#":
        outfile.write("      <dt>Notes</dt>\n")
        outfile.write("        <dd>"+video.notes()+"</dd>\n")
    outfile.write("    </dl>\n")
    commonHTMLFooter(outfile)            
    outfile.close()


def writeSpeciesPage(species,references,specificNames,allNames,photos,videos,artList,spRefs,refDict):
    """ create the master page for a species """
    if species.status() == "fossil":
        isFossil = True
    else:
        isFossil = False
    outfile = codecs.open("u_"+species.species()+".html", "w", "utf-8")
    if isFossil:
        commonHTMLHeader(outfile,"Uca "+species.species()+" / Fossil","")
    else:
        commonSpeciesHTMLHeader(outfile,"Uca "+species.species()+" / "+species.common(),"",species.species())
    outfile.write("    <header>\n")
    if isFossil:
        sC = fossilImage
    else:
        sC = ""    
    outfile.write("      <h1 class=\"species\">Uca "+species.species()+sC+"</h1>\n")
    if isFossil:
        outfile.write("      <h2>Fossil</h2>\n")
    else:
        outfile.write("      <h2>"+species.common()+"</h2>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    outfile.write("          <li><a href=\"#type\">Type</a></li>\n")
    outfile.write("          <li><a href=\"#info\">Information</a></li>\n")
    outfile.write("          <li><a href=\"#pics\">Photos</a></li>\n")
    if not isFossil:
        outfile.write("          <li><a href=\"#video\">Video</a></li>\n")
        outfile.write("          <li><a href=\"#art\">Art</a></li>\n")
    outfile.write("          <li><a href=\"#refs\">References</a></li>\n")
    outfile.write("          <li><a href=\"uca_species.html\">Species List</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <section class=\"topspsection\">\n")
    outfile.write("      <h2><a name=\"type\">Type Description</a></h2>\n")
    outfile.write("      <dl>\n")
    outfile.write("        <dt><em class=\"species\">"+species.typeSpecies()+"</em></dt>\n")
    tRef = refDict[species.typeRef()]
    outfile.write("        <dd>"+tRef.formattedHTML()+"</dd>\n")
    outfile.write("      </dl>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"info\">Information</a></h2>\n")
    outfile.write("      <dl>\n")
    outfile.write("       <dt>Subgenus</dt>\n")
    outfile.write("         <dd><a href=\""+systURL+"#"+species.subgenus()+"\"><em class=\"species\">"+species.subgenus()+"</em></a></dd>\n")
    if not isFossil:
        outfile.write("       <dt>Common Names</dt>\n")
        outfile.write("         <dd>"+species.commonext()+"</dd>\n")

    # Synonyms
    synList = []
    for spName in specificNames:
        if spName.synonym() == species.species():
            varlist = spName.variations().split(";")
            for varname in varlist:
                for uName in allNames:
                    cleanName = cleanSpecificName(uName)
                    if varname == cleanName:
                        synList.append(uName)
    if len(synList) > 0:
        synList.sort(key = lambda s: s.lower())
        lList = []
        for n in synList:
            namefile = nameToFileName(n)
            lList.append("<a href=\"names/"+namefile+".html\">"+formatNameString(n)+"</a>")
        outfile.write("       <dt>Synonyms, Alternate Spellings, &amp; Name Forms</dt>\n")
        outfile.write("         <dd><em class=\"species\">"+", ".join(lList)+"</em></dd>\n")

    # Geographic Range
    outfile.write("       <dt>Geographic Range</dt>\n")
    outfile.write("         <dd>"+species.region()+": "+species.range()+"</dd>\n")
    if not isFossil:
        outfile.write("         <dd>\n")
        outfile.write("           <div id=\"map_canvas\" style=\"width: 450px; height: 350px;\"></div>\n")
        outfile.write("         </dd>\n")
        outfile.write("         <dd class=\"map_data\">\n")
        mapRefKeyList = species.rangeRefs().split(";")
        mapRefKeyList.sort(key = lambda s: s.lower())
        mapCiteList = []
        for m in mapRefKeyList:
            if m in refDict:
                mRef = refDict[m]
                mapCiteList.append("<a href=\"references/"+mRef.citeKey()+".html\">"+mRef.citation()+"</a>")
            else:
                mapCiteList.append(m)
        outfile.write("           Map data derived from: "+"; ".join(mapCiteList)+"\n")
        outfile.write("         </dd>\n")

    # External links
    outfile.write("       <dt>External Links</dt>\n")
    if species.EOLid() != ".":
        outfile.write("         <dd><a href=\"http://eol.org/pages/"+species.EOLid()+"/overview\">Encyclopedia of Life</a></dd>\n")
    outfile.write("         <dd><a href=\"http://en.wikipedia.org/wiki/Uca_"+species.species()+"\">Wikipedia</a></dd>\n")
    if species.iNatid() != ".":
        outfile.write("         <dd><a href=\"http://www.inaturalist.org/taxa/"+species.iNatid()+"\">iNaturalist</a></dd>\n")
    if species.taxonid() != ".":
        outfile.write("         <dd><a href=\"http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id="+species.taxonid()+"\">NCBI Taxonomy Browser/Genbank</a></dd>\n")
    if species.gbifid() != ".":
        outfile.write("         <dd><a href=\"http://www.gbif.org/species/"+species.gbifid()+"\">GBIF</a></dd>\n")

    outfile.write("      </dl>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"pics\">Photos</a></h2>\n")
    photoN = 0
    for photo in photos:
        slist = photo.species().split(";")
        if species.species() in slist:
            pn = int(photo.n())
            if ";" in photo.species():
                nl = photo.species().replace(";","_")
                pfname = "photos/u_"+nl+format(pn,"0>2")+".html"
                tname = nl
            else:
                pfname = "photos/u_"+species.species()+format(pn,"0>2")+".html"
                tname = species.species()
            outfile.write("      <figure class=\"sppic\">\n")
            outfile.write("        <a href=\""+pfname+"\"><img src=\"photos/U_"+tname+format(pn,"0>2")+"tn.jpg\" alt=\"Uca "+species.species()+"\" /></a>\n")
            outfile.write("      </figure>\n")
            writeSpeciesPhotoPage(pfname,species.species(),species.common(),photo.caption(),pn,photo.species())
            photoN += 1
    if photoN == 0:
        outfile.write("      <p>\n")
        outfile.write("        <em>No pictures available at this time.</em>\n")
        outfile.write("      </p>\n")

    outfile.write("\n")
    if not isFossil:
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"video\">Video</a></h2>\n")
        videoN = 0
        for video in videos:
            slist = video.species().split(";")
            if species.species() in slist:
                vn = int(video.n())
                if ";" in video.species():
                    nl = video.species().replace(";","_")
                    vfname = "video/u_"+nl+format(vn,"0>2")+".html"
                else:
                    vfname = "video/u_"+species.species()+format(vn,"0>2")+".html"
                videoN += 1
                if videoN == 1:
                    outfile.write("      <dl class=\"vidlist\">\n")
                outfile.write("            <dt><a class=\"vidlink\" href=\""+vfname+"\">"+video.caption()+"</a></dt>\n")
                outfile.write("              <dd>"+video.length()+", "+video.size()+", "+video.format()+"</dd>\n")
                writeSpeciesVideoPage(vfname,species.species(),species.common(),video,vn)
        if videoN == 0:
            outfile.write("      <p>\n")
            outfile.write("        <em>No videos available at this time.</em>\n")
            outfile.write("      </p>\n")
        else:
            outfile.write("      </dl>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")

        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\"art\">Art</a></h2>\n")
        artN = 0
        for art in artList:
            slist = art.species().split(";")
            if species.species() in slist:
                pfname = "art/"+art.image()+".html"
                outfile.write("      <figure class=\"sppic\">\n")
                outfile.write("        <a href=\""+pfname+"\"><img src=\"art/"+art.image()+"_tn."+art.ext()+"\" alt=\""+art.title()+"\" /></a>\n")
                outfile.write("      </figure>\n")
                artN += 1
        if artN == 0:
            outfile.write("      <p>\n")
            outfile.write("        <em>No art available at this time.</em>\n")
            outfile.write("      </p>\n")
        else:
            outfile.write("      </dl>\n")
        outfile.write("    </section>\n")
        outfile.write("\n")

    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"refs\">References</a></h2>\n")
    outfile.write("      <div id=\"citation\">\n")
    outfile.write("        <ul>\n")
    for i,ref in enumerate(references):
        if ref.citeKey() in spRefs:
            outfile.write(formatReference(i+1,ref))
    outfile.write("        </ul>\n")
    outfile.write("      </div>\n")    
    outfile.write("    </section>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createPhotosHTML(speciesList,photos):
    createBlankIndex("photos/index.html")
    """ create the photos index page """
    outfile = codecs.open(photoURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Photos","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Photos</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <p>\n")
    outfile.write("      Note: many photos of supposed fiddler crabs on the web are actually from other genera (ghost crabs are a common error).\n")
    outfile.write("      Lay-people often assume any crab with asymmetric claws is a fiddler crab.\n")
    outfile.write("    </p>\n")
    outfile.write("    <p>\n")
    outfile.write("      Total photo count is "+str(len(photos))+".\n")
    outfile.write("    </p>\n")
    for sp in speciesList:
        species = sp.species()
        status = sp.status()
        outfile.write("    <section class=\"photosection\">\n")
        outfile.write("      <h2>"+createSpeciesLink(species,status,"")+"</h2>\n")
        photoN = 0
        for photo in photos:
            splist = photo.species().split(";")
            if species in splist:
                pn = int(photo.n())
                if ";" in photo.species():
                    spname = photo.species().replace(";","_")
                else:
                    spname = photo.species()
                pfname = "photos/u_"+spname+format(pn,"0>2")+".html"
                outfile.write("      <figure class=\"sppic\">\n")
                outfile.write("        <a href=\""+pfname+"\"><img src=\"photos/U_"+spname+format(pn,"0>2")+"tn.jpg\" alt=\"Uca "+spname+"\" /></a>\n")
                outfile.write("      </figure>\n")
                photoN += 1
        if photoN == 0:
            outfile.write("      <p>\n")
            outfile.write("        <em>No pictures available at this time.</em>\n")
            outfile.write("      </p>\n")
        outfile.write("    </section>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createVideosHTML(videos):
    createBlankIndex("video/index.html")
    """ create the videos page """
    sectitle = ("Feeding","Male Waving and Other Displays","Female Display","Fighting","Mating","Miscellaneous")
    secshort = ("Feeding","Male Display","Female Display","Fighting","Mating","Miscellaneous")
    secanchor = ("feeding","display","female","fighting","mating","misc")    

    outfile = codecs.open(videoURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Videos","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Videos</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    for i,x in enumerate(secshort):
        outfile.write("          <li><a href=\"#"+secanchor[i]+"\">"+x+"</a></li>\n")        
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <p>\n")
    outfile.write("      Most of these videos predate digital video (let alone HD) and were recorded on Hi8 tape. "+\
                  "Hopefully they will eventually be replaced by higher quality video. "+\
                  "These are grouped by activity. Videos for specific species can be found on the "+\
                  "<a href=\""+speciesURL+"\">individual species' page</a>.\n")
    outfile.write("    </p>\n")
    outfile.write("    <p>\n")
    outfile.write("      Total video count is "+str(len(videos))+"\n")
    outfile.write("    </p>\n")
    for i,x in enumerate(sectitle):
        outfile.write("\n")
        outfile.write("    <section class=\"spsection\">\n")
        outfile.write("      <h2><a name=\""+secanchor[i]+"\">"+x+"</a></h2>\n")
        outfile.write("      <dl class=\"vidlist\">\n")
        for video in videos:
            if video.activity() == secanchor[i]:
                vn = int(video.n())
                if ";" in video.species():
                    spname = video.species().replace(";","_")
                else:
                    spname = video.species()
                vfname = "video/u_"+spname+format(vn,"0>2")+".html"
                outfile.write("            <dt><a class=\"vidlink\" href=\""+vfname+"\">"+video.caption()+"</a></dt>\n")
                outfile.write("              <dd>"+video.length()+", "+video.size()+", "+video.format()+"</dd>\n")
        outfile.write("      </dl>\n")
        outfile.write("    </section>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def writeScienceArtPage(fname,art):
    """ create the indivdual page for each piece of art """
    outfile = codecs.open(fname, "w", "utf-8")
    ptitle = art.title() + " (" + art.author() + " "+art.year()+")"
    commonHTMLHeader(outfile,ptitle,"../")
    outfile.write("    <header>\n")
    outfile.write("      <h1><em class=\"species\">"+art.title()+"</em></h1>\n")
    outfile.write("      <h2>"+art.author()+" ("+art.year()+")</h2>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    if art.species() != "n/a":
        outfile.write("          <li><a href=\"../u_"+art.species()+".html\">Species page</a></li>\n")
    if art.citeKey() != "n/a":
        outfile.write("          <li><a href=\"../references/"+art.citeKey()+".html\">Reference</a></li>\n")
    outfile.write("          <li><a href=\"../"+artURL+"\">All art</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <figure class=\"fullpic\">\n")
    outfile.write("      <img src=\""+art.image()+"."+art.ext()+"\" alt=\""+ptitle+"\" />\n")
    outfile.write("      <figcaption>"+art.notes()+"</figcaption>\n")
    outfile.write("    </figure>\n")
    commonHTMLFooter(outfile)            
    outfile.close()


def createArtHTML(artList):
    """ create the art index """
    outfile = codecs.open(artURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Art","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Art</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    outfile.write("          <li><a href=\"#science\">Scientific Drawings</a></li>\n")
    outfile.write("          <li><a href=\"#stamps\">Postage Stamps</a></li>\n")
    outfile.write("          <li><a href=\"#origami\">Origami</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")
    outfile.write("    <p>\n")
    outfile.write("      Fiddler crabs have rarely been the focus of artistic works. Furthermore, many works of art purporting to contain fiddler crabs are actually of other species (ghost crabs are a particularly common mix-up).\n")
    outfile.write("      Below are some of the more notable or interesting examples of fiddler crabs in various art forms.\n")
    outfile.write("    </p>\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"science\">Scientific Drawings</a></h2>\n")
    artSource = []
    cnt = 0
    for art in artList:
        if art.artType() == "science":
            cnt += 1
            artist = art.author() + " (" + art.year() + ")"
            try:
                artSource.index(artist)
            except:
                artSource.append(artist)
    outfile.write("      <p>\n")
    outfile.write("        Formal scientific drawings are often works of art as well as scientific illustration. These are ordered chronologically.\n")
    outfile.write("      </p>\n")
    outfile.write("      <p>\n")
    outfile.write("        Total scientific drawing count is "+str(cnt)+".\n")
    outfile.write("      </p>\n")
    createBlankIndex("art/index.html")
    for a in artSource:
        outfile.write("      <h3>"+a+"</h3>\n")
        for art in artList:
            if art.artType() == "science":
                artist = art.author() + " (" + art.year() + ")"
                if artist == a:
                    pfname = "art/"+art.image()+".html"
                    outfile.write("      <figure class=\"sppic\">\n")
                    outfile.write("        <a href=\""+pfname+"\"><img src=\"art/"+art.image()+"_tn."+art.ext()+"\" alt=\""+art.title()+"\" /></a>\n")
                    outfile.write("      </figure>\n")
                    writeScienceArtPage(pfname,art)
    outfile.write("    </section>\n")
    outfile.write("\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"stamps\">Postage Stamps</a></h2>\n")
    artSource = []
    cnt = 0
    for art in artList:
        if art.artType() == "stamp":
            cnt += 1
            try:
                artSource.index(art.author())
            except:
                artSource.append(art.author())
    outfile.write("      <p>\n")
    outfile.write("        Fiddler crabs have been featured on postage stamps surprisingly often. Quality control leaves something to be desired, however, as misidentifications are common (<em>e.g.</em>, see The Gambia and the Solomon Islands).\n")
    outfile.write("        Omori &amp; Holthuis (2000, 2005) have actually written papers about crustacea on postage stamps.\n")
    outfile.write("      </p>\n")
    outfile.write("      <p>\n")
    outfile.write("        Total fiddler crab stamps is "+str(cnt)+".\n")
    outfile.write("      </p>\n")
    for a in artSource:
        outfile.write("      <h3>"+a+"</h3>\n")
        for art in artList:
            if art.artType() == "stamp":
                if art.author() == a:
                    pfname = "art/"+art.image()+".html"
                    outfile.write("      <figure class=\"sppic\">\n")
                    outfile.write("        <a href=\""+pfname+"\"><img src=\"art/"+art.image()+"_tn."+art.ext()+"\" alt=\""+art.title()+"\" /></a>\n")
                    outfile.write("      </figure>\n")
                    writeScienceArtPage(pfname,art)
    outfile.write("    </section>\n")
    outfile.write("\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"origami\">Origami</a></h2>\n")
    artSource = []
    cnt = 0
    for art in artList:
        if art.artType() == "origami":
            cnt += 1
            try:
                artSource.index(art.author())
            except:
                artSource.append(art.author())
    outfile.write("      <p>\n")
    outfile.write("        Male fiddler crabs are a particular challenge for origami because of the asymmetry, but a number of\n")
    outfile.write("        origami experts have developed fiddler crab models.\n")
    outfile.write("      </p>\n")
    outfile.write("      <p>\n")
    outfile.write("        Total fiddler crab origami models is "+str(cnt)+".\n")
    outfile.write("      </p>\n")
    for a in artSource:
        outfile.write("      <h3>"+a+"</h3>\n")
        for art in artList:
            if art.artType() == "origami":
                if art.author() == a:
                    pfname = "art/"+art.image()+".html"
                    outfile.write("      <figure class=\"sppic\">\n")
                    outfile.write("        <a href=\""+pfname+"\"><img src=\"art/"+art.image()+"_tn."+art.ext()+"\" alt=\""+art.title()+"\" /></a>\n")
                    outfile.write("      </figure>\n")
                    writeScienceArtPage(pfname,art)
    outfile.write("    </section>\n")

    commonHTMLFooter(outfile)
    outfile.close()
    

def speciesToHTML(speciesList,references,specificNames,allNames,photos,videos,art,speciesRefs,refDict):
    """ output species list and individual species pages """
    writeSpeciesList(speciesList)
    for species in speciesList:
        """
        species = specData[0]
        specInfo = specData[1:]
        spRefs = speciesRefs[species]
        writeSpeciesPage(species,specInfo,references,specificNames,allNames,photos,videos,art,spRefs)
        """
        spRefs = speciesRefs[species.species()]
        writeSpeciesPage(species,references,specificNames,allNames,photos,videos,art,spRefs,refDict)


def createSystematicsHTML(subgenList,speciesList):
    """ create the systematics page """
    outfile = codecs.open(systURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Systematics","")
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
    outfile.write("    <div class=\"topspection\">\n")
    outfile.write("    <p>The following information is an expansion and update of that found in:</p>\n")
    outfile.write("    <blockquote>\n")
    outfile.write("      Rosenberg, M.S. 2001. The systematics and taxonomy of fiddler crabs: A\n")
    outfile.write("      phylogeny of the genus <em class=\"species\">Uca.</em> <em>Journal of Crustacean Biology</em>\n")
    outfile.write("      21(3):839-869.\n")
    outfile.write("    </blockquote>\n")
    outfile.write("    <p>Additional references for updated information will be detailed below.</p>")
    outfile.write("    </div>\n")
    outfile.write("\n")

    # genus section
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"genus\">Genus <em class=\"species\">Uca</em> Leach, 1814</a></h2>\n")
    outfile.write("      <h3>Type species: <em class=\"species\">Cancer vocans major</em> Herbst, 1782</h3>\n")
    outfile.write("      <p>\n")
    outfile.write("         The earliest description of the type species of <em class=\"species\">Uca</em> is from a drawing in\n")
    outfile.write("         <a href=\"references/Seba1758.html\">Seba (1758)</a>, which he called <em class=\"species\">Cancer uka una, Brasiliensibus</em> (shown below).\n")
    outfile.write("      </p>\n")
    outfile.write("      <figure>\n")
    outfile.write("        <img src=\"art/Seba_Uca_una.jpg\" width=\"647\" height=\"477\" alt=\"Seba's fiddler crab\" />\n")
    outfile.write("      </figure>\n")
    outfile.write("      <p>\n")
    outfile.write("        A number of authors subsequently used this same picture as a basis for naming the " + \
       "species (<a href=\"references/Manning1981.html\">Manning and Holthuis 1981</a>).  " + \
       "<em class=\"species\">Cancer vocans major</em> Herbst, 1782; " + \
       "<em class=\"species\">Ocypode heterochelos</em> Lamarck, 1801; " + \
       "<em class=\"species\">Cancer uka</em> Shaw and Nodder, 1802; and " + \
       "<em class=\"species\">Uca una</em> Leach, 1814, are " + \
       "all objective synonyms, because they are all based on the picture and " + \
       "description from Seba. Because of this, the official type specimen of the " + \
       "genus <em class=\"species\">Uca</em> is <em class=\"species\">Cancer vocans major.</em> " + \
       "The earliest description of " + \
       "this species based on actual specimens and not on Seba's drawing was <em class=\"species\">" + \
       "Gelasimus platydactylus</em> Milne-Edwards, 1837.\n")
    outfile.write("      </p>\n")
    outfile.write("      <blockquote>\n")
    outfile.write("        As an aside, Seba's name, <em class=\"species\">Cancer uka una</em> comes from the nomenclature of " + \
       "<a href=\"references/Marcgrave1648.html\">Marcgrave (1648)</a>, who mispelled &ldquo;u&ccedil;a una&rdquo; as &ldquo;uca una&rdquo;. Not only did Seba copy the " + \
       "mispelling, but he applied it to the fiddler crab instead of the mangrove crab " + \
       "(which is today called <em class=\"species\">Ucides</em>) to which Marcgrave applied the name (see below). <a href=\"references/Latreille1817.2.html\">Latreille's (1817)</a> proposal of the " + \
       "generic name <em class=\"species\">Gelasimus</em> for fiddler crabs was so that <em class=\"species\">Uca</em> " + \
       "could be applied to mangrove crabs; as this was an invalid proposal, <em class=\"species\">Uca</em> " + \
       "is retained for fiddlers, despite being due to a pair of errors (<a href=\"references/Tavares1993.html\">Tavares 1993</a>).\n")
    outfile.write("        <figure class=\"syspic\">\n")
    outfile.write("          <img src=\"art/Marcgrave_Maracoani.png\" alt=\"Marcgrave's Maracoani\">\n")
    outfile.write("          <figcaption>Oldest known drawing of a fiddler crab (<a href=\"references/Marcgrave1648.html\">Marcgrave, 1648</a>). He labeled it &ldquo;Maracoani&rdquo;, and it represents the namesake of the species <em class=\"species\">Uca maracoani.</em></figcaption>\n")
    outfile.write("        </figure>\n")
    outfile.write("        <figure class=\"syspic\">\n")
    outfile.write("          <img src=\"art/Marcgrave_Uca_una.png\" alt=\"Marcgrave's Uca una\">\n")
    outfile.write("          <figcaption>The drawing actually labeled &ldquo;Uca Una&rdquo; by <a href=\"references/Marcgrave1648.html\">Marcgrave (1648)</a> is not a fiddler crab. Today this species is known as the mangrove crab <em class=\"species\">Ucides cordatus.</em></figcaption>\n")
    outfile.write("        </figure>\n")
    outfile.write("        <figure class=\"syspic\">\n")
    outfile.write("          <img src=\"art/Marcgrave_Ciecie_Ete.png\" alt=\"Marcgrave's Ciecie Ete\">\n")
    outfile.write("          <figcaption>The other fiddler crab drawing found in <a href=\"references/Marcgrave1648.html\">Marcrgrave (1648)</a>, labeled &ldquo;Ciecie Ete&rdquo; (he also refers to a very similar species called &ldquo;Ciecie Panema&rdquo;). This figure is believed to most likely represent <em class=\"species\">Uca thayeri.</em></figcaption>\n")
    outfile.write("        </figure>\n")
    outfile.write("      </blockquote>\n")
    outfile.write("      <p>\n")
    outfile.write("        For about 60 years, the genus was known as <em class=\"species\">Gelasimus,</em> until <a href=\"references/Rathbun1897.1.html\">Rathbun " + \
       "(1897)</a> showed that the abandonment of the older name <em class=\"species\">Uca</em> did not " + \
       "conform to zoological naming conventions. The type species of <em class=\"species\">Uca</em> was " + \
       "known as both <em class=\"species\">Uca heterochelos</em> and " + \
       "<em class=\"species\">U. platydactylus,</em> until <a href=\"references/Rathbun1918.2.html\">Rathbun (1918)</a> suggested the adoption of " + \
       "<em class=\"species\">U. heterochelos</em> " + \
       "as the valid name. Almost 50 years later, <a href=\"references/Holthuis1962.html\">Holthuis (1962)</a> pointed out that <em class=\"species\">" + \
       "U. heterochelos</em> " + \
       "was an objective junior synonym of <em class=\"species\">U. major,</em> thus the type species has " + \
       "been referred to as <em class=\"species\">U. major</em> ever since.\n")
    outfile.write("      <p>\n")
    outfile.write("      <p>\n")
    outfile.write("        However, <a href=\"references/Bott1973.1.html\">Bott (1973)</a> discovered that there has been a universal " + \
       "misinterpretation of the type species; the species pictured by Seba is not the " + \
       "American species commonly referred to as " + \
       "<em class=\"species\">U. major,</em> but rather the West African/Portuguese species called " + \
       "<em class=\"species\">U. tangeri</em> " + \
       "(Eydoux, 1835). Correcting this error would have caused a somewhat painful " + \
       "change of names (<a href=\"references/Holthuis1979.html\">Holthuis 1979</a>; <a href=\"references/Manning1981.html\">Manning and Holthuis 1981</a>). The type species " + \
       "would still be called <em class=\"species\">U. major</em>, but would refer to the West " + \
       "African/European species rather than the American one; the American species, " + \
       "which has been called <em class=\"species\">U. major</em> since 1962, would be called " + \
       "<em class=\"species\">U. platydactylus,</em> a name not used since 1918.\n")
    outfile.write("      <p>\n")
    outfile.write("      <p>\n")
    outfile.write("         To deal with this dilemma, the Society of Zoological Nomenclature officially " + \
       "designated the holotype of <em class=\"species\">Gelasimus platydactylus</em> as a neotype " + \
       "of <em class=\"species\">Cancer vocans major</em> " + \
       "(<a href=\"references/Holthuis1979.html\">Holthuis 1979</a>; <a href=\"references/ICZN1983.html\">ICZN Opinion 1262</a>). The result of this decision is that we retain " + \
       "the names " + \
       "<em class=\"species\">U. major</em> for the American species and <em class=\"species\">U. tangeri</em> for the West " + \
       "African/European species. It also means that although <em class=\"species\">U. tangeri</em> is " + \
       "technically the species upon which the genus is named, <em class=\"species\">U. major</em> " + \
       "(<em class=\"species\">Cancer vocans major</em>) is still the official type species of the genus " + \
       "<em class=\"species\">Uca.</em>\n")
    outfile.write("      <p>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")

    # subgenera section
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"subgenera\">Subgenera</a></h2>\n")
    outfile.write("      <p>")
    outfile.write("       There have been two major proposals for splitting up the genus, one by <a href=\"references/Bott1973.2.html\">Bott " + \
      "(1973)</a> and the other by <a href=\"references/Crane1975.html\">Crane (1975)</a>. Neither is based on a numerical phylogeny. " + \
      "Crane's descriptions are very complete. Bott's descriptions are poor, but have " + \
      "priority. For a long time, scientists actively ignored both subdivisions and when there " + \
      "was a reference in the literature, it almost always used Crane's names " + \
      "and not Bott's. Bott also split the genus into multiple genera rather than subgenera, an unnecessary complication in most researcher's minds.\n")
    outfile.write("      </p>")
    outfile.write("      <p>")
    outfile.write("       <a href=\"references/Rosenberg2001.html\">Rosenberg (2001)</a> partly cleared up the confusion between the two systems. More recent work by " + \
        "<a href=\"references/Beinlich2006.html\">Beinlich &amp; von Hagen (2006)</a>, <a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009), <a href=\"references/Spivak2009.html\">Spivak &amp; Cuesta (2009)</a>, <a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> (2010)</a>, and " + \
        "<a href=\"references/Landstorfer2010.html\">Landstorfer &amp; Schbart (2010)</a> has continued to refine the subgenera as detailed below.\n")
    outfile.write("      </p>")
    outfile.write("      <ul>\n")
    for subgen in subgenList:
        outfile.write("        <li><a href=\"#"+subgen.subgenus()+"\">Subgenus <em class=\"species\">"+subgen.subgenus()+"</em></a></li>\n")
    outfile.write("      </ul>\n")
 
    for subgen in subgenList:
        outfile.write("      <hr />")
        outfile.write("      <h3>Subgenus <a name=\""+subgen.subgenus()+"\"><em class=\"species\">"+subgen.subgenus()+"</em> "+subgen.author()+"</a></h3>\n")
        outfile.write("      <dl>\n")
        outfile.write("        <dt>Type</dt>\n")
        outfile.write("        <dd>"+createSpeciesLink(subgen.typeSpecies(),"","")+"</dd>\n")
        outfile.write("        <dt>All Species</dt>\n")
        spList = []
        for s in speciesList:
            if s.subgenus() == subgen.subgenus():
                spList.append(createSpeciesLink(s.species(),s.status(),""))
        outfile.write("        <dd>"+", ".join(spList)+"</dd>\n")    
        outfile.write("      </dl>\n")
        outfile.write("      <p>\n")
        outfile.write("      "+subgen.notes()+"\n")
        outfile.write("      </p>\n")
        outfile.write("\n")

    outfile.write("    </section>\n")
    outfile.write("\n")

    # species section
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2><a name=\"species\">Species Level Systematics</a></h2>\n")
    outfile.write("      <ul>\n")
    outfile.write("        <li><a href=\""+speciesURL+"\">Currently recognized species</a></li>\n")
    outfile.write("      </ul>\n")
    outfile.write("      <p>\n")
    outfile.write("For an overview of all <em class=\"species\">Uca</em> species, the best reference is <a href=\"references/Crane1975.html\">Crane (1975)</a>; " + \
        "any earlier major work would be overridden by Crane's descriptions. For the most " + \
        "part, the taxa recognized by Crane are still accepted today. A number of new " + \
        "species have been described since the publication of her monograph, a few " + \
        "species has been discovered to be invalid, and two of her new species were " + \
        "previously described by <a href=\"references/Bott1973.2.html\">Bott (1973)</a>; as with the subgenera, his names have " + \
        "priority and take precedence. These changes are summarized below.\n")
    outfile.write("      </p>\n")
    outfile.write("      <h3>Changes to the species level taxonomy of the genus <em class=\"species\">Uca</em> since Crane (1975)</h3>\n")  
    outfile.write("      <table>\n")
    outfile.write("        <thead>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <th>New/Validated Extant Species</th><th>Reference(s)</th>\n")
    outfile.write("          </tr>\n")
    outfile.write("        </thead>\n")
    outfile.write("        <tfoot>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <td colspan=\"2\"><strong>Note:</strong> The newly described (relative to Crane) species \n")
    outfile.write("             <em class=\"species\">Uca pavo</em> George &amp; Jones (1982), is a junior subsynonym of \n")
    outfile.write("             <em class=\"species\">Uca capricornis</em> (see <a href=\"references/vonHagen1989.html\">von Hagen &amp; Jones 1989</a>)</td>\n")
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
    outfile.write("            <td><a href=\"references/Kossmann1877.html\">Kossmann (1877)</a>, <a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009)</a>, <a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> (2010)</a></td>\n")
    outfile.write("          </tr>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <td><em class=\"species\">Uca iranica</em></td>\n")
    outfile.write("            <td><a href=\"references/Pretzmann1971.html\">Pretzmann (1971)</a>, <a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009)</a>, <a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> (2010)</a></td>\n")
    outfile.write("          </tr>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <td><em class=\"species\">Uca cryptica</em></td>\n")
    outfile.write("            <td><a href=\"references/Naderloo2010.html\">Naderloo <em>et al.</em> (2010)</a></td>\n")
    outfile.write("          </tr>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <td><em class=\"species\">Uca osa</em></td>\n")
    outfile.write("            <td><a href=\"references/Landstorfer2010.html\">Landstorfer &amp; Schubart (2010)</a></td>\n")
    outfile.write("          </tr>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <td><em class=\"species\">Uca jocelynae</em></td>\n")
    outfile.write("            <td><a href=\"references/Shih2010.1.html\">Shih <em>et al.</em> (2010</a>)</td>\n")
    outfile.write("          </tr>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <td><em class=\"species\">Uca splendida</em></td>\n")
    outfile.write("            <td><a href=\"references/Stimpson1858.html\">Stimpson (1858)</a>, <a href=\"references/Shih2012.html\">Shih <em>et al.</em> (2012)</a></td>\n")
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
    outfile.write("            <td colspan=\"3\"><strong>Note:</strong> <em class=\"species\">Uca australiae</em> is\n")
    outfile.write("            probably not a valid species; it is based on a single specimen found washed up on the Australian shore \n")
    outfile.write("            (<a href=\"references/George1982.html\">George &amp; Jones 1982</a>, among others)</td>\n")
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
    outfile.write("            <td><a href=\"references/Dai1991.html\">Dai &amp; Yang (1991)</a>; <a href=\"references/Jones1994.html\">Jones &amp; Morton (1994)</a></td>\n")
    outfile.write("          </tr>\n")
    outfile.write("          <tr>\n")
    outfile.write("            <td><em class=\"species\">Uca pacificensis</em></td>\n")
    outfile.write("            <td><em class=\"species\">Uca neocultrimana</em></td>\n")
    outfile.write("            <td><a href=\"references/Rosenberg2001.html\">Rosenberg (2001)</td>\n")
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
    outfile.write("<a href=\"references/Crane1975.html\">Crane (1975)</a> tended to lump related taxa into subspecies rather than treat them " + \
       "as distinct species. A number of studies since that time have raised virtually " + \
       "all of her subspecies to specific status (<em>e.g.,</em> <a href=\"references/Barnwell1980.html\">Barnwell 1980</a>; " + \
       "<a href=\"references/Barnwell1984.1.html\">Barnwell and Thurman 1984</a>; <a href=\"references/Collins1984.html\">Collins <em>et al.</em> 1984</a>; <a href=\"references/Green1980.html\">Green 1980</a>; <a href=\"references/Salmon1979.2.html\">Salmon <em> " + \
       "et al.</em> 1979</a>; <a href=\"references/Salmon1987.2.html\">Salmon and Kettler 1987</a>; <a href=\"references/Thurman1979.html\">Thurman 1979</a>, <a href=\"references/Thurman1982.html\">Thurman 1982</a>; <a href=\"references/vonHagen1989.html\">von Hagen and " + \
       "Jones 1989)</a>. It has become common practice with many authors to ignore all of " + \
       "the subspecific designations and treat each as a separate species (<em>e.g.,</em> " + \
       "<a href=\"references/George1982.html\">George and Jones 1982</a>; <a href=\"references/Jones1994.html\">Jones and Morton 1994</a>; <a href=\"references/vonHagen1989.html\">von Hagen and Jones 1989</a>). I " + \
       "follow this practice throughout this website.\n")
    outfile.write("      </p>\n")
    outfile.write("    </section>\n")
    commonHTMLFooter(outfile)


def summarizeYear(yearDict):
    minY = 2014
    maxY = 0
    for y in yearDict:
        if y < minY:
            minY = y
        elif y > maxY:
            maxY = y
    dataList = []
    c = 0
    # year, total pubs, cumulative pubs, pubs with cite info
    for y in range(minY,maxY+1):
        if y in yearDict:
            c = c + yearDict[y][0]
            dataList.append([y,yearDict[y][0],c,yearDict[y][1]])
        else:
            dataList.append([y,0,c,0])

    dataList1900 = []
    for y in range(1900,maxY+1):
        if y in yearDict:
            dataList1900.append([y,yearDict[y][0],yearDict[y][1]])
        else:
            dataList1900.append([y,0,0])
    return dataList, dataList1900


def createLifeCycle():
    """ create the life cycle page """
    outfile = codecs.open(lifeCycleURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Life Cycle","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Life Cycle</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("    <p>\n")
    outfile.write("      Following is a rough outline of the stages of the life of a fiddler crab. "+\
                  "The photographs are from a mix of species.\n")
    outfile.write("    </p>\n")
    outfile.write("\n")  
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2>Egg</h2>\n")
    outfile.write("      <p>\n")
    outfile.write("      Fertilized female fiddler crabs carry hundreds to thousands of eggs under their abdomen. "+\
                  "These are sometimes known as &ldquo;sponge&rdquo; crabs.\n")
    outfile.write("      </p>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_rapax10.html\"><img src=\"photos/U_rapax10tn.jpg\" alt=\"Gravid female\" /></a>\n")
    outfile.write("        <figcaption>Gravid female</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_rapax11.html\"><img src=\"photos/U_rapax11tn.jpg\" alt=\"Gravid female\" /></a>\n")
    outfile.write("        <figcaption>Close up of eggs</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")  
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2>Zoea</h2>\n")
    outfile.write("      <p>\n")
    outfile.write("        When the eggs are ready, the mother goes into the water and allows the eggs to hatch into microscopic "+\
                  "free-swimming larvae. The early stage larvae are known as zoea.\n")
    outfile.write("      </p>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_ecuadoriensis07.html\"><img src=\"photos/U_ecuadoriensis07tn.jpg\" alt=\"zoea\" /></a>\n")
    outfile.write("        <figcaption>Zoea</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_ecuadoriensis08.html\"><img src=\"photos/U_ecuadoriensis08tn.jpg\" alt=\"zoea\" /></a>\n")
    outfile.write("        <figcaption>Zoea</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")  
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("    <h2>Megalopa</h2>\n")
    outfile.write("      <p>\n")
    outfile.write("        The larvae live in the open water as part of the plankton. "+\
                  "As they grow and go through a number of molt stages. Older larvae are known as megalopa.\n")
    outfile.write("      </p>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_ecuadoriensis09.html\"><img src=\"photos/U_ecuadoriensis09tn.jpg\" alt=\"megalopa\" /></a>\n")
    outfile.write("        <figcaption>Megalopa</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")  
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("    <h2>Crab</h2>\n")
    outfile.write("      <p>\n")
    outfile.write("        At the end of the final larval stage, the larvae molt into immature crabs. "+\
                  "The amount of time spent as a swimming larvae (hatching to true crab stage) varies among species, but ranges from a few weeks to a few months.\n")
    outfile.write("      </p>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_ecuadoriensis10.html\"><img src=\"photos/U_ecuadoriensis10tn.jpg\" alt=\"early stage crab\" /></a>\n")
    outfile.write("        <figcaption>Early Stage Full Crab</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("      <p style=\"clear: both\">\n")
    outfile.write("        The crabs return to land and begin to grow; juvenile male and female crabs look alike.\n")
    outfile.write("      </p>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_pugilator21.html\"><img src=\"photos/U_pugilator21tn.jpg\" alt=\"juveniles\" /></a>\n")
    outfile.write("        <figcaption>Juvenile Crabs</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("      <p style=\"clear: both\">\n")
    outfile.write("        As they grown larger and turn into adults, the secondary-sexual characteristics (e.g., the asymmetric claws) begin to develop. "+\
                  "Adult crabs mate and the cycle starts over.\n")
    outfile.write("      </p>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_tangeri10.html\"><img src=\"photos/U_tangeri10tn.jpg\" alt=\"adult female\" /></a>\n")
    outfile.write("        <figcaption>Adult Female</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("      <figure class=\"sppic\">\n")
    outfile.write("        <a href=\"photos\\u_tangeri12.html\"><img src=\"photos/U_tangeri12tn.jpg\" alt=\"adult male\" /></a>\n")
    outfile.write("        <figcaption>Adult Male</figcaption>")
    outfile.write("      </figure>\n")
    outfile.write("    </section>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createPhylogeny():
    """ create the phylogeny page """
    outfile = codecs.open(treeURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Phylogeny","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Phylogeny</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("    <p>\n")
    outfile.write("     The phylogeny of fiddler crabs is still largely unresolved. Two trees are shown below: one "+\
                  "just the subgenera and one including all species. These are both rough, conservative estimates "+\
                  "based on combining information from <a href=\"references/Levinton1996.html\">Levinton <em>et al.</em> (1996)</a>, <a href=\"references/Sturmbauer1996.html\">Sturmbauer <em>et al.</em> (1996)</a>, <a href=\"references/Rosenberg2001.html\">Rosenberg (2001)</a>, "+\
                  "<a href=\"references/Shih2009.html\">Shih <em>et al.</em> (2009)</a>, <a href=\"references/Shih2010.1.html\">Shih <em>et al.</em> (2010)</a>, <a href=\"references/Shih2012.html\">Shih <em>et al.</em> (2012)</a>, <a href=\"references/Shih2013.html\">Shih <em>et al.</em> (2013a)</a>, <a href=\"references/Shih2013.2.html\">Shih <em>et al.</em> (2013b)</a>, and <a href=\"references/Landstorfer2010.html\">Landstorfer &amp; Schubart (2010)</a>.\n")
    outfile.write("    </p>\n")
    outfile.write("\n")  
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2>Subgenera Phylogeny</h2>\n")
    outfile.write("      <object width=\"600px\" height=\"300px\" data=\"images/tree_subgenera.svg\" type=\"image/svg+xml\"></object>\n")
    outfile.write("    </section>\n")
    outfile.write("    <section class=\"spsection\">\n")
    outfile.write("      <h2>Species Phylogeny</h2>\n")
    outfile.write("      <object width=\"600px\" height=\"2500px\" data=\"images/tree_species.svg\" type=\"image/svg+xml\"></object>\n")
    outfile.write("    </section>\n")
    outfile.write("\n")  
    commonHTMLFooter(outfile)
    outfile.close()


def morphLink(parent,character):
    if parent == ".":
        return character.replace(" ","_")
    else:
        return parent.replace(" ","_")+"_"+character.replace(" ","_")


def findMorphParent(p,mList):
    x = ""
    for m in mList:
        if p == m.character():
            x = morphLink(m.parent(),m.character())
    return x


def createMorphPage(morph,morphList):
    """ create individual pages for morphology descriptions """
    outfile = codecs.open("morphology/"+morphLink(morph.parent(),morph.character())+".html", "w", "utf-8")
    if morph.parent() == ".":
        p = ""
    else:
        p = " ("+morph.parent()+")"
    commonHTMLHeader(outfile,"Fiddler Crab Morphology: " + morph.character() + p,"../")
    outfile.write("    <header>\n")
    outfile.write("      <h1>"+morph.character()+"</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    if morph.parent() != ".":
        outfile.write("          <li><a href=\""+findMorphParent(morph.parent(),morphList)+".html\">"+morph.parent()+"</a></li>\n")
    outfile.write("          <li><a href=\"../"+morphURL+"\">General Morphology</a></li>\n")
    outfile.write("          <li><a href=\".\">Morphology Index</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("    <div class=\"morphdesc\">\n")
    outfile.write("     <p>\n")
    outfile.write("       " + morph.description() + "\n")
    outfile.write("     </p>\n")
    c = 0
    for m in morphList:
        if m.parent() == morph.character():
            c += 1
    if c > 0:
        outfile.write("     <h2>More Detail</h2>\n")
        outfile.write("     <ul>\n")
        for m in morphList:
            if m.parent() == morph.character():
                outfile.write("       <li><a href=\""+morphLink(m.parent(),m.character())+".html\">"+m.character()+"</a></li>\n")
        outfile.write("     </ul>\n")
    outfile.write("    </div>\n")
    if "|" in morph.image():
        plist = morph.image().split("|")
        clist = morph.caption().split("|")
    else:
        plist = [morph.image()]
        clist = [morph.caption()]
    for i in range(len(plist)):
        outfile.write("    <figure class=\"morphimg\">\n")
        outfile.write("      <img src=\""+plist[i]+"\" alt=\""+clist[i]+"\" />\n")
        outfile.write("      <figcaption>"+clist[i]+"</figcaption>\n")
        outfile.write("    </figure>\n")

    commonHTMLFooter(outfile)
    outfile.close()


def createMorphIndex(morphList):
    """ create index for morphology pages """
    outfile = codecs.open("morphology/index.html", "w", "utf-8")
    commonHTMLHeader(outfile,"Morphology Index","../")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Morphology Index</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    outfile.write("          <li><a href=\"../"+morphURL+"\">General Morphology</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("     <ul>\n")
    uniqueList = {}
    for m in morphList:
        if m.character() in uniqueList:
            uniqueList[m.character()] += 1
        else:
            uniqueList[m.character()] = 1

    sortList = []
    for m in morphList:
        if uniqueList[m.character()] > 1:
            sortList.append([m.character() + " (" + m.parent() + ")",m])
        else:
            sortList.append([m.character(),m])
    sortList.sort()
    for s in sortList:
        m = s[1]
        if uniqueList[m.character()] > 1:
            p = " ("+m.parent()+")"
        else:
            p = ""
        outfile.write("      <li><a href=\""+morphLink(m.parent(),m.character())+".html\">"+m.character()+ p +"</a></li>\n")
    outfile.write("     </ul>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createMorphologyPages(morphology):
    """ create page for general morphology descriptions """
    outfile = codecs.open(morphURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Morphology","../")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Morphology</h1>\n")
    outfile.write("      <nav>\n")
    outfile.write("        <ul>\n")
    outfile.write("          <li><a href=\"morphology/index.html\">Index</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </nav>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("    <div class=\"morphdesc\">\n")
    outfile.write("     <p>\n")
    outfile.write("      Fiddler crabs are decapod &ldquo;true crabs&rdquo; which much of the standard morphology found within this group. The following\n")
    outfile.write("      sections briefly describe major morphological features as well as characteristics that are often used to distinguish among species.\n")
    outfile.write("     </p>\n")
    outfile.write("      The morphology is organized hierarchically by major body component with further details within each section.\n")
    outfile.write("     <p>\n")
    outfile.write("     </p>\n")
    outfile.write("     <h2>More Detail</h2>\n")
    outfile.write("     <ul>\n")
    for m in morphology:
        if m.parent() == ".":
            outfile.write("      <li><a href=\"morphology/"+morphLink(m.parent(),m.character())+".html\">"+m.character()+"</a></li>\n")
        createMorphPage(m,morphology)
    createMorphIndex(morphology)
    outfile.write("     </ul>\n")
    outfile.write("    </div>\n")

    # max height = 335
    
    outfile.write("    <figure class=\"morphimg\">\n")
    outfile.write("      <img src=\"morphology/dorsal_view.png\" alt=\"dorsal view of crab\" />\n")
    outfile.write("      <figcaption>Figure modified from Crane (1975).</figcaption>\n")
    outfile.write("    </figure>\n")
    outfile.write("    <figure class=\"morphimg\">\n")
    outfile.write("      <img src=\"morphology/ventral_view.png\" alt=\"ventral view of crab\" />\n")
    outfile.write("      <figcaption>Figure modified from Crane (1975).</figcaption>\n")
    outfile.write("    </figure>\n")
    outfile.write("    <figure class=\"morphimg\">\n")
    outfile.write("      <img src=\"morphology/anterior_view.png\" alt=\"anterior view of crab\" />\n")
    outfile.write("      <figcaption>Figure modified from Crane (1975).</figcaption>\n")
    outfile.write("    </figure>\n")

    commonHTMLFooter(outfile)
    outfile.close()


def createCitationPage(refDict):
    """ create page with site citation info """
    outfile = codecs.open(citeURL, "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crab Website Citation","")
    outfile.write("    <header>\n")
    outfile.write("      <h1>Citation Info</h1>\n")
    outfile.write("    </header>\n")
    outfile.write("\n")  
    outfile.write("    <p>\n")
    outfile.write("      Generally it is best to cite the primary literature, whenever possible. However, the following paper " + \
                  "desribes much of the data that is unique to this website:\n")
    outfile.write("    </p>\n")
    outfile.write("    <div id=\"citation\">\n")
    outfile.write("      <ul>\n")
    ref = refDict["Rosenberg2014"] # citation describing the database
    outfile.write("        <li><a href=\"references/Rosenberg2014.html\">" + ref.formattedHTML() + "</a></li>\n")
    outfile.write("      </ul>\n")
    outfile.write("    </div>\n")
    outfile.write("    <ul>\n")
    outfile.write("      <li><a href=\"http://dx.plos.org/10.1371/journal.pone.0101704\">Read paper online at PLoS ONE</a></li>\n")
    outfile.write("      <li><a href=\"https://github.com/msrosenberg/fiddlercrab.info\">Website data repository on Github</a></li>\n")
    outfile.write("    </ul>\n")
    commonHTMLFooter(outfile)
    outfile.close()


def createIndex(species,refs):
    """ create the site index """
    outfile = codecs.open("index.html", "w", "utf-8")
    commonHTMLHeader(outfile,"Fiddler Crabs (Genus Uca)","")
    outfile.write("    <p>\n")
    scnt = 0
    for s in species:
        if s.status() != "fossil":
            scnt += 1
    outfile.write("      Fiddler crabs are small, semi-terrestrial crabs of the genus <em class=\"species\">Uca</em> " + \
       "that are characterized by extreme cheliped asymmetry in males.  They are " + \
       "most closely related to the <em class=\"species\">Ocypode</em> (ghost crabs). " + \
       "<a href=\""+speciesURL+"\">There are currently {} recognized extant species</a>.\n".format(scnt))

    outfile.write("    </p>\n")
    outfile.write("    <div>\n")
    outfile.write("      <img src=\"photos/U_mjoebergi04tn.jpg\" />\n")
    outfile.write("      <img src=\"photos/U_minax07tn.jpg\" />\n")
    outfile.write("      <img src=\"photos/U_crassipes19tn.jpg\" />\n")
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
    outfile.write("      The common English name &ldquo;Fiddler Crab&rdquo; comes from the feeding of the " + \
       "males, where the movement of the small claw from the ground to its mouth " + \
       "resembles the motion of a someone moving a bow across a fiddle (the large claw).\n")
    outfile.write("    </p>\n")
    outfile.write("    <h2>Information</h2>\n")  
    outfile.write("    <ul>\n")
    outfile.write("      <li><a href=\""+systURL+"\">Systematics</a></li>\n")
    outfile.write("      <li><a href=\""+treeURL+"\">Phylogeny</a></li>\n")
    outfile.write("      <li><a href=\""+speciesURL+"\">Species</a>\n")
    outfile.write("        <ul>\n")
    outfile.write("           <li><a href=\"names\">Name Index</a></li>\n")
    outfile.write("        </ul>\n")
    outfile.write("      </li>\n")
    outfile.write("      <li><a href=\""+commonURL+"\">Common Names</a></li>\n")
    outfile.write("      <li><a href=\""+mapURL+"\">Geographic Ranges</a></li>\n")
    outfile.write("      <li><a href=\""+lifeCycleURL+"\">Life Cycle</a></li>\n")
    outfile.write("      <li><a href=\""+morphURL+"\">Morphology</a></li>\n")
    outfile.write("      <li><a href=\""+refURL+"\">Comprehensive Reference List</a></li>\n")
    outfile.write("    </ul>\n")
    outfile.write("    <h2>Multimedia</h2>\n")  
    outfile.write("    <ul>\n")
    outfile.write("      <li><a href=\""+photoURL+"\">Photos</a></li>\n")
    outfile.write("      <li><a href=\""+videoURL+"\">Videos</a></li>\n")
    outfile.write("      <li><a href=\""+artURL+"\">Art</a></li>\n")
    outfile.write("    </ul>\n")
    outfile.write("    <h2>Miscellania</h2>\n")  
    outfile.write("    <ul>\n")
    outfile.write("      <li><a href=\""+citeURL+"\">Citation info for this website</a></li>\n")
    outfile.write("      <li><a href=\"https://github.com/msrosenberg/fiddlercrab.info\">Website data on Github</a></li>\n")
    outfile.write("    </ul>\n")

    commonHTMLFooter(outfile)
    outfile.close()


def main():
    references,refDict,citeList,yearDict = getReferences()
    yearDat, yearDat1900 = summarizeYear(yearDict)
    referencesToHTML(references,yearDat,yearDat1900)
    referencePages(references,refDict,citeList)
    specificNames = getSpecificNames()
    allNames = binomialNamePages(refDict,citeList,specificNames)
    specificNamePages(citeList,specificNames)
    species = getSpecies()
    photos = getPhotos()
    videos = getVideos()
    art = getArt()
    speciesRefs = connectRefsToSpecies(species,citeList)
    speciesToHTML(species,references,specificNames,allNames,photos,videos,art,speciesRefs,refDict)
    subgenera = getSubgenera()
    createSystematicsHTML(subgenera,species)
    createCommonNamesHTML(refDict)
    createPhotosHTML(species,photos)
    createArtHTML(art)
    createVideosHTML(videos)
    createMapHTML(species)
    createLifeCycle()
    createPhylogeny()
    morphology = getMorphology()
    createMorphologyPages(morphology)    
    createIndex(species,references)
    createCitationPage(refDict)

    # tmp
    outfile = open("year.txt","w")
    for x in yearDat:
        outfile.write(str(x[0])+"\t"+str(x[1])+"\t"+str(x[2])+"\n")
    outfile.close()
    
    print("done")

main()
