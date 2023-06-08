if __name__ == '__main__':
    students = [] # list for storing student names and scores
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score]) #adding entered names and scores
      
a=[] #list for storing only scores

for i in students:
  a.append(i[1])
sat = set(a) #converting list to set to get unique values

Second_lowest = sorted(sat)[1] #getting 2nd lowest score

studs = [] # list to store names with 2nd lowest score if there are more than 1 student with same score

for i in students:
  if Second_lowest==i[1]:
    studs.append(i[0])
    
studs_sorted = sorted(studs) #sorting names alphabetically

for i in studs_sorted:
  print(i)
