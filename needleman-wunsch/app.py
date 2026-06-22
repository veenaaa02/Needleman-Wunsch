from flask import Flask, render_template, request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/align",methods=["POST"])
def align():
    seq1=request.form["seq1"]
    seq2=request.form["seq2"]
    match=request.form["match"]
    mismatch=request.form["mismatch"]
    gap=request.form["gap"]
    seq1=seq1.upper()
    seq2=seq2.upper()
    match=int(request.form["match"])
    mismatch=int(request.form["mismatch"])
    gap=int(request.form["gap"])
    if not seq1 or not seq2:
        return render_template("error.html",message="Please enter both DNA sequences.")
    if not match or not mismatch or not gap:
        return render_template("error.html",message="Please enter all scoring values.")
    valid = set("ACGTURNDCQEGHILKMFPSTWYV")
    if any(ch not in valid for ch in seq1):
        return render_template("error.html",message="Sequence 1 contains invalid characters. Please enter a valid DNA, RNA, or protein sequence.")
    if any(ch not in valid for ch in seq2):
        return render_template("error.html",message="Sequence 2 contains invalid characters. Please enter a valid DNA, RNA, or protein sequence.")
    if match<=0:
        return render_template("error.html",message="Match should be positive")
    if mismatch>=0:
        return render_template("error.html",message="Mismatch should be negative")
    if gap>=0:
        return render_template("error.html",message="Gap Penalty should be negative")
    try:
        match = int(match)
        mismatch = int(mismatch)
        gap = int(gap)
    except ValueError:
        return render_template("error.html",message="Match, mismatch and gap values must be integers.")
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
    traceback=[]
    while i>0 or j>0:
        traceback.append((i,j))
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
    traceback.append((0,0))
    align1=align1[::-1]
    align2=align2[::-1]
    length=len(align1)
    i=0
    score=0
    match_count=0
    mismatch_count=0
    gap_count=0
    for i in range(len(align1)):
        if align1[i]=="-" or align2[i]=="-":
            score+=gap
            gap_count+=1
        elif align1[i]==align2[i]:
            score+=match
            match_count+=1
        else:
            score+=mismatch
            mismatch_count+=1
    identity=round((match_count/length)*100,2)
    return render_template("results.html",align1=align1,align2=align2,score=score,matrix=matrix,seq1=seq1,
                           seq2=seq2,traceback=traceback,gap_count=gap_count,match_count=match_count,
                           mismatch_count=mismatch_count,length=length,identity=identity)
if __name__=="__main__":
    app.run(debug=True)