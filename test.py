def convert(list_touple):
    list1,list1_clean=[],[]
    list_touple_str=str(sorted(list_touple)).replace('[','').replace(']','').replace('(','').replace(')','').replace(' ','').split(',')
    for i in range(len(list_touple_str)):   #提出每个元组第一个元素
        if i%2==0:
            list1.append(list_touple_str[i])
    i=''
    [list1_clean.append(i) for i in list1 if i not in list1_clean]
    dict1={}
    print(list1_clean)
    for list1_iter in list1_clean:
        for touple_iter in list_touple :
            if str(touple_iter[0])==list1_iter:
                dict1.setdefault(list1_iter,[]).append(touple_iter)
    return(list1_clean,dict1)
b=[(12,12),(13,13),(13, 14), (39, 40), (39,39),(40,40),(15, 17)]
(parent_node,node_set)=convert(b)
#print(node_first)
#print(parent_node)
first_node=parent_node[0]
#print(node_set)
tree_list=[]
tree=[]
for node_iter in node_set[first_node]:
    
def tree_bulid(node):
    if node in parent_node:
        tree.append(node)
        for node_iter in parent_node[node]:
            tree_bulid(i)


