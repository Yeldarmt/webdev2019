def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)].find(sub_string)>=0:
            cnt+=1
    return cnt

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count