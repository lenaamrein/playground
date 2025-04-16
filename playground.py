
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def max_of_two(a, b):
    return a if a > b else b

def min_of_two(a, b):
    return a if a < b else b

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_palindrome(s):
    s = str(s).lower().replace(" ", "")
    return s == s[::-1]

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def find_max(lst):
    if not lst:
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    if add(1,2) == 3:
        print("Add Test bestanden")

    if subtract(5,10) == (-5):
        print("Subtract Test bestanden")
    
    if multiply(0,5) == 0:
        print("Multiply Test bestanden")

    if divide(0,0) == None:
        print("Divide Test bestanden")
    else: print("Divide Test nicht bestanden")

    if is_even(6)== True:
        print("is even Test bestanden")

    if max_of_two(-5,0) == 0:
        print("max of two Test bestanden")
    
    if min_of_two(-1,-2) == -2:
        print("min of two Test bestanden")

    if factorial(4) == 24:
        print("factorial Test bestanden")
    
    if is_palindrome(1221) == 1:
        print("is_palindrome Test bestanden")

    if count_vowels("Ich bin am töstön") == 5:
        print("Vokal Test bestanden")
    # Die Vokale ÄÖÜ sind nicht vorhanden

    if find_max([1000,2,300,4,5,-600000]) == 1000:
        print("find_max Test bestanden")
    
    if bubble_sort([0,7,9,-4,5]) == [-4,0,5,7,9]:
        print("bubble_sort Test bestanden")

    if binary_search([-1,0,1,2,3,4,5,6,7,8,9,10],8) == 9:
        print("binary_search Test bestanden")

    def test_add():
    assert add(1,3) == 4
    assert add(-2,-3) == -5
    assert add(5,-5) == 0
    assert add(1000000, 1) == 1000001
    print("add Test bestanden")

