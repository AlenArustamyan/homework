
#Write a python function, which create a dictionary
#for given number N, where keys are numbers from
#1 to N, and values are cubs of that numbers

def create_cubes_dictionary(N):
    cubes_dict = {num: num**3 for num in range(1, N+1)}
    return cubes_dict
N = int(input("Enter a number (N): "))
result_dict = create_cubes_dictionary(N)

print(result_dict)
