import json
import ndjson
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
        levels = []
        for i_d1, d1 in enumerate(doc.xpath("text/body/div")):
            levels.append(str(i_d1 + 1))
            for i_d2, d2 in enumerate(d1.xpath("div")):
                levels.append(f"{i_d1+1}.{i_d2+1}")
        DATA[file_info.filename] = levels
    except lxml.etree.XMLSyntaxError:
        ISSUES.append(file_info.filename)

open("dbnl.ndjson", "w").write(ndjson.dumps(DATA.items()))
