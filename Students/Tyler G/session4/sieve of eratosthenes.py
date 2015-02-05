def sieve_eratosthenes(n):
    """
    Generate a list of odd integers from 3 to "n".
    Use the first element in the list to iterate over the
    remaining elements to remove it's multiples. Rinse and repeat.
    """
    numbers = range(3, n + 1, 2)
    for index, value in enumerate(numbers):
        for num in numbers[index + 2:]:
            if num % value == 0:
                numbers.remove(num)
    numbers.append(2)
    return sorted(numbers)
    
if __name__ == "__main__":
    print sieve_eratosthenes(50)


