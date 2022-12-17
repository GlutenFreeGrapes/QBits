import json,os
c=0
thing={"data":{"num_tossups_found":None,"num_tossups_shown":None,"tossups":[],"num_bonuses_found":None,"num_bonuses_shown":None,"bonuses":[]}}
thing2=dict()
t=dict()
b=dict()
directory='longest'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f) and f.find('.json')>=0:
        c+=1
        print("Parsed %s of %s json files"%(c,len(os.listdir(directory))))
        with open(f, 'r', encoding='utf-8') as ff:
            d = json.load(ff)
        for i in d['data']['tossups']:
            t[i['id']]=i#{'id':i['id'],
                        # "text":i["text"],
                        # "answer":i["answer"],
                        # "tournament_id":i["tournament_id"],
                        # "formatted_answer":i["formatted_answer"],
                        # "category_id":i["category_id"],
                        # "tournament":{
                        #                 "id":i["tournament"]["id"],
                        #                 "name":i["tournament"]["name"],
                        #                 "year":i["tournament"]["year"],
                        #                 "difficulty_num":i["tournament"]["difficulty_num"]
                        #             },
                        # "subcategory_id":i["subcategory_id"]}
        for i in d['data']['bonuses']:
            b[i['id']]=i#{'id':i['id'],
                        # "texts":i["texts"],
                        # "leadin":i["leadin"],
                        # "answers":i["answers"],
                        # "tournament_id":i["tournament_id"],
                        # "formatted_answers":i["formatted_answers"],
                        # "category_id":i["category_id"],
                        # "tournament":{
                        #                 "id":i["tournament"]["id"],
                        #                 "name":i["tournament"]["name"],
                        #                 "year":i["tournament"]["year"],
                        #                 "difficulty_num":i["tournament"]["difficulty_num"]
                        #             },
                        # "subcategory_id":i["subcategory_id"]}
        if c==1:
            thing2=d
        else:
            thing2['data']['tossups'].extend(d['data']['tossups'])
            thing2['data']['bonuses'].extend(d['data']['bonuses'])
print(len(t.keys()),len(b.keys()))
thing['data']['tossups']=list(t.values())
thing['data']['bonuses']=list(b.values())
tt=len(thing['data']['tossups'])
bb=len(thing['data']['bonuses'])
thing['data']['num_tossups_found']=len(t.keys())
thing['data']['num_tossups_shown']=len(t.keys())
thing['data']['num_bonuses_found']=len(b.keys())
thing['data']['num_bonuses_shown']=len(b.keys())
thing2['data']['num_tossups_found']=len(thing2['data']['tossups'])
thing2['data']['num_tossups_shown']=len(thing2['data']['tossups'])
thing2['data']['num_bonuses_found']=len(thing2['data']['bonuses'])
thing2['data']['num_bonuses_shown']=len(thing2['data']['bonuses'])
print(tt,bb)
print(thing2['data']['tossups'][0])
print(thing2['data']['bonuses'][0])
print(thing2['data']['tossups'][-1])
print(thing2['data']['bonuses'][-1])
with open('longest.json','w') as f:
    f.write(json.dumps(thing,indent=2))
print("done with file 1")
# with open('raynor_please_dont_sue_me.json','w') as f:
#     f.write(json.dumps(thing2))
# print("done with file 2")