"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item = str(item)
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1
            
    print(frequencies)
    return frequencies

i = [100, 'Hello', '100', '100', 100]
frequencies(i)