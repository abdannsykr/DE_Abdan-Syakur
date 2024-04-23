import sys

class MeanCalculatorMapper:
    
    @staticmethod
    def process_input(line):
        values = line.strip().split(',')
        
        total = sum(map(float, values))
        count = len(values)
        
        print(f"{total}\t{count}")

if __name__ == "__main__":
    for line in sys.stdin:
        MeanCalculatorMapper.process_input(line)