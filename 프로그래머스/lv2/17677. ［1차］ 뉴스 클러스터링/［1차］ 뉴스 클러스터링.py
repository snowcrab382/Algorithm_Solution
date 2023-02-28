def solution(str1, str2):
    str1,str2 = str1.lower(),str2.lower()
    result_1 = []
    result_2 = []

    for i in range(len(str1)-1):
        if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i+1]) <= 122:
            result_1.append(str1[i]+str1[i+1])
    for j in range(len(str2)-1):
        if 97 <= ord(str2[j]) <= 122 and 97 <= ord(str2[j+1]) <= 122:
            result_2.append(str2[j]+str2[j+1])
    
    hap = set(result_1+result_2)
    allhap,cnt = 0,0
    
    for i in hap:
        allhap += max(result_1.count(i),result_2.count(i))
        if i in result_1 and i in result_2:
            cnt += min(result_1.count(i),result_2.count(i))
    
    if allhap == 0:
        return 65536
    return int(cnt*65536/allhap)
