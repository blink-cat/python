def convert(list_touple):
    list1,list1_clean=[],[]
    list_touple_str=str(sorted(list_touple)).replace('[','').replace(']','').replace('(','').replace(')','').replace(' ','').split(',')
    for i in range(len(list_touple_str)):   #提出每个元组第一个元素
        if i%2==0:
            list1.append(list_touple_str[i])
    i=''
    [list1_clean.append(i) for i in list1 if i not in list1_clean]
    dict1={}
    for list1_iter in list1_clean:
        for touple_iter in list_touple :
            if str(touple_iter[0])==list1_iter:
                dict1.setdefault(list1_iter,[]).append(touple_iter)
    return (list1_clean,dict1)
#b=[(0, 1), (0, 2), (0, 3),(0,10),(0, 6),(0,26),(4, 6), (4,5),(6,7),(4, 7), (5, 7), (8, 11),(12, 13),(9, 12), (10, 12), (11, 14), (12, 15), (13, 15), (14,14),(15,17), (16, 18), (17, 18), (18, 20), (21,29),(19, 21), (22, 23), (24, 26), (26, 28), (27, 29)]
#print(node_first)
#print(parent_node)
#print(node_set)

def tree_bulid(node):
    (parent_node,node_set)=convert(b) 
    #print(node_set)
    #print(parent_node)
    end=str(int(node[1])+1)
    if  end in parent_node:      
        if  node_set[end][0] : 
            tree.append(node) 
            #print(tree)
            #print(node_set[end][0])   
            tree_bulid(node_set[end][0])
    else:
        tree.append(node)
        #print(sorted(b)[-1][1])
        #print(tree)
        #print(b)
        if (int(end)-1) !=sorted(b)[-1][1] and len(tree)>=1:
            #print(tree)
            del b[b.index(node)]
            node_set=convert(b)
            del tree[-1]
            #print(tree)
            if len(tree)==0:
                pass
            else:
                #print(tree[-1])
                node_end=tree[-1]
                del tree[-1]
                tree_bulid(node_end)

        #else:
            #print(tree)
        elif (int(end)-1) ==sorted(b)[-1][1]:
            pass
        #print(tree)
    return tree
#f_in=open('C:/Users/yangmengcheng/Desktop/DATA.txt').readlines()
#d=str(f_in).replace(']','').replace('[','').replace("'",'')
b=[(0, 1), (0, 2), (0, 3), (4, 6), (4, 7), (5, 7), (8, 11), (9, 12), (10, 12), (11, 14), (12, 15), (13, 15), (14, 17), (16, 18), (17, 18), (18, 20), (19, 21), (22, 23), (24, 26), (26, 28), (27, 29), (28, 29), (29, 31), (30, 31), (32, 34), (35, 36), (36, 38), (37, 39), (37, 40), (40, 43), (41, 43), (44, 46), (44, 47), (47, 49), (50, 52), (51, 53), (52, 53), (53, 55), (55, 58), (56, 58), (59, 63), (61, 62), (62, 64), (64, 67), (65, 67), (66, 67), (67, 69), (68, 70), (68, 71), (72, 74), (75, 78), (76, 78), (77, 78), (79, 81), (80, 81), (80, 82), (81, 83), (82, 84), (83, 84), (85, 87), (86, 89), (87, 89), (88, 89), (90, 92), (92, 94), (93, 95), (94, 97), (96, 99), (98, 100), (99, 100), (100, 102), (103, 105), (106, 109), (107, 109), (108, 109), (110, 112), (111, 113), (112, 113), (113, 115), (116, 119), (118, 120), (119, 120), (120, 122), (121, 124), (122, 124), (123, 124), (123, 125), (123, 126), (126, 130), (129, 132), (130, 132), (131, 132), (133, 135), (135, 137), (136, 138), (137, 140), (139, 142), (141, 143), (142, 143), (143, 145), (146, 148), (147, 149), (148, 149), (149, 151), (151, 153), (152, 155), (156, 159), (158, 160), (159, 160), (160, 162), (162, 164), (163, 164), (163, 165), (163, 166), (167, 169), (168, 171), (170, 174), (173, 176), (174, 176), (175, 176), (177, 179), (178, 179), (180, 184), (185, 189), (187, 189), (190, 192), (193, 196), (197, 200), (201, 205), (203, 204), (204, 206), (206, 208), (207, 208), (209, 211), (210, 212), (211, 212), (212, 214), (215, 217), (218, 220), (219, 222), (221, 224), (223, 225), (224, 225), (225, 227), (226, 229), (227, 229), (228, 229), (228, 230), (228, 231), (231, 235), (234, 237), (235, 237), (236, 237), (238, 240), (241, 243), (244, 245), (244, 246), (245, 247), (246, 248), (247, 248), (247, 249), (247, 250), (249, 252), (250, 252), (253, 255), (255, 257), (256, 258), (256, 259), (260, 263), (261, 263), (262, 265), (263, 265), (264, 268), (266, 267), (267, 271), (269, 271), (272, 274), (273, 276), (274, 276), (275, 276), (275, 277), (275, 278), (279, 281), (282, 284), (285, 286), (286, 288), (287, 290), (288, 290), (289, 290), (291, 293), (292, 294), (293, 294), (294, 296), (295, 296), (296, 298), (297, 299), (297, 300), (301, 303), (302, 304), (303, 304), (304, 306), (307, 310), (308, 310), (311, 314), (312, 314), (315, 317), (317, 319), (318, 320), (319, 322), (321, 323), (321, 324), (324, 326), (325, 326), (325, 327), (326, 328), (326, 329), (327, 329), (330, 332), (333, 335), (334, 337), (336, 338), (336, 339), (340, 342), (340, 343), (344, 346), (347, 349), (347, 350), (350, 353), (351, 353), (352, 355), (354, 358), (359, 360), (361, 365), (366, 369), (370, 371), (371, 373), (372, 374), (372, 375), (372, 377), (375, 377), (376, 378), (377, 378), (378, 380), (380, 383), (381, 383), (382, 383), (383, 385), (384, 385), (384, 386), (384, 387), (386, 389), (390, 392), (391, 393), (392, 393), (393, 395), (396, 398), (399, 402), (401, 403), (402, 403), (403, 405), (404, 407), (405, 407), (406, 407), (406, 408), (407, 409), (408, 410), (409, 410), (411, 415), (416, 418), (416, 419), (417, 419), (420, 421), (422, 426), (425, 426), (426, 428), (427, 429), (427, 430), (431, 433), (433, 435), (434, 435), (434, 436), (434, 437), (437, 439), (438, 439), (439, 441), (440, 441), (441, 443), (442, 443), (442, 444), (442, 445), (446, 448), (449, 451), (452, 453), (454, 458), (457, 459), (458, 459), (459, 461), (460, 461), (460, 462), (461, 463), (462, 464), (463, 464), (463, 465), (464, 466), (465, 467), (466, 467), (467, 469), (468, 470), (468, 471), (471, 473), (472, 475), (473, 475), (476, 477), (477, 479), (478, 479), (478, 480), (479, 481), (481, 483), (481, 484), (485, 487), (486, 488), (487, 488), (488, 490), (490, 492), (491, 493), (492, 495), (494, 496), (494, 497), (497, 499), (498, 499), (499, 501), (500, 502), (500, 503), (500, 505), (503, 505), (506, 510), (511, 515), (516, 518), (516, 520), (518, 519), (519, 521), (521, 525), (523, 524), (524, 526), (524, 528), (526, 527), (527, 529), (528, 530), (528, 531), (528, 533), (531, 533), (534, 538), (539, 543), (544, 546), (544, 548), (546, 547), (546, 548), (546, 549), (549, 553), (554, 555), (556, 560), (558, 560), (559, 561), (560, 561), (561, 563), (564, 568), (567, 570), (568, 571), (569, 571), (570, 573), (571, 573), (572, 573), (573, 575), (574, 575), (574, 576), (574, 577), (578, 580), (581, 583), (583, 586), (584, 586), (587, 591), (590, 593), (591, 593), (592, 593), (593, 595), (594, 595), (594, 596), (594, 597), (598, 600), (598, 601), (599, 601), (602, 605), (603, 606), (604, 606), (605, 608), (606, 609), (607, 609), (608, 611), (610, 612), (611, 612), (612, 614), (613, 615), (616, 617), (616, 618), (617, 619), (618, 620), (619, 620), (621, 623), (622, 623), (623, 625), (624, 626), (624, 627), (628, 630), (630, 632), (631, 634), (633, 636), (634, 637), (635, 637), (636, 639), (637, 639), (638, 639), (638, 640), (638, 641), (640, 643), (642, 645), (644, 646), (645, 646), (646, 648), (647, 648), (647, 649), (647, 650), (649, 652), (650, 652), (651, 654), (652, 654), (653, 654), (655, 657), (657, 659), (658, 660), (659, 660), (660, 662), (661, 662), (663, 665), (665, 668), (666, 668), (669, 671), (670, 671), (672, 674), (673, 674), (674, 676), (675, 676), (677, 679), (680, 681), (680, 682), (680, 683), (684, 686), (684, 688), (686, 687), (687, 689), (689, 691), (689, 692), (690, 692), (693, 695), (693, 697), (695, 696), (696, 700), (701, 703), (704, 706), (705, 708), (706, 708), (707, 708), (708, 710), (709, 711), (709, 712), (712, 714), (713, 715), (716, 717), (716, 718), (716, 719), (718, 721), (719, 721), (722, 724), (725, 726), (726, 728), (727, 730), (728, 731), (729, 731), (730, 733), (731, 734), (732, 734), (733, 736), (734, 737), (735, 737), (736, 739), (737, 739), (738, 739), (740, 744), (743, 744), (745, 749), (750, 754), (753, 755), (754, 756), (755, 756), (757, 761), (760, 761), (762, 764), (765, 767), (765, 768), (768, 770), (771, 773), (772, 774), (773, 774), (774, 776), (776, 779), (777, 779), (780, 781), (781, 783), (782, 783), (782, 784), (782, 785), (784, 787), (785, 787), (786, 788), (786, 789), (790, 794), (795, 797), (798, 800), (801, 804), (803, 806), (804, 806), (805, 806), (807, 811), (809, 811), (810, 812), (811, 812), (812, 814), (815, 818), (817, 820), (818, 821), (819, 821), (822, 824), (822, 825), (825, 827), (826, 827), (828, 830), (829, 832), (830, 832), (831, 832), (833, 835), (833, 837), (835, 836), (836, 838), (837, 838), (838, 842), (841, 842), (842, 844), (843, 844), (843, 845), (843, 846), (847, 851), (849, 851), (850, 852), (851, 852), (852, 854), (852, 856), (857, 861), (862, 863), (864, 868), (867, 871), (869, 872), (870, 872), (873, 875), (875, 877), (876, 878), (877, 878), (878, 880), (879, 880), (880, 882), (881, 884), (885, 887), (885, 888), (888, 890), (889, 892), (891, 893), (892, 893), (893, 895), (894, 895), (896, 898), (897, 899), (898, 899), (899, 901), (902, 904), (904, 907), (905, 907), (908, 909), (909, 911), (910, 912), (910, 913), (914, 916), (916, 918), (917, 918), (917, 919), (917, 920), (921, 923), (924, 926), (925, 926), (926, 928), (927, 928), (929, 931), (932, 934), (932, 935), (935, 937), (936, 937), (937, 939), (938, 940), (938, 941), (941, 943), (942, 944), (942, 945), (946, 949), (947, 949), (948, 951), (949, 951), (950, 951), (951, 953), (952, 954), (952, 955), (955, 957), (956, 958), (959, 960), (959, 961), (959, 962), (961, 964), (962, 964), (965, 967), (967, 970), (968, 970), (969, 970), (970, 972), (971, 974), (973, 975), (974, 975), (975, 977), (978, 980), (981, 982), (981, 983), (981, 984), (984, 986), (986, 988), (987, 989), (988, 991), (990, 992), (990, 993), (993, 995), (994, 995), (996, 998), (997, 998), (998, 1000), (999, 1001), (1002, 1003), (1003, 1005), (1004, 1005), (1004, 1006), (1004, 1007), (1008, 1010), (1008, 1011), (1009, 1011), (1012, 1015), (1013, 1016), (1014, 1016), (1015, 1018), (1016, 1019), (1017, 1019), (1018, 1021), (1020, 1022), (1021, 1022), (1022, 1024), (1023, 1025), (1026, 1027), (1027, 1029), (1028, 1031), (1029, 1031), (1030, 1031), (1032, 1034), (1033, 1035), (1034, 1035), (1035, 1037), (1036, 1037), (1037, 1039), (1038, 1040), (1038, 1041), (1042, 1044), (1043, 1045), (1044, 1045), (1045, 1047), (1048, 1051), (1049, 1051), (1052, 1055), (1053, 1055), (1056, 1058), (1058, 1060), (1059, 1061), (1060, 1063), (1062, 1064), (1062, 1065), (1065, 1067), (1066, 1067), (1066, 1068), (1067, 1069), (1067, 1070), (1068, 1070), (1071, 1073), (1074, 1076), (1075, 1078), (1077, 1079), (1077, 1080), (1081, 1083), (1081, 1084), (1085, 1087), (1088, 1090), (1088, 1091), (1091, 1094), (1092, 1094), (1093, 1096), (1095, 1099)]
(first_node,node_list)=convert(b)
first_node=first_node[0]
#print(first_node)
#print(node_list[first_node])
tree_list=[]
for node_iter in node_list[first_node]:
    #print(int(node_iter[1]))
    tree=[]
    print(node_iter)
    tree1=tree_bulid(node_iter)
    tree_list.append(tree1)
print(tree_list)
#new_set=convert(b)
#print(new_set[1])