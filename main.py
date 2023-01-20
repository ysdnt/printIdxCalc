import math

print("Mode:\n1. Normal.\n2. Book.")
mode = int(input("\nMode: "))

while(1):
    firstPage = int(input("\n\nFirst page: "))
    lastPage = int(input("Last page: "))

    nPage = lastPage-firstPage+1
    nSheet = math.ceil(nPage/4)
    print(f"Number of pages: {nPage}")
    print(f"Number of sheets: {nSheet}")

    if (mode == 1):
        a = []
        b = []
        i = firstPage
        while i in range(firstPage, lastPage + 1):
            a.extend([i, i+1])
            b.insert(0, i+2)
            b.insert(1, i+3)
            i = i + 4
        a = [0 if x not in range(firstPage, lastPage + 1) else x for x in a]
        b = [0 if x not in range(firstPage, lastPage + 1) else x for x in b]
        print(a)
        print(b)
    else:
        gap = firstPage - 1
        if gap != 0:
            firstPage = firstPage - gap
            lastPage = lastPage - gap
        a = []
        b = []
        if nPage % 4 == 0:
            lastPage_holder = lastPage
        else:
            lastPage_holder = (lastPage//4+1) * 4
        a.append(lastPage_holder)
        a.append(firstPage)
        b.append(int(lastPage_holder/2))
        b.append(b[0] + 1)
        i = firstPage
        while i in range(firstPage, lastPage - 3):
            tmp_a = a[-2:]
            tmp_b = b[-2:]
            a.extend([tmp_a[0]-2, tmp_a[1]+2])
            b.extend([tmp_b[0]-2, tmp_b[1]+2])
            i = i + 4

        a = [0 if x not in range(firstPage, lastPage + 1) else x+gap for x in a]
        b = [0 if x not in range(firstPage, lastPage + 1) else x+gap for x in b]
        print(a)
        print(b)

