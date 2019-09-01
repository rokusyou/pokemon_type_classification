
def pk_preprocess():
    import numpy as np
    import json
    f = open(r'.\data\pokemon_skills_utf8.json','r',encoding='utf-8')

    pk_zkan = json.load(f)
    f.close()


    ##################
    #    SETTINGS    #
    ##################
    TRAIN_N = 500
    TOT_PK_NUM = 800

    skill_num = 1
    skills =[]
    types =[]
    type_dic ={}
    type_no = 1
    # PK iter
    for i in range(1,TOT_PK_NUM+1):

        # Create skill dictionary
        pk_skills = pk_zkan[str(i)]['skills']
        #print(pk_skills)
        skills.append(pk_skills)

        # Create type dictionary
        pk_type     = pk_zkan[str(i)]['types'][0]
        type_regist = pk_type in type_dic.values()
        #print( "skill name = %s , Dic_exist = %s" % (skill, skill_regist ) )
        if type_regist ==False:
            type_dic[type_no] = pk_type
            type_no +=1

    from gensim import corpora,matutils
    dictionary = corpora.Dictionary(skills)

    tmp = dictionary.doc2bow(pk_zkan[str(1)]['skills'])
    dense = list(matutils.corpus2dense([tmp], num_terms=len(dictionary)).T[0])


    pk_class = {}
    pk_No = 1

    class_no = 1

    for pk_No in range(1,TOT_PK_NUM+1):

        pk_type = pk_zkan[str( pk_No )]['types'][0]
        if ( pk_type in pk_class.values() ) == False:
            pk_class[class_no] = pk_type
            class_no +=1
    #  type => class
    pk_class2 = {v:k for k,v in pk_class.items()}
    pk_class_list = []
    for pk_No in range(1,TOT_PK_NUM+1):
        pk_class_list.append( pk_class2[ pk_zkan[str( pk_No )]['types'][0] ]) 


    pk_skills_v = []
    for pk_No in range(1,TOT_PK_NUM+1):
        tmp = dictionary.doc2bow(pk_zkan[str( pk_No )]['skills'])
        dense = list(matutils.corpus2dense([tmp], num_terms=len(dictionary)).T[0])
        #dense = list(matutils.corpus2dense([tmp], num_terms=len(dictionary)).T[0])
        pk_skills_v.append(dense)
    return pk_skills_v,pk_class_list