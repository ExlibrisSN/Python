import array
import math

def luhnControlSUM(numberChars):
    numNoChsArr = list(numberChars)
    firstStepSUM = 0
    secondStepSUM = 0
    
    evenNumSTR = numNoChsArr[1::2]
    evenNum = array.array('i',[])
    oddNumSTR = numNoChsArr[::2]
    oddNum = array.array('i',[])
    
    switcher = {
        0:'0',
        1:'2',
        2:'4',
        3:'6',
        4:'8',
        5:'1',
        6:'3',
        7:'5',
        8:'7',
        9:'9'
        }
    for z in range (len(oddNumSTR)):
        oddNum.append(int(oddNumSTR[z]))
        firstStepSUM = firstStepSUM + oddNum[z]

    n = 0
    
    for z in evenNumSTR:
        evenNumSTR[int(n)] = switcher.get((int(z)))
        evenNum.append(int(evenNumSTR[n]))
        secondStepSUM = secondStepSUM + evenNum[n]
        n =n + 1
 
    
    sum = int(firstStepSUM) + int(secondStepSUM)
    controlsum = (math.ceil(sum/10) * 10) - sum
 
    return controlsum