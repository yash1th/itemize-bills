from pprint import pprint as pp


def getTax():
    print("Enter tax amount: ",end = "")
    return float(input().strip())


def calculatePercentage(num1, num2):
    return round(num1/num2 * 100, 2)


def getOtherFees():
    otherFees = {}
    while input("Do you have another fee (y/n): ".strip().lower()) in ["yes","y"]:
        feeName, feeTotal = input("enter fee name, fee total : ").split(",",2)
        otherFees[feeName] = float(feeTotal)
    return otherFees


def getHowMuchPeopleOwe():
    from collections import defaultdict
    peopleToItems = defaultdict(float)
    numberOfItems = int(input("Enter the total number of items : ").strip())
    items = defaultdict(float)
    for _ in range(numberOfItems):
        itemName, itemPrice = [i.strip() for i in input("Enter item name, item price : ").split(",", 2)]
        itemPrice = float(itemPrice)
        items[itemName] = itemPrice
        people = [name.strip() for name in input(f"Enter people involved in {itemName} : ").split(",")]
        itemPricePerPerson = itemPrice/len(people)
        for name in people:
            peopleToItems[name] += itemPricePerPerson
    return items, peopleToItems


def addTax(peopleToItems, taxPercentage):
    for k, v in peopleToItems.items():
        peopleToItems[k] += (v*taxPercentage)/100
    return peopleToItems


def addOtherFees(peopleToItems, otherFees):
    totalPeople = len(peopleToItems)
    otherFeesPerPerson = sum([v for _, v in otherFees.items()])/totalPeople
    print("Other fee per person - ", otherFeesPerPerson)
    for k, v in peopleToItems.items():
        peopleToItems[k] += otherFeesPerPerson
    return peopleToItems


if __name__ == "__main__":    
    items, peopleToItems = getHowMuchPeopleOwe()
    subTotal = sum(v for _, v in items.items())
    taxAmount = getTax()
    taxPercentage = calculatePercentage(taxAmount, subTotal)
    peopleToItems = addTax(peopleToItems, taxPercentage)
    otherFees = getOtherFees() 
    peopleToItems = addOtherFees(peopleToItems, otherFees)
    peopleToItems = {k:round(v,2) for k, v in peopleToItems.items()}
    pp(peopleToItems)
