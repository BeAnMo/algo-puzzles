import os

from src.new_years_chaos.algo import minimumBribes

DIR = os.path.dirname(__file__)
CASES = [
    'case_0.txt'
]

def main():
    for case in CASES:
        filepath = DIR.join(case)
        print(filepath)
        with open(filepath, 'r') as case_text:
            case_q = []

            for line in case_text:
                nums = [int(n) for n in line.split(' ') if n]

            print(case_q)

if __name__ == '__main__':
    main()