old_inventory = [[21, "Bowling Ball"],
    			 [2, "Dirty Sock"],
    			 [1, "Hair Pin"],
    			 [5, "Microphone"]]

new_inventory = [[2, "Hair Pin"],
    			 [3, "Half-Eaten Apple"],
    			 [67, "Bowling Ball"],
    			 [7, "Toothpaste"]]

def update_inventory(old, new):
	result = []
	item_indecies = []
	for i in range(len(old)):
		item_index = 0
		item_in_store = False
		for j in range(len(new)):
			if old[i][1] == new[j][1] and i != j:
				item_in_store = True
				item_index = j
				item_indecies.append(item_index)
				print(str(i) + ": " + str(j))
				print(old[i][1] + ": " + new[j][1])
		if item_in_store == True:
			res_item = old[i]
			res_item[0] += new[item_index][0]
			result.append(res_item)
		else:
			result.append(old[i])
	for n in range(len(new)):
		if not n in item_indecies:
			result.append(new[n])

	print(item_indecies)
	print(len(result))
	return result

print(update_inventory(old_inventory, new_inventory))

