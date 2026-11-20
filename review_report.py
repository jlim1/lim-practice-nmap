from pathlib import Path
import xml.etree.ElementTree as ET

# A port appears in the inventory only when the saved report marks it open.
report = ET.parse(Path(__file__).with_name("sample.xml"))
for host in report.findall("host"):
    address = host.find("address").attrib["addr"]
    for port in host.findall("ports/port"):
        if port.find("state").get("state") == "open":
            print(
                address,
                port.get("protocol"),
                port.get("portid"),
                port.find("service").get("name"),
            )
