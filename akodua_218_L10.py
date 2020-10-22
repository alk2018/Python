#Albert Kodua
#G01139458

def get(xs, index, response=None):
    try:
        return xs[index]
    except IndexError:
        return response
		
def classify(input_string):
    word_list = input_string.split()
    numbers = []
    words = []
    for word in word_list:
        try:
            num = int(word)
            if '.' in word:
                words.append(word)
            else:
                numbers.append(num)
        except:
            words.append(word)
    return (numbers, words)

def shelve(inventory, product_list):
    for (prod, qnty) in product_list:
        if prod not in inventory:
            inventory[prod] = 0
        if qnty + inventory[prod] < 0:
            raise ValueError('negative amount for ' + prod)
        inventory[prod] += qnty