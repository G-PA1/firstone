f={}
l=[]

d1={
    'p':8,
    'q':7,
    'r':3,
}

d2={
    'x':9,
    'y':2,
    'z':0,
}

consumers = {
    'sai':{
        'serial no':1 ,
        'email':'sai@g' ,
        'phone':828 ,
        'address':'anr' ,
        'pincode':500071,
        'subscribed':True
    },

    'jac':{
        'serial no':2 ,
        'email':'rai@g' ,
        'phone':728 ,
        'address':'dnr' ,
        'pincode':500078,
        'subscribed':False
    },

    'sid':{
        'serial no':3,
        'email':'sid@g' ,
        'phone':928 ,
        'address':'mnr' ,
        'pincode':500079,
        'subscribed':True
    },
}


def ad_dict(d1,d2):
    for i in d2:
        if i in d1:
            print('common keys,addition not possible')
            return
        else:
            d1.update({i:d2[i]})
    return d1


print(ad_dict(d1, d2))





