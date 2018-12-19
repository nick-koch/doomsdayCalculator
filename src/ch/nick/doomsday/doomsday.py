"""
The formula and other information can be found on: https://www.timeanddate.com/date/doomsday-weekday.html
"""

import datetime

class Main(object):

    #Variables and Constants
    day = 17
    month = 4
    year = 2003
    inputDate = datetime.datetime(year, month, day)
    strInputDate = str(str(day) + "." + str(month) + "." + str(year))

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    anchordays = [[1800, 1900, 2000, 2100], [5, 3, 2, 0]] #[[centurys],[weekdays]]
    universalDoomsday = datetime.datetime(year, 6, 6) #see: https://www.timeanddate.com/date/doomsday-rule.html

    def main(self):

        Display().askForDate()

        doomsday_of_the_year, rest_of_calculation = (Doomsday().getTheDoomsdayOfYear(self.year, self.anchordays, self.weekdays))
        raw_index_number_of_day = Doomsday().doomsdayOfYearToDate(self.inputDate, self.universalDoomsday, self.strInputDate, doomsday_of_the_year, rest_of_calculation)
        weekday = Doomsday().getTheWeekday(raw_index_number_of_day, self.weekdays)
        print(weekday)


class Doomsday(object):
    def getTheDoomsdayOfYear(self, year, anchordays, weekdays):
        # How many times does the number 12 fit as a whole into the two last digits of the year number?
        global anchordayOfTheCentury
        year = str(year)
        last_two_digits = (str(year)[len(year) - 2] + str(year)[len(year) - 1])
        last_two_digits_divided_by_twelve = int(int(last_two_digits) / 12)

        # What is the difference between the two last digits of the year number and the product of the multiples of 12 from calculation 1?
        difference_between_two_last_digits_and_multiple_of_twelve = int(last_two_digits) - (12 * last_two_digits_divided_by_twelve)

        # How many times does the number 4 fit into the result of calculation 2?
        fit_in_number_four = int(difference_between_two_last_digits_and_multiple_of_twelve / 4)

        # What is the century's anchor day?
        first_two_digits = str(year)[0] + str(year)[1]
        century = first_two_digits + "00"

        for centurys in range(len(anchordays[0])):
            if str(anchordays[0][centurys]) == century:
                anchordayOfTheCentury = anchordays[1][centurys]

        # Add up all the results.
        sum_of_all_results = (last_two_digits_divided_by_twelve + difference_between_two_last_digits_and_multiple_of_twelve + fit_in_number_four + anchordayOfTheCentury)

        # Subtract whole multiples of 7 from the result of calculation 5. This will result in a number between 0 and 6, which corresponds to the doomsday of the year.
        rest_of_calculation = sum_of_all_results % 7
        doomsday_of_the_year = weekdays[rest_of_calculation]

        return doomsday_of_the_year, rest_of_calculation

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

    def doomsdayOfYearToDate(self, input_date, universal_doomsday, str_input_date, doomsday_of_the_year, rest_of_calculation):
        # Move from the doomsday to the date in question.
        if input_date <= universal_doomsday:
            str_number_of_days = str(universal_doomsday - input_date)
            int_number_of_days = self.getIntNumberOfDays(str_number_of_days)

            rest_of_division_by_seven = int_number_of_days % 7

            raw_index_number_of_day = rest_of_calculation - rest_of_division_by_seven

            return raw_index_number_of_day

        elif input_date > universal_doomsday:
            str_number_of_days = str(input_date - universal_doomsday)
            int_number_of_days = self.getIntNumberOfDays(str_number_of_days)

            rest_of_division_by_seven = int_number_of_days % 7

            raw_index_number_of_day = rest_of_calculation + rest_of_division_by_seven

            return raw_index_number_of_day

    def getTheWeekday(self, raw_index_number_of_day, weekdays):

        if raw_index_number_of_day < 0:
            index_number_of_day = raw_index_number_of_day + 7
        else:
            index_number_of_day = raw_index_number_of_day

        weekday_of_user_input = weekdays[index_number_of_day]

        return weekday_of_user_input




if __name__ == '__main__':
    Main().main()