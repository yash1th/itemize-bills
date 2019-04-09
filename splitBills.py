from pprint import pprint as pp


def getPeople():
    print("Enter list of people separated by commas -- ")
    people = [i.strip().lower() for i in input().split(",")]
    return people, len(people)


def getSubTotal():
    print("Enter Sub total (before tax) : ", end = "")
    return float(input().strip())


def getTax():
    print("Enter tax amount: ",end = "")
    return float(input().strip())


def getItems():
    numberOfItems = int(input("How many items are there : ").strip())
    items = {}
    for _ in range(numberOfItems):
        itemName, itemPrice = input("enter item name, price : ").split(",", 2)
        items[itemName.strip()] = float(itemPrice.strip())
    return items


def calculatePercentage(num1, num2):
    return round(num1/num2 * 100, 2)


def getOtherFees():
    otherFees = {}
    while input("Do you have another fee (y/n): ".strip().lower()) in ["yes","y"]:
        feeName, feeTotal = input("enter fee name, fee total : ").split(",",2)
        otherFees[feeName] = float(feeTotal)
    return otherFees


def getHowMuchPeopleOwe(items):
    from collections import defaultdict
    peopleToItems = defaultdict(float)
    for itemName, itemCost in items.items():
        people = [name.strip().lower() for name in input(f"Who are involved in {itemName} : ").split(",")]
        totalPeople = len(people)
        eachOwe = itemCost/totalPeople
        for name in people:
            peopleToItems[name] += eachOwe
    pp(peopleToItems)

if __name__ == "__main__":
    #people, lenPeople = getPeople()
    #subTotal = getSubTotal()
    taxAmount = getTax()
    taxPercentage = calculatePercentage(taxAmount, subTotal)
    #otherFees = getOtherFees()
    #items = getItems()
    peopleToItems = getHowMuchPeopleOwe({"a":4.5,"b":3.75})
    