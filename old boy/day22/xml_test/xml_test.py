import xml.etree.ElementTree as ET


tree = ET.parse("xmlTest")

root = tree.getroot()

print(root.tag)

# #遍历xml文档      (修改)
# for child in root:
#
#     for i in child.findall('name'):
#         print(i.tag,i.text)
#         i.text = "liangxiaoli"
#
# tree.write("xmltest.xml")

# #只遍历year节点
# for node in root.iter("year"):
#
#     print(node.tag,node.text)

#remove

for child in root:
     for i in child.findall('name'):
          child.remove(i)

tree.write('xmlTest')



