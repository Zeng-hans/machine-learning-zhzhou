import pandas as pd

def get_watermelon_dataset():
    file = open('/Users/HansZeng/Desktop/watermelon-dataset.txt')
    lines = file.readlines()
    m = []
    i = 0
    for line in lines:
        m.append(line.split(","))
        i = i + 1
    df = pd.DataFrame(m[1:])
    l1 = ['是']*8
    l2 = ['否']*9
    l1.extend(l2)
    df[9] = l1
    df.columns = ['编号','色泽','根蒂','敲声','纹理','脐部','触感','密度','含糖率','好瓜']
    return df
