'''
Project 1 - Supermarket Bill Analyzer
You had saved the items and their price details in a text file, which you 
purchased yesterday from a nearby supermarket.
You need to know:
1.	How many items did you purchase?
2.	How many items are free?
3.	What is the total amount you had to pay?
4.	What is the discount amount?
5.	What is the final amount you paid after the discount?'''

file_path = 'file.txt'

def analyze_bill():
    try:
        filename = input(file_path)
        with open(filename, "r") as file:
            lines = [line.strip() for line in file if line.strip() != ""]

        paid_items = 0
        free_items = 0
        total_amount = 0
        discount = 0
        discount_found = False

        for line in lines:
            if line.lower().startswith("discount"):
                # Extract discount
                try:
                    discount = int(line.split()[1])
                    discount_found = True
                except:
                    print("Invalid discount line.")
                    return
            else:
                parts = line.split()
                if len(parts) < 2:
                    continue
                price_str = parts[-1]
                if price_str.lower() == "free":
                    free_items += 1
                else:
                    try:
                        price = int(price_str)
                        total_amount += price
                        paid_items += 1
                    except ValueError:
                        print(f"Invalid price format in line: {line}")
                        return

        final_amount = total_amount - discount

        print(f"\nNo of items purchased: {paid_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {total_amount}")
        print(f"Discount given: {discount}")
        print(f"Final amount paid: {final_amount}")

    except FileNotFoundError:
        print("File not found. Please make sure the file name is correct.")
    except Exception as e:
        print(f"An error occurred: {e}")