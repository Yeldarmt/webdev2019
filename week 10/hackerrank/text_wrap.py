import textwrap

def wrap(string, max_width):
    a=[]
    for i in range(0,len(string),max_width):
        a.append(string[i:i+max_width])
    b = "\n".join(a)
    return b

if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result