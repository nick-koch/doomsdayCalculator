"""
The formula and other information can be found on: https://www.timeanddate.com/date/doomsday-weekday.html
"""

import datetime  # datetime is just used to compare date objects and not to get the weekday


class Main(object):
    def main(self):
        date = Display().askForDate()
        splitted_date = date.split(".")
        day = int(splitted_date[0])
        month = int(splitted_date[1])
        year = int(splitted_date[2])
        year_string = splitted_date[2]
        input_date = datetime.datetime(year, month, day)
        universal_doomsday = datetime.datetime(year, 6, 6)  # see: https://www.timeanddate.com/date/doomsday-rule.html

        anchorday_of_the_century = Doomsday().getTheCenturysAnchorday(year_string)

        index_of_doomsday = (Doomsday().getTheDoomsdayOfYear(year_string, anchorday_of_the_century))

        raw_index_number_of_day = Doomsday().doomsdayOfYearToDate(input_date, universal_doomsday, index_of_doomsday)

        weekday = Doomsday().getTheWeekday(raw_index_number_of_day)

        Display().printWeekday(weekday, date)


class Doomsday(object):
    def getTheDoomsdayOfYear(self, year, anchorday_of_the_century):

        # How many times does the number 12 fit as a whole into the two last digits of the year number?
        last_two_digits = (str(year)[len(year) - 2] + str(year)[len(year) - 1])
        last_two_digits_divided_by_twelve = int(int(last_two_digits) / 12)

        # What is the difference between the two last digits of the year number and the product of the multiples of 12 from calculation 1?
        difference_between_two_last_digits_and_multiple_of_twelve = int(last_two_digits) - (12 * last_two_digits_divided_by_twelve)

        # How many times does the number 4 fit into the result of calculation 2?
        fit_in_number_four = int(difference_between_two_last_digits_and_multiple_of_twelve / 4)

        # What is the century's anchor day?
        # anchorday_of_the_century --> method call in main method to make testing easier

        # Add up all the results.
        sum_of_all_results = (last_two_digits_divided_by_twelve + difference_between_two_last_digits_and_multiple_of_twelve + fit_in_number_four + anchorday_of_the_century)

        # Subtract whole multiples of 7 from the result of calculation 5. This will result in a number between 0 and 6, which corresponds to the doomsday of the year.
        rest_of_calculation = sum_of_all_results % 7
        index_of_doomsday = rest_of_calculation

        return index_of_doomsday

    def getTheCenturysAnchorday(self, year):
        anchordays = [2, 0, 5, 3]

        first_two_digits = year[0] + year[1]
        modulo_four = int(first_two_digits) % 4
        anchorday_of_the_century = anchordays[modulo_four]

        return anchorday_of_the_century

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def getIntNumberOfDays(self, str_number_of_days):
        global strNumberOfDaysWithoutText
        if self.is_number(str_number_of_days[0]):
            strNumberOfDaysWithoutText = str_number_of_days[0]
            if self.is_number(str_number_of_days[1]):
                strNumberOfDaysWithoutText += str_number_of_days[1]
                if self.is_number(str_number_of_days[2]):
                    strNumberOfDaysWithoutText += str_number_of_days[2]

        int_number_of_days = int(strNumberOfDaysWithoutText)
        return int_number_of_days

    def doomsdayOfYearToDate(self, input_date, universal_doomsday, index_of_doomsday):
        # Move from the doomsday to the date in question.
        if input_date <= universal_doomsday:
            str_number_of_days = str(universal_doomsday - input_date)
            int_number_of_days = self.getIntNumberOfDays(str_number_of_days)

            rest_of_division_by_seven = int_number_of_days % 7

            raw_index_number_of_day = index_of_doomsday - rest_of_division_by_seven

            return raw_index_number_of_day

        elif input_date > universal_doomsday:
            str_number_of_days = str(input_date - universal_doomsday)
            int_number_of_days = self.getIntNumberOfDays(str_number_of_days)

            rest_of_division_by_seven = int_number_of_days % 7

            raw_index_number_of_day = index_of_doomsday + rest_of_division_by_seven

            return raw_index_number_of_day

    def getTheWeekday(self, raw_index_number_of_day):

        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        if raw_index_number_of_day < 0:
            index_number_of_day = raw_index_number_of_day + 7
        elif raw_index_number_of_day > 6:
            index_number_of_day = raw_index_number_of_day - 7
        else:
            index_number_of_day = raw_index_number_of_day

        weekday_of_user_input = weekdays[index_number_of_day]

        return weekday_of_user_input


class Display(object):
    def askForDate(self):
        user_input = input("Please enter a date (DD.MM.YYYY):")
        try:
            datetime.datetime.strptime(user_input, '%d.%m.%Y')
        except:
            Display().askForDate()
        return user_input

    def printWeekday(self, weekday, date):
        print("The", date, "was/is a", weekday)


if __name__ == '__main__':
    Main().main()
