import argparse


accepted_operations = ['list-operations', 'sum', 'subtract', 'multiply', 'divide']
operations_description = '''
list-operations: Describe all accepted routes at the calculator API. If operands are given, they're ignored.
sum: Add the two operands
subtract: Subtract the two operands
multiply: Multiply the two operands
divide: Divide the two operands
'''

operands_description = '''
Two numbers to perform the desired operation. 
In case no numbers are given, both values are assumed to be 0.
Inputs are expected as floating point numbers following python3 notation.
'''

parser = argparse.ArgumentParser(description='Cliente de calculadora http')

parser.add_argument('operation', choices=accepted_operations, help=operations_description)
parser.add_argument('-o', '--operands', required=False, metavar='<number>', type=float, nargs=2,
                    help=operands_description)

args = parser.parse_args()


def treat_raw_operands(untreated_operands):
    if untreated_operands is not None:
        return untreated_operands
    return [0, 0]


def parse_user_input():
    # argparse forces users to input 0 or 2 args. This ensures that we have always a list with 2 numbers.
    operation = treat_raw_operands(args.operation)
    operands = args.operands

    return (operation, operands)
