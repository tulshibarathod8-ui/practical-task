print(" Welcome to inventory List Analzer!\n")

item_name=[]
item_quantitys=[]
itemcategory_set= set()

while True:

       name = input("Enter item name:")
       category=input("Enter category:")
       quantity=input("Enter quantity:")

       while quantity.isdigit()==False:
              print("please enter a valid number.")
              quantity=input("enter quantity:")

       quantity = int(quantity)

       item_name.append(name)
       item_quantitys.append(quantity)
       itemcategory_set.add(category)

       choice = input("\nDo you want to add more items ?(y/n):")

       if choice!="y":
              break


print("\n=================INVENTORY SUMMARY=======================") 
print()

total_items= len(item_name)

print("\ntotal items:",total_items)


print("items entered:",item_name)

total_quantity = sum(item_quantitys)

print("\ntotal quantity in stock:",total_quantity)
print()

print("Explanation:")

for i in range(total_items):
       print(item_quantitys[i],end="+")

print("=",total_quantity)

average_quantity = total_quantity/total_items

print("\nAverage Quantity per Item:", average_quantity)

print("Explanation:", total_quantity, "/", total_items)

highest_quantity = max(item_quantitys)

for i in range(total_items):

       if item_quantitys[i] == highest_quantity:
              most_stocked_name = item_name[i]
              break

print("\nMost Stocked Item:", most_stocked_name)
print("Quantity:", highest_quantity, "units")


lowest_quantity = min(item_quantitys)

for i in range(total_items):

       if item_quantitys[i] == lowest_quantity:
              least_stocked_name = item_name[i]
              break

print("\nLeast Stocked Item:", least_stocked_name)
print("Quantity:", lowest_quantity, "units")


print("\n--------------------------------------------")

print("\nUnique Categories in Inventory:")

for category in itemcategory_set:
       print(category)

print("Explanation: Set does not allow duplicate values.")

print("\n--------------------------------------------")

print("\nItems Sorted by Quantity (High to Low):")

sorted_names = item_name[:]
sorted_quantities = item_quantitys[:]

for i in range(total_items):

       for j in range(total_items - 1):

              if sorted_quantities[j] < sorted_quantities[j + 1]:

                     temp = sorted_quantities[j]
                     sorted_quantities[j] = sorted_quantities[j + 1]
                     sorted_quantities[j + 1] = temp

                     temp = sorted_names[j]
                     sorted_names[j] = sorted_names[j + 1]
                     sorted_names[j + 1] = temp


for i in range(total_items):

       print(i + 1, ".", sorted_names[i], "-", sorted_quantities[i], "units")


print("\n--------------------------------------------")

print("\nCategories in Alphabetical Order:")

sorted_categories = sorted(itemcategory_set)

for i in range(len(sorted_categories)):

       print(i + 1, ".", sorted_categories[i])

print("\n============ END OF REPORT ============")