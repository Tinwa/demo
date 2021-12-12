#!/usr/bin/python3
import ast
def main():
    a = ast.literal_eval(input())
    dataset2 = []
    out = ''
    stra = ''
    for i in a[0]:
        dataset2.append(i)
        for i1 in range(1,len(a)):
            if i not in a[i1]:
                del(dataset2[-1])
                break
            stra = a[i1].replace(i,'',1)
            a[i1] = stra
    dataset2 = sorted(dataset2)
    for i in range(len(dataset2)):
        out += str(dataset2[i])
    print('"{}"'.format(out))
if __name__ == '__main__':
    main()
