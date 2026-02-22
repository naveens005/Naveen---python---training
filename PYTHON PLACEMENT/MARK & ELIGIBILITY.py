class Test:

    def __init__(self, message):
        print("Message:", message)
        self.marks = []
        self.result = []

    def set_user_input(self):
        for i in range(6):
            mark = float(input(f"Enter mark for Student {i+1}: "))
            self.marks.append(mark)

    def check_eligibility(self):
        for mark in self.marks:

            if 70 <= mark <= 85:
                self.result.append("3R")

            elif 86 <= mark <= 100:
                self.result.append("1R")

            elif mark < 70:
                self.result.append("Not Eligible")

            else:
                self.result.append("Invalid")

        print("\nFinal Result List:")
        print(self.result)


test_obj = Test("Interview Eligibility Check")
test_obj.set_user_input()
test_obj.check_eligibility()