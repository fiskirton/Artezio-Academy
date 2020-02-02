"""
This is a module for
working with xml documents
"""

import xml.etree.ElementTree as et
import json


def parse_xml(xml_str):
    """
    This function parsesxml document.
    Returns the hierarchy of the document
    in json format and the maximum level
    of nesting of elements.
    """

    tree = et.fromstring(xml_str)
    xml_dict = {'name': tree.tag, 'children': []}

    def dive(root, children):
        # DFS algorithm for filling the tree
        # and finding the most nesting
        if list(root):
            max_depth = 0
            for child in root:
                new_node = {'name': child.tag, 'children': []}
                depth = dive(child, new_node['children'])
                max_depth = max(depth, max_depth)
                children.append(new_node)
            return 1 + max_depth
        return 0

    depth = dive(tree, xml_dict['children'])
    tree_json = json.dumps(xml_dict, indent=4)

    return tree_json, depth


# XML = """
# <root>
#     <element1 />
#     <element2 />
#     <element3>
#             <element4>
#                 <element6>
#                     <element9 />
#                 </element6>
#             </element4
#             ><element5>
#                 <element7 />
#             </element5>
#     </element3>
# </root>
# """

# RES = parse_xml(XML)
# print(*RES)
