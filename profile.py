import csv

path = "data/olist_order_reviews_dataset.csv"
key_column = "review_id"

row_count = 0
blank_counts = {}
distinct_keys = set()
#note-it is important to give name to the file after opening because otherwise 
# nothing holds it and it is trown away in trash
#note-everything you want to do with the file open needs to be done within the with
#  block because when it closes the file also closes
with open(path, newline="",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    columns = reader.fieldnames

    for column in columns:
        blank_counts[column] = 0

    for row in reader:
        row_count += 1
        distinct_keys.add(row[key_column])
        for column in columns:
            if row[column] == "":
                blank_counts[column] += 1

print("File:", path)
print("Rows:", row_count)
print("Columns:", columns)
print("Blanks per column:", blank_counts)
print("Distinct", key_column, "values:", len(distinct_keys))
print("Key unique:", len(distinct_keys) == row_count)
print("Key blanks:", blank_counts[key_column])