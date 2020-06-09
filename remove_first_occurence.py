#this program removes the nth repetation of the provided element from list 

lis = []
while  True:

    ele = (input('Enter values (type "done" if completed entering): '))
    if ele == 'done':
        break
    lis.append(ele)


print(lis)

ele = input('enter word: ')

rpt_count = int(input('enetr the count: '))
count = 0
index = -1
for i in lis:
    index+=1
    if i == ele :
        count+=1
    
        if count == rpt_count:
            del lis[index]
            print(lis)
            break


if count == 0:
    print('word is not in list')

elif count< rpt_count:
    print('"', ele,'"',  'is only repeated ', count, ' times,\ncant find the ',rpt_count, ' occurence')

