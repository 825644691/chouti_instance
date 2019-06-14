from xml import etree
from lxml.html import parse

data = parse("xmlTest")
print(data)
text = data.xpath("//food/name/text()")
print(text)


