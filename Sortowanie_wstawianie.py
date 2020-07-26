"""zaimplementuj sortowanie przez wstawiane -
 http://www.algorytm.edu.pl/algorytmy-maturalne/sortowanie-przez-wstawianie.html"""

object_to_sort = [2, 111, 3, 22, 8, 7, 1]
print(object_to_sort)

for i in range(1, len(object_to_sort)):
    for a in range (0, len(object_to_sort[0:i])):
        f = object_to_sort[i]
        t = object_to_sort[a]
        if object_to_sort[i] >= object_to_sort[a]:
            pass
        else:
            b = object_to_sort[i]
            object_to_sort.insert(a, object_to_sort[i])
            object_to_sort.pop((i+1))

print(object_to_sort)

