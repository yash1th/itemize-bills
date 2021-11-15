from tabulate import tabulate
from decimal import Decimal, ROUND_HALF_UP

# TODO - write unit tests
# TODO - better rounding of numbers


class Item:
    def __init__(self, price):
        self.price = price
        self.people = []
        self.tax_amount = 0.0

    def add_person(self, person):
        self.people += person


class Person:
    def __init__(self):
        self.sub_total = 0
        self.items = []
        self.tax_amount = 0.0
        self.other_amount = 0.0

    def add_item(self, item_name):
        self.items.append(item_name)

    def get_total(self):
        return self.sub_total + self.tax_amount + self.other_amount


def print_items(items):
    _tmp_list = []
    for i in items.keys():
        _tmp_list.append([i, items[i].price, items[i].tax_amount, ','.join(items[i].people)])

    print(tabulate(_tmp_list, headers=['item', 'price', 'tax', 'people']))


def print_people(people):
    _tmp_list = []
    for i in people.keys():
        _tmp_list.append([i, people[i].get_total(), people[i].sub_total, people[i].tax_amount,
                          people[i].other_amount, ','.join(people[i].items)])
    print(tabulate(_tmp_list, headers=['name', 'total', 'sub-total', 'tax', 'others', 'items']))


def calculate_tax_amount(amount, percentage):
    return round(amount * (percentage / 100), 2) if percentage else 0.0


def calculate_percentage(num1, num2):
    return round(num2 / num1 * 100, 2) if num2 else 0.0


def main():
    items = dict()
    people = dict()
    _other_charges = dict()

    _sub_total = float(input('enter sub total before tax - ').strip())
    _tax_amount = round(float(input('enter total tax amount - ').strip()), 2)
    _tax_percentage = calculate_percentage(_sub_total, _tax_amount)

    while True:
        try:
            _tmp_item = input('enter item name, item price - ').strip().split(',', 2)
            if not _tmp_item[0]:
                break
            item_name, item_price = _tmp_item[0].strip(), float(_tmp_item[1].strip())
            items[item_name] = Item(item_price)

            _tmp_people = [i.strip().lower() for i in
                           input(f'enter people involved in {item_name} - ').strip().split(',')]
            items[item_name].add_person(_tmp_people)
            items[item_name].tax_amount = calculate_tax_amount(items[item_name].price, _tax_percentage)
            item_per_person = round(item_price / len(_tmp_people), 2)

            for i in _tmp_people:
                if i not in people:
                    people[i] = Person()
                people[i].add_item(item_name)
                people[i].sub_total += item_per_person
                people[i].tax_amount += calculate_tax_amount(people[i].sub_total, _tax_percentage)
                people[i].tax_amount = float(Decimal(str(people[i].tax_amount)).quantize(Decimal('.01'),
                                                                                         rounding=ROUND_HALF_UP))

        except Exception as e:
            if e is IndexError:
                continue
            else:
                # print(e)
                break

    while True:
        # other charges like tips, service fee etc
        try:
            _input_charge = input('enter any charge name, charge amount - ').strip().split(',', 2)
            if not _input_charge:
                break
            _other_charges[_input_charge[0].strip().lower()] = float(_input_charge[1].strip())
        except Exception as e:
            # if e is KeyboardInterrupt:
            #     break
            if e is IndexError:
                continue
            else:
                # print(e)
                break
    total_other_charges = sum(_other_charges.values())

    if people:
        _other_charge_per_person = round(total_other_charges / len(people), 2)
        for i in people:
            people[i].other_amount = _other_charge_per_person

    return items, people


if __name__ == "__main__":
    items, people = main()
    # print(items)
    print_people(people)
