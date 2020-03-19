from oner import OneR
import pandas
import functools
import json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

# expects a column list
def create_fit(df, prefix, pred, cols):
    cls = OneR()
    filename = prefix+"/"+pred+".json"
    X = df[cols]
    Y = df[pred]
    resp = cls.fit(X,Y)

    with open(filename,'w') as f:
        f.write(json.dumps(resp, cls=NpEncoder))
        
    #for i in range(len(cols)):
    #    create_fit(df, pred, cols[:i]+cols[i+1:])


def create_rules(dataset):
    df = pandas.read_csv(dataset+'.csv').fillna(-1)
    attrs = list(df.columns)

    for pred_index in range(len(attrs)):
        pred = attrs[pred_index]
        cols = attrs[:pred_index]+attrs[pred_index+1:]
        create_fit(df, dataset, pred, cols)


create_rules('titanic')
        
df = app.pandas.read_csv('approval.csv')
df['index']=app.pandas.Series(range(len(df)))
df[['Gender','Approved','index']].groupby(['Gender','Approved']).count()
df[['Income','Approved','index']].groupby(['Income','Approved']).count()
df[['Martial Status','Approved','index']].groupby(['Martial Status','Approved']).count()
