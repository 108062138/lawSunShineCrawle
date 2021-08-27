import json
def fop(filename):
    with open(filename,encoding='utf-8') as f:
        dataf = json.load(f)
        for k,v in dataf.items():
            dataf[k] = int(v)
        return dataf
def writefile(dataf):
    minres = {}
    midres = {}
    larres = {}
    #cnt = 0
    for k,v in dataf.items():
    #print(dataf[k])
        if dataf[k]<2000:
            minres[k] = v
        elif dataf[k]<3000 and dataf[k]>=2000:
            midres[k] = v
        else:
            larres[k] = v
    with open('minjg.json','w',encoding = 'utf-8') as f:
        f.write(json.dumps(minres,indent=4,ensure_ascii=False))
    with open('midjg.json','w',encoding = 'utf-8') as f:
        f.write(json.dumps(midres,indent=4,ensure_ascii=False))
    with open('larjg.json','w',encoding = 'utf-8')as f:
        f.write(json.dumps(larres,indent=4,ensure_ascii=False))
if __name__ == '__main__':
    f1 = fop('jg_0_100.json')
    f2 = fop('jg_101_199.json')
    f2.update(f1)
    writefile(f2)
    print('finish')

