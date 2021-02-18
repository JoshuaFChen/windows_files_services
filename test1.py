file1 = r"c:\temp\text1.txt"

with open(file1, 'r') as f:
    lines = f.readlines()
    domain1 = set([line.split('@')[-1].strip() for line in lines])
    print(domain1)