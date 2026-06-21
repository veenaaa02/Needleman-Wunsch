seq1=input("Enter the sequence 1: ")
seq2=input("Enter the sequence 2: ")
seq1=seq1.upper()
seq2=seq2.upper()
match=int(input("Enter the match score: "))
mismatch=int(input("Enter the mismatch score: "))
gap=int(input("Enter the gap penalty: "))
if match<=0:
    print("Match should be positive")
    exit()
if mismatch>=0:
    print("Mismatch should be negative")
    exit()
if gap>=0:
    print("Gap penalty should be negative")
    exit()
rows=len(seq1)+1
cols=len(seq2)+1
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(0)
    matrix.append(row)
for i in range(1,rows):
    matrix[i][0]=(gap)*i
for i in range(1,cols):
    matrix[0][i]=(gap)*i
for i in range(1,rows):
    for j in range(1,cols):
        up=(matrix[i-1][j])+gap
        left=(matrix[i][j-1])+gap
        if seq1[i-1]==seq2[j-1]:
            diag=(matrix[i-1][j-1])+match
        else:
            diag=(matrix[i-1][j-1])+mismatch
        score=max(up,left,diag)
        matrix[i][j]=score
align1=""
align2=""
i=rows-1
j=cols-1
while i>0 or j>0:
    if i>0 and j>0:
        if seq1[i-1]==seq2[j-1]:
            score=match
        else:
            score=mismatch
    if i>0 and j>0 and matrix[i][j]==matrix[i-1][j-1]+score:
        align1+=seq1[i-1]
        align2+=seq2[j-1]
        i=i-1
        j=j-1
    elif i>0 and matrix[i][j]==matrix[i-1][j]+gap:
        align1+=seq1[i-1]
        align2+="-"
        i=i-1
    elif j>0 and matrix[i][j]==matrix[i][j-1]+gap:
        align1+="-"
        align2+=seq2[j-1]
        j=j-1
    else:
        print("Backtracking error")
        break
align1=align1[::-1]
align2=align2[::-1]
print("Aligned Sequence 1:", align1)
print("Aligned Sequence 2:", align2)
i=0
score=0
for i in range(len(align1)):
    if align1[i]=="-" or align2[i]=="-":
        score+=gap
    elif align1[i]==align2[i]:
        score+=match
    else:
        score+=mismatch
print("Score: ",score)