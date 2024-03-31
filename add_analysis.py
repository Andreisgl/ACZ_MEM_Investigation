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

workset = workset[:-2]

# Identify single entries
def get_entry_rec(data): # This function is recursive
    output_list = []
    skip_to_next = False

    for index, line in enumerate(data):
        output_list.append(line)
    
    

    return output_list # Return this entry's data

            

aux = get_entry_rec(workset)

pass