import os

file_name = 'MEM INVESTIGATION - Copia.txt'
#path = os.path.join('.', file_name)
path = file_name


with open(path, 'r') as file:
    data = file.read()


data_lines = data.splitlines()

# Identify and extract address entries and their data
workset = data_lines
#entries =  data_lines[2:] # Remove first two lines
ind_char = ' ' # Indentation char to remove when checking flags

all_entries_start_flag = '<CheatEntries>'
all_entries_end_flag = '</CheatEntries>'

entry_start_flag = '<CheatEntry>'
entry_end_flag = '</CheatEntry>'

#id_s_flag = '<ID>'
#id_e_flag = '</ID>'

# Trim data to where lines start
for index, line in enumerate(workset): 
    if line.strip(ind_char) == all_entries_start_flag:
        workset = workset[index:]
        break

# Identify single entries
def get_entry_rec(data): # This function is recursive
    output_list = []
    skip_to_next = False

    for index, line in enumerate(data):
        if (line.strip(' ') == all_entries_start_flag
            or line.strip(' ') == entry_start_flag): # A new level starts

            child = get_entry_rec(data[index+1:])
            output_list.append(child)
            skip_to_next = True
        elif (line.strip(' ') == all_entries_end_flag
            or line.strip(' ') == entry_end_flag): # The new level ends
            
            skip_to_next = False
            return output_list
        
        if skip_to_next:
            continue

        output_list.append(line)
    
    return output_list # Return this entry's data

            

aux = get_entry_rec(workset)

pass