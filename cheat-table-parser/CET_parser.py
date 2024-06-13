import xml.etree.ElementTree as ET

def parse_cheat_table(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    cheat_entries = []

    def parse_entries(entries, parent_description=""):
        for entry in entries:
            entry_info = {
                "ID": entry.findtext("ID"),
                "Description": entry.findtext("Description"),
                "GroupHeader": entry.findtext("GroupHeader"),
                "ShowAsHex": entry.findtext("ShowAsHex"),
                "ShowAsSigned": entry.findtext("ShowAsSigned"),
                "VariableType": entry.findtext("VariableType"),
                "Address": entry.findtext("Address"),
                "ParentDescription": parent_description
            }
            cheat_entries.append(entry_info)

            nested_entries = entry.find("CheatEntries")
            if nested_entries is not None:
                parse_entries(nested_entries.findall("CheatEntry"), entry_info["Description"])

    parse_entries(root.find("CheatEntries").findall("CheatEntry"))

    return cheat_entries

# Example usage
file_path = 'MEM INVESTIGATION - Copia (2).txt'
entries = parse_cheat_table(file_path)

# Print the parsed entries
for entry in entries:
    print(entry)

pass