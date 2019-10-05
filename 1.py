def fourletters(sentence):
    arr=sentence.split(" ")
    count=0
    for x in arr:
        if len(x)==4:
            count=count+1
    return count

#print(fourletters("This sentence is fine"))

def drawRating(vote):
    if vote>=0 and vote<=20:
        return "★☆☆☆☆"
    elif  vote>20 and vote<=40:
        return "★★☆☆☆"
    elif  vote>40 and vote<=60:
        return "★★★☆☆"
    elif vote > 60 and vote <= 80:
        return "★★★★☆"
    elif vote > 80 :
        return "★★★★☆"


def sequences(arr,k):
    arr2=[]
    i=0
    count=0
    while i < len(arr):
        cou=0
        while cou<len(arr):
            if abs(arr[i] - arr[cou]) == 3:
               count=count+1
               str=str(arr[i])+","+str(arr[cou])
        i=i+1

    return count

arr=[1, 5, 3, 4, 2]
print(sequences(arr,3))