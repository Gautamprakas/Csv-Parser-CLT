import csv
import sys
import argparse
data = [] # List to store the CSV data

# Load CSV file into memory

def load(filename):
    global data
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
        print(f"Loaded {len(data)} rows from {filename}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print(f"Error loading file: {e}")

# Count number of rows in currently loaded CSV file
def count():
    print(f"Number of rows: {len(data)}")
# Calculate mean of a numeric column in currently loaded CSV file
def mean(column):
    try:
        column_index = data[0].index(column)
        values = [float(row[column_index]) for row in data[1:] if row[column_index].isdigit()]
        mean = sum(values) / len(values)
        print(f"Mean of column {column}: {mean}")
    except ValueError:
        print(f"Column {column} is not numeric")
    except IndexError:
        print(f"Column {column} not found")
    except Exception as e:
        print(f"Error calculating mean: {e}")
# Filter currently loaded CSV file to include only rows where specified column matches specified value
def filter(column, value):
    try:
        column_index = data[0].index(column)
        filtered_data = [row for row in data if row[column_index] == value]
        print(f"Filtered data ({len(filtered_data)} rows):")
        for row in filtered_data:
            print(row)
    except ValueError:
        print(f"Column {column} not found")
    except Exception as e:
        print(f"Error filtering data: {e}")

# Command-line interface
if __name__ == "__main__":
    while True:
        command = input("Enter command: ").split()
        if not command:
            continue
        elif command[0] == "load":
            if len(command) != 2:
                print("Usage: load <file>")
            else:
                load(command[1])
        elif command[0] == "count":
            count()
        elif command[0] == "mean":
            if len(command) != 2:
                print("Usage: mean <column>")
            else:
                mean(command[1])
        elif command[0] == "filter":
            if len(command) != 3:
                print("Usage: filter <column> <value>")
            else:
                filter(command[1], command[2])
        elif command[0] == "quit":
            sys.exit()
        else:
            print("Invalid command")