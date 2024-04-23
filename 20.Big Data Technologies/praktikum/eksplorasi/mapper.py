#!/usr/bin/env python3
import sys

class PalindromeCheckerMapper:
    
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]
    
    @staticmethod
    def process_input(line):
        word = line.strip()

        is_palindrome = PalindromeCheckerMapper.is_palindrome(word)
        print(f"{word}\t{is_palindrome}")

if __name__ == "__main__":
    for line in sys.stdin:
        PalindromeCheckerMapper.process_input(line)