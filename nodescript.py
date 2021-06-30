import json
f = open('./Padloc_Defense.csv').readlines()
StrainDict = {}
ContigDict = {}
elements = []
nodes = []
edges = []
for line in f[1:]:
    data = line.split('!')
    data = data[:16]
    if data[0] not in ContigDict.keys():
        ContigDict[data[0]] = {
            "name":data[0],
            "strain":data[2],
            "gemomeId":data[1],
            "data": []
        }
        t={
        "system":data[4],
        "protein": data[8],
        "start": data[13],
        "end":data[14],
        "strand":data[15]
        }
        ContigDict[data[0]]["data"].append(t)
        
    else:
        t={
        "system":data[4],
        "protein": data[8],
        "start": data[13],
        "end":data[14],
        "strand":data[15]
        }
        ContigDict[data[0]]["data"].append(t)
    if data[1] not in StrainDict.keys():
        StrainDict[data[1]] = {
            "strain":data[2],
            "gemomeId":data[1],
            "contigs": [],
            "contigSet":set()
        }
        StrainDict[data[1]]["contigs"].append((data[0],data[5])) 
        StrainDict[data[1]]["contigSet"].add(data[0]) 
    else:
        StrainDict[data[1]]["contigs"].append((data[0],data[5])) 
        StrainDict[data[1]]["contigSet"].add(data[0]) 


# print(ContigDict.keys(),len(ContigDict.keys()))
# print(StrainDict.keys(),len(StrainDict.keys()))
sum=0
setSum = 0
nodeCount=0
edgeCount=0
l = list(StrainDict.keys())
for i in l[0:200]:
    sum += len(StrainDict[i]["contigs"])
    setSum += len(StrainDict[i]["contigSet"])
    d = {
    "data": {
        "id": i,
        "group": "nodes"
        }
    }
    nodes.append(d)
    nodeCount+=1
    # print(i)
    for j in StrainDict[i]["contigs"]:
        # print(j)
        if j[0] == 'CP022494':
            print(j[0])
        d = {
                "data": {
                    "id": j[0]+":"+j[1],
                    "group": "nodes"
                    }
                }
        nodes.append(d)
        nodeCount+=1
        d = {
    "data": {
        "id": i+j[0]+":"+j[1],
        "source": j[0]+":"+j[1],
        "target": i,
        "group": "edges"
    }}
        edgeCount+=1
        edges.append(d)
defenceSystems = 0
for i in ContigDict.keys():
    n = len(ContigDict[i]["data"])
    matrix = [[0 for _ in range(n)]for _ in range(n)] 
    systemname = set()
    for j in range(n):
        systemname.add(ContigDict[i]["data"][j]["system"])
        for k in range(n):
            if k==j:
               matrix[j][k] = 0
            else: 
                matrix[j][k] = min(abs(int(ContigDict[i]["data"][k]["end"])-int(ContigDict[i]["data"][j]["start"])),abs(int(ContigDict[i]["data"][j]["end"])-int(ContigDict[i]["data"][k]["start"])))
    ContigDict[i]["matrix"] = matrix
    if len(systemname)>1:
        defenceSystems+=1
        print(i)
        print(systemname)
    # print(ContigDict[i])
    
print(sum)
print(setSum)
print(len(ContigDict.keys()),len(StrainDict.keys()))
# print(elements)
print(nodeCount,edgeCount)
print(defenceSystems)
# {
#     "data": {
#         "id": "glyph5",
#         "group": "nodes"
#     }
# }, {
#     "data": {
#         "id": "e22",
#         "source": "glyph9",
#         "target": "glyph8",
#         "group": "edges"
#     }
# },
elements = elements + nodes
elements = elements + edges
with open('./test.json', 'w') as fout:
    json.dump(elements , fout)