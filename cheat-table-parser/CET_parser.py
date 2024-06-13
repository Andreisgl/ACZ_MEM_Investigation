import xml.etree.ElementTree as ET

def parse_cheat_table(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    def parse_entries(entries, parent=None):
        parsed_entries = []
        for entry in entries:
            entry_info = {
                "ID": entry.findtext("ID"),
                "Description": entry.findtext("Description"),
                "GroupHeader": entry.findtext("GroupHeader"),
                "ShowAsHex": entry.findtext("ShowAsHex"),
                "ShowAsSigned": entry.findtext("ShowAsSigned"),
                "VariableType": entry.findtext("VariableType"),
                "Address": entry.findtext("Address"),
                "Parent": parent,
                "Children": []
            }
            nested_entries = entry.find("CheatEntries")
            if nested_entries is not None:
                entry_info["Children"] = parse_entries(nested_entries.findall("CheatEntry"), entry_info["Description"])
            
            parsed_entries.append(entry_info)

        return parsed_entries

    root_entries = root.find("CheatEntries").findall("CheatEntry")
    cheat_entries = parse_entries(root_entries)

    return cheat_entries

# Example usage
file_path = 'MEM INVESTIGATION - Copia (2).txt'
entries = parse_cheat_table(file_path)

# Function to print the hierarchy of parsed entries
def print_entries(entries, level=0):
    indent = "  " * level
    for entry in entries:
        print(f"{indent}Description: {entry['Description']}, Address: {entry['Address']}, Parent: {entry['Parent']}")
        if entry["Children"]:
            print_entries(entry["Children"], level + 1)

# Print the parsed entries with hierarchy
print_entries(entries)



pass