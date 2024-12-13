

def solve(row: list, include_concat=False):
    #Set up the result we want to achieve
    expected_result: int = row[0]
    #Set up the first number
    numbers: int = row[1][::-1]
    queue = []
    #Add the first number to our queue:
    queue.append([numbers[-1], numbers[:-1]])
    #Instead of a for loop we let a while loop run as long as there are entrys in queue:
    while queue:
        #Get the last entry of the queue
        current_result, numbers = queue.pop()
        #Set the next number on the last int from numbers
        next_number = numbers[-1]
        #Set remaining numbers to the rest of the list
        remaining_numbers = numbers[:-1]
        
        #Now we do the addition, multiplication concatenation
        addition = current_result + next_number
        multiplication = current_result * next_number
        concatenation = int(str(current_result) + str(next_number))
        
        #Now we check for each of these if they meet our expected_result
        #AND if there are no remaining numbers
        #If both apply we can return the result since there is a way to solve it.
        if (addition == expected_result) and (len(remaining_numbers) == 0):
            return expected_result
        if (multiplication == expected_result) and len(remaining_numbers) == 0:
            return expected_result
        if (concatenation == expected_result) and include_concat and len(remaining_numbers) == 0:
            return expected_result
        
        #if there are no remaining numbers and we did not found a result we skip to the next iteration of the loop
        if not remaining_numbers:
            continue
        
        #if the result is lower or equal to the expected result we add it back to the queue
        if addition <= expected_result:
            queue.append((addition, remaining_numbers))
        if multiplication <= expected_result:
            queue.append((multiplication, remaining_numbers))
        if (concatenation <= expected_result) and include_concat:
            queue.append((concatenation, remaining_numbers))
            
#Enter each row, I refactored my input into a csv file; so a row looks like this at my code:
#I used some of my data as example
puzzle: list = [(770, [17, 20, 4, 8, 5, 51, 49, 5]),(26278489293, [93, 57, 4, 109, 3, 6, 98, 99, 7]),(2521425784, [1, 7, 826, 8, 237, 39, 9, 8, 23]),(40672828, [730, 9, 68, 504, 28])]
part_one: int = 0
part_two: int = 0
#If we already find a solution from the first part we can exclude the inputs.
#So we add the remaining ones in a second list
second_list = []
for row in puzzle:
    if solve(row):
        part_one += solve(row)
    else:
        second_list.append(row)
#Set part_two to part_one since we dont iterate over all rows again but rather just
#the ones we did not find a solution for already.
part_two = part_one
for row in second_list:
    #set True for concatenation
    if solve(row, True):
        part_two += solve(row, True)
print(f"Result for day 7 exercise 1: {part_one}")
print(f"Result for day 7 exercise 2: {part_two}")


#My read_data function
def read_data(file_path: str) -> list: 
    puzzle = []
    with open("file_path",'r') as file:
        for row in file:
            result, *nums = row.strip().split(',')
            puzzle.append((int(result), list(map(int, nums))))
    return puzzle
puzzle = read_data("path")
