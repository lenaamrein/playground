
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
    
    def test_add():
        assert add(1,3) == 4
        assert add(-2,-3) == -5
        assert add(5,-5) == 0
        assert add(1000000, 1) == 1000001
        print("add Test bestanden")

    def test_subtract():
        assert subtract(9,7) == 2
        assert subtract(5, 7) == -2
        assert subtract(5,5) == 0
        assert subtract(-5, -100) == 95
        print("substract Test bestanden")

    def test_multiply():
        assert multiply(5,5) == 25
        assert multiply(-5,5) == -25
        assert multiply(0,5) == 0
        assert multiply(-5,-5) == 25
        print("multiply Test bestanden")

    def test_divide():
        assert divide(5,5) == 1
        assert divide(5,-5) == -1
        assert divide(-5,-5) == 1
        assert divide(0,5) == 0
        assert divide(0,0) == None
        print("divide Test bestanden")

    def test_is_even():
        assert is_even(2) == True
        assert is_even(-2) == True
        assert is_even(0) == True
        assert is_even(13) == False
        print("is_even Test bestanden")

    def test_max_of_two():
        assert max_of_two(2,3) == 3
        assert max_of_two(-10,-5) == -5
        assert max_of_two(-3,0) == 0
        assert max_of_two(-100,1) == 1
        print("max_of_two Test bestanden")

    def test_min_of_two():
        assert min_of_two(2,3) == 2
        assert min_of_two(-10,-5) == -10
        assert min_of_two(3,0) == 0
        assert min_of_two(-100,1) == -100
        print("min_of_two Test bestanden")

    def test_factorial():
        assert factorial(5) == 120
        assert factorial(-5) == None
        assert factorial(0) == 1
        assert factorial(2) == 2
        print("factorial Test bestanden")
    #Es kann Dezimalzahlen nicht berechnen

    def test_is_palindrome():
        assert is_palindrome(1221) == True
        assert is_palindrome(23234) == False
        print("is_palindrome Test bestanden")

    def test_count_vowels():
        assert count_vowels("Hallo, mir geht es gut") == 6
        assert count_vowels("jkdlfk") == 0
        assert count_vowels("2j5kdv9ma") == 1
        assert count_vowels("Öhm, Ich bin am testen.") == 5
        print("count_vowels Test bestanden (Ausser ÄÖÜ)")

    def test_find_max():
        assert find_max([1000,200,4,5,6]) == 1000
        assert find_max([-5,-6,-1]) == -1
        assert find_max([0,0,0,0]) == 0
        assert find_max([-5,3,0]) == 3
        print("find_max Test bestanden")


    def test_bubble_sort():
        assert bubble_sort([0,7,9,-4,5]) == [-4,0,5,7,9]
        assert bubble_sort([0,0,0,1,0]) == [0,0,0,0,1]
        print("bubble_sort Test bestanden")

    def test_binary_search():
        assert binary_search([-1,0,1,2,3,4,5,6,7,8,9,10],8) == 9
        assert binary_search([0,1],1) == 1 
        print("binary_search Test bestanden (Ausser wenn Element nicht in der Liste ist)")


    
test_add()
test_subtract()
test_multiply()
test_divide()
test_is_even()
test_max_of_two()
test_min_of_two()
test_factorial()
test_is_palindrome()
test_count_vowels()
test_find_max()
test_bubble_sort()
test_binary_search()
