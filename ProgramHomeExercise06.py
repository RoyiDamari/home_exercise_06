import random
import statistics
# Exercise 1
num_list: list[int] = [];
for i in range(80, 100):
    num_list.append(i);
print(num_list[0]);
print(num_list[-1]);
print(len(num_list));
print(num_list[3:13]);
print(num_list[3:]);
print(num_list[:9]);
num_list.insert(10,999);
print(num_list);
print(num_list[::-1]);
print(num_list[::2]);

# Exercise 2
temp_list: list[float] = [];
while True:
    float_num: float = float(input("Please enter a temperature: "));
    if float_num == -999:
        break
    elif float_num < -50 or float_num > 50:
        continue
    else:
        temp_list.append(float_num);
print(temp_list);
temp_list.extend([-20.0, 39.1, 18.5]);
print(temp_list);
print(max(temp_list));
print(min(temp_list));
print(sum(temp_list) / len(temp_list));
print(statistics.mean(temp_list));
del temp_list[0];
print(temp_list);
temp_list.remove(18.5);
print(temp_list);
temp_last: float = temp_list.pop();
print(temp_last);
print(temp_list);
clone = temp_list.copy();
clone.sort();
print(clone);
clone = temp_list.copy();
clone.sort(reverse = True);
print(clone);
# Sort function is replacing the original list while sorted function creates a copy of the original list
# Reversed function brings back iterator, A list function must be used to bring it back to a list

# Exercise 3
random_booleans: list[bool] = [random.choice([True, False]) for _ in range(3)];
print(random_booleans);
print(all(random_booleans));
print(any(random_booleans));
print(not any(random_booleans));
print(not all(random_booleans));

random_numbers: list[int] = [random.choice([-2, -1 , 0, 2]) for _ in range(5)];
print(random_numbers);
print(all(random_numbers));
print(any(random_numbers));
print(not any(random_numbers));
print(not all(random_numbers));

# Exercise 4
random_nums: list[int] = [i for i in range(95, 106)];
print(random_nums);
random_nums: list[int] = [i for i in range(10, 21, 2)];
print(random_nums);
random_bool: list[bool] = [random.choice([True, False]) for _ in range(5)];
print(random_bool);

'''Defining a memory cell named _ is when you want to ignore certain values in a loop, indicate 
   that a value is intentionally being ignored makes the code clearer.
   Other developers can immediately understand that the variable is not intended to be used.'''
rand_numbers: list[int] = [random.randint(1, 100) for _ in range(10)];
print(rand_numbers);
greater_then_fifty: list[int] = [i for i in rand_numbers if i > 50];
print(greater_then_fifty);
bigger_numbers: list[int] = [i for i in [random.randint(1, 100) for _ in range(10)] if i > 50];
print(bigger_numbers);

user_string = input("Pleas enter a string: ").lower();
filter_str: list[str] = [i for i in user_string if i != "t" and i != " "];
print(filter_str);

# Exercise 5
rand_nums: list[int] = [2, 4, 6, 8];
index: any = None;
while index not in {0, 1, 2, 3, -4, -3, -2, -1}:
    try:
        index = int(input("Please enter a index: "));
        if index == -999:
            break
        else:
            print("Index is", rand_nums[index]);
    except Exception as e:
        print(f"Something went wrong ---{e}---...try again")
print('finish')


