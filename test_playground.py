import unittest
import playground

class TestPlayground(unittest.TestCase):
    def test_add(self): 
        resultat = playground.add(2, 3)
        self.assertEqual(resultat, 5)
        resultat = playground.add(-2, -2)
        self.assertEqual(resultat, -4)
        resultat = playground.add(0, 0)
        self.assertEqual(resultat, 0)

    def test_subtract(self):
        resultat = playground.subtract(2,2)
        self.assertEqual(resultat,0)
        resultat = playground.subtract(2,-2)
        self.assertEqual(resultat,4)
        resultat = playground.subtract(3,5)
        self.assertEqual(resultat,-2)

    def test_multiply(self):
        resultat = playground.multiply(2,3)
        self.assertEqual(resultat,6)
        resultat = playground.multiply(0,3)
        self.assertEqual(resultat,0)
        resultat = playground.multiply(-2,-3)
        self.assertEqual(resultat,6)
        resultat = playground.multiply(-2,3)
        self.assertEqual(resultat,-6)

    def test_divide(self):
        resultat = playground.divide(100, 2)
        self.assertEqual(resultat, 50)
        resultat = playground.divide(0, 2)
        self.assertEqual(resultat, 0.0)
        resultat = playground.divide(-25, 5)
        self.assertEqual(resultat, -5)

    def test_is_even(self):
        resultat = playground.is_even(6)
        self.assertEqual(resultat, True)
        resultat = playground.is_even(3)
        self.assertEqual(resultat, False)
        resultat = playground.is_even(-2)
        self.assertEqual(resultat, True)
        resultat = playground.is_even(0)
        self.assertEqual(resultat, True)

    def test_max_of_two(self):
        resultat = playground.max_of_two(3,5)
        self.assertEqual(resultat, 5)
        resultat = playground.max_of_two(-1,0)
        self.assertEqual(resultat, 0)
        resultat = playground.max_of_two(-100,-5)
        self.assertEqual(resultat, -5)

    def test_min_of_two(self):
        resultat = playground.min_of_two(3,5)
        self.assertEqual(resultat, 3)
        resultat = playground.min_of_two(0,3)
        self.assertEqual(resultat, 0)
        resultat = playground.min_of_two(-100,-50)
        self.assertEqual(resultat, -100)

    def test_factorial(self):
        resultat = playground.factorial(1)
        self.assertEqual(resultat, 1)
        resultat = playground.factorial(3)
        self.assertEqual(resultat, 6)
        resultat = playground.factorial(5)
        self.assertEqual(resultat, 120)        

    def test_is_palindrome(self):
        resultat = playground.is_palindrome(1221)
        self.assertEqual(resultat, True)
        resultat = playground.is_palindrome(75875)
        self.assertEqual(resultat, False)
        resultat = playground.is_palindrome(1)
        self.assertEqual(resultat, True)

    def test_count_vowels(self):
        resultat = playground.count_vowels("lena")
        self.assertEqual(resultat, 2)
        resultat = playground.count_vowels("fjadk8dj2j5h8s93h")
        self.assertEqual(resultat, 1)
        resultat = playground.count_vowels("äo")
        self.assertEqual(resultat, 1)

    def test_find_max(self):
        resultat = playground.find_max([100,50,-3,0])
        self.assertEqual(resultat, 100)
        resultat = playground.find_max([0,0,0,0,0])
        self.assertEqual(resultat, 0)
        resultat = playground.find_max([])
        self.assertEqual(resultat, None)

    def test_bubble_sort(self):
        resultat = playground.bubble_sort([1,2,3,4,5,6])
        self.assertEqual(resultat, [1,2,3,4,5,6])
        resultat = playground.bubble_sort([6,3,5,4,2,1])
        self.assertEqual(resultat, [1,2,3,4,5,6])
        resultat = playground.bubble_sort([])
        self.assertEqual(resultat, [])
        resultat = playground.bubble_sort([1,1,1,2,1,1,1])
        self.assertEqual(resultat, [1,1,1,1,1,1,2])
        resultat = playground.bubble_sort([1,2,3,4,5,0,-1,-2])
        self.assertEqual(resultat, [-2,-1,0,1,2,3,4,5])

    def test_binary_search(self):
        resultat = playground.binary_search([1,2,3,4,5,6], 3)
        self.assertEqual(resultat, 2)
        resultat = playground.binary_search([1,2,3,4,5,6],0)
        self.assertEqual(resultat, -1)
        resultat = playground.binary_search([-2,-1,0,1,2,3,4,5,6],0)
        self.assertEqual(resultat, [1,2,3,4,5,6],2)


if __name__ == "__main__":
    unittest.main()