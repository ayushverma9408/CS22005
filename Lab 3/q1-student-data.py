'''
Develop a Python program to read student marks from a text file, calculate the total, average, and grade for each student, and write the results to an output file along with their details.
'''
f1=open("students.txt","r")
f2=open("results.txt","a")
for l in f1:

    l=l.strip().split(",")
    # sirf 3 subjects consider kia hai. 
    roll,name,m1,m2,m3=l[0],l[1],int(l[2]),int(l[3]),int(l[4]) 

    student = {
        "Roll No": roll,
        "Name": name,
        "Physics": m1,
        "Chemistry": m2,
        "Maths": m3
    }
    t=m1+m2+m3
    avg = (m1 + m2 + m3)/ 3

    if avg >= 90: g = "A+"
    elif avg >= 80: g = "A"
    elif avg >= 70: g = "B"
    elif avg >= 60: g = "C"
    elif avg >= 50: g = "D"
    else: g = "F"

    f2.write(
        f"Roll No: {roll}, Name: {name}, "
        f"Total: {t}, Average: {avg}, Grade: {g}\n"
    )
    print(f"Roll No: {roll}, Name: {name}, Total: {t}, Average: {avg}, Grade: {g}")

print("Results written successfully.")
f1.close()
f2.close()