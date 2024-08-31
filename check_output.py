from json import load

with open("test.json", encoding="utf8") as file:
    data = load(file)
missing_values = {"name": 0, "category": 0, "goals": 0, "results": 0, "program": 0}
for course in data:
    for key, value in course.items():
        if len(value) == 0:
            missing_values[key] += 1
with open("output_info.txt", "w") as new_file:
    new_file.write(f"{'Output':^30}\n")
    new_file.write('-'*30 + "\n")
    new_file.write(f"{'Scrapped courses:':<25}{len(data)}\n")
    new_file.write(f"{'Unique courses:':<25}{len(set([course['name'] for course in data]))}\n")
    new_file.write(f"{'Nr of categories:':<28}{len(set([course['category'] for course in data]))}\n")
    new_file.write("Missing values:\n")
    for key, value in missing_values.items():
        new_file.write(f"\t{key:<17}{value/len(data)*100:.2f}%\n")