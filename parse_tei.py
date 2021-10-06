import zipfile
import lxml, lxml.etree
from rich.progress import track

z = zipfile.ZipFile("xml_pd.zip")
parser = lxml.etree.XMLParser(resolve_entities=False)

DATA = {}
ISSUES = []
for file_info in track(z.infolist()):
    file_contents = z.read(file_info)
    try:
        doc = lxml.etree.fromstring(file_contents, parser)
        divs = doc.xpath(".//div")
        div_chapters = doc.xpath(".//div[@type='chapter']")
        div_sections = doc.xpath(".//div[@type='section']")
        DATA[file_info.filename] = (
            doc,
            len(divs),
            len(div_chapters),
            len(div_sections),
        )
    except lxml.etree.XMLSyntaxError:
        ISSUES.append(file_info.filename)
