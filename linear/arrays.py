expence = [{"January": 2200}, {"February": 2350}, {"March": 2600}, {"April": 2130}, {"May": 2190}]



# 1. In Feb, how many dollars you spent extra compare to January?
extra_feb_jan = expence[1]["February"] - expence[0]["January"]
print(f"Extra spent in February compared to January: ${extra_feb_jan}")

# 2. Find out your total expense in first quarter (first three months) of the year.
total_first_quarter = expence[0]["January"] + expence[1]["February"] + expence[2]["March"]
print(f"Total expense in first quarter: ${total_first_quarter}")

# 3. Find out if you spent exactly 2000 dollars in any month
# option 1
for ex in expence:
    if 2000 in ex.values():
        print(f"Yes, spent exactly $2000 in {list(ex.keys())} month")

# option 2
for month , amount in expence.items():
    if amount == 2000:
        print(f"Yes, spent exactly $2000 in {month} month")
        

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expence.append({"June": 1980})
print(f"Updated expense list: {expence}")

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
expence[3]["April"] -= 200
print(f"Corrected expense list after refund: {expence}")