import sys

class MeanCalculatorReducer:
    
    def __init__(self):
        self.total_sum = 0
        self.total_count = 0
    
    def process_input(self, line):
        total, count = map(float, line.strip().split('\t'))
      
        self.total_sum += total
        self.total_count += count
    
    def calculate_mean(self):
        return self.total_sum / self.total_count

if __name__ == "__main__":
    mean_calculator = MeanCalculatorReducer()
    
    for line in sys.stdin:
        mean_calculator.process_input(line)
   
    mean = mean_calculator.calculate_mean()
    print("Rata-rata:", mean)