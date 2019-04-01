def mutate_string(string, position, character):
    l =list(string)
    l[position]=character
    b =''.join(l)
    return b

if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new