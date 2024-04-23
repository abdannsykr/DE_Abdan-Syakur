#!/usr/bin/env python3
import sys

class PalindromeCheckerReducer:
    
    @staticmethod
    def process_input(line):
        line_parts = line.strip().split('\t')
    
        if len(line_parts) == 2:
            word, is_palindrome = line_parts
            print(f"{word}\t{is_palindrome}")
        else:
            print("Input tidak valid:", line.strip(), file=sys.stderr)

if __name__ == "__main__":
    for line in sys.stdin:
        PalindromeCheckerReducer.process_input(line)