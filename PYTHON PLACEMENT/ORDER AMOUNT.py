class Test:

    def __init__(self, message):
        print('Message:', message)
        self.amount = []
        self.total = 0

    def cal_disc(self):
        discount_price = []
        for i in self.amount:
            print('Amount in disc price:', i)
            if i > 500:
                discount_price.append(i * 0.1)
            else:
                discount_price.append(0)
        return discount_price

    def set_user_input(self):
        for i in range(3):
            self.amount.append(float(input('Enter amount: ')))

    def get_final_amount(self):
        disc_price = self.cal_disc()
        print('Calculated Disc price:', disc_price)
        for i, j in enumerate(self.amount):
            self.total += (j - disc_price[i])
        return self.total


test_obj = Test('welcome')
test_obj.set_user_input()
final_bill = test_obj.get_final_amount()
print("Final Bill:", final_bill)