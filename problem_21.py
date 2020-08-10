

class LinkedList:
    def __init__(self, values=None):
        if values is None:
            self.head = None
        else:
            self.head = Node(val=values[0])
            prev = self.head
            for i in range(1, len(values)):
                next_val = Node(values[i])
                prev.next = next_val
                prev = next_val

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.val, end=",")
            printval = printval.next

    def delete(self, prev, val):
        prev.next = val.next

    def pop_head(self):
        head = self.head
        self.head = self.head.next
        return head

    def get_amicable_sum(self):
        sum_val = 0
        number_to_test = self.pop_head().val

        prev_val = self.head
        next_val = prev_val.next

        while next_val is not None:
            if Amicable.is_amicable(next_val.val, number_to_test):
                print(f"Amicable numbers: {number_to_test}, {next_val.val}")
                sum_val += number_to_test+next_val.val
                self.delete(prev_val, next_val)
                break
            prev_val = next_val
            next_val = prev_val.next
        return sum_val


class Amicable:

    @staticmethod
    def divisors_sum(nb):
        divisors = []
        # start from 2 because 1 will qave nb as quotient which will increase the sum
        for i in range(2, int(nb**0.5)+1):
            q, r = divmod(nb, i)
            if r == 0:
                if q >= i:
                    divisors.append(i)
                    if q > i:
                        divisors.append(q)
        # add 1 as a divisor
        return 1+sum(divisors)

    @staticmethod
    def is_amicable(a, b):
        return Amicable.divisors_sum(a) == b and Amicable.divisors_sum(b) == a


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def main():
    N = 10000
    total = 0
    # the smallest pair of amicable numbers is (220,284)
    llist = LinkedList(values=range(220, N))
    while llist.head.next is not None:
        total += llist.get_amicable_sum()
        # print(llist.head.val)
    print(total)


if __name__ == "__main__":
    main()
