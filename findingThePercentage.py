if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks:
      if query_name.lower() == key.lower():
          avg = sum(student_marks[key])/len(student_marks[key])
          print(f'{avg:.2f}')
          break
          
