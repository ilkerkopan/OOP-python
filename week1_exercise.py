# printing odd numbers
for i in range(0,10) :
    if i%2 == 1 : 
        print(i)

#summing two arrays
lab1_scores = [5,2,1,1,3,4,1,2]
lab2_scores = [5,3,2,4,3,5,2,4]
summed_scores = []

for i in range(0,len(lab1_scores)) :
    summed_scores.append(lab1_scores[i] + lab2_scores[i])
print(summed_scores)