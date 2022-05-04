

f = open("genome.txt", "r")
dna_data=f.read().replace("\n","")
f.close() 


list_start=input().split()
list_end=input().split()


    
def compare_head( str, search_str):
    
    if str[:len(search_str)] == search_str : 
        return True
    else :
        return False



def check_list( str, list_word): 
    for i in range(len(list_word)) :
        if  compare_head(str, list_word[i] ) == True :
            #print( "str=%s, word=%s" %(str[:10], list_word[i])) 
            return i
    return -1



flag_dna=False
list_dna=[]


for i in range(len(dna_data)):
    start_idx = check_list( dna_data[i:], list_start )
    end_idx = check_list( dna_data[i:], list_end )
    if start_idx >= 0:
        flag_dna=True
        dna_idx=i
        
    elif end_idx >= 0 and  flag_dna == True and  dna_idx + len( list_start[start_idx] )   <=  i :
        list_dna.append(dna_data[dna_idx:i+len(list_end[end_idx])])
        flag_dna=False

print( list_dna )
print( len(list_dna) )





