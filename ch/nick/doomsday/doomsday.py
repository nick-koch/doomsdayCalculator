"""
The formula and other information can be found on: https://www.timeanddate.com/date/doomsday-weekday.html
"""

import datetime

class Main(object):

    #Variables and Constants
    day = 3
    month = 5
    year = 2000
    inputDate = datetime.datetime(year, month, day)
    strInputDate = str(str(day) + "." + str(month) + "." + str(year))

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    anchordays = [[1800, 1900, 2000, 2100], [5, 3, 2, 0]] #[[centurys],[weekdays]]
    universalDoomsday = datetime.datetime(year, 6, 6) #see: https://www.timeanddate.com/date/doomsday-rule.html

    def main(self):
        doomsdayOfTheYear, restOfCalculation = (Doomsday().getTheDoomsdayOfYear(self.year, self.anchordays, self.weekdays))
        rawIndexNumberOfDay = Doomsday().doomsdayOfYearToDate(self.inputDate, self.universalDoomsday, self.strInputDate, doomsdayOfTheYear, restOfCalculation)
        weekday = Doomsday().getTheWeekday(rawIndexNumberOfDay, self.weekdays)
        print(weekday)


class Doomsday(object):
    def getTheDoomsdayOfYear(self, year, anchordays, weekdays):
        # How many times does the number 12 fit as a whole into the two last digits of the year number?
        global anchordayOfTheCentury
        year = str(year)
        lastTwoDigits = (str(year)[len(year) - 2] + str(year)[len(year) - 1])
        lastTwoDigitsDividedByTwelve = int(int(lastTwoDigits) / 12)

        # What is the difference between the two last digits of the year number and the product of the multiples of 12 from calculation 1?
        differenceBetweenTwoLastDigitsAndMultipleOfTwelve = int(lastTwoDigits) - (12 * lastTwoDigitsDividedByTwelve)

        # How many times does the number 4 fit into the result of calculation 2?
        fitInNumberFour = int(differenceBetweenTwoLastDigitsAndMultipleOfTwelve / 4)

        # What is the century's anchor day?
        firstTwoDigits = str(year)[0] + str(year)[1]
        century = firstTwoDigits + "00"

        for centurys in range(len(anchordays[0])):
            if str(anchordays[0][centurys]) == century:
                anchordayOfTheCentury = anchordays[1][centurys]

        # Add up all the results.
        sumOfAllResults = (lastTwoDigitsDividedByTwelve + differenceBetweenTwoLastDigitsAndMultipleOfTwelve + fitInNumberFour + anchordayOfTheCentury)

        # Subtract whole multiples of 7 from the result of calculation 5. This will result in a number between 0 and 6, which corresponds to the doomsday of the year.
        restOfCalculation = sumOfAllResults % 7
        doomsdayOfTheYear = weekdays[restOfCalculation]

        return doomsdayOfTheYear, restOfCalculation

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def getIntNumberOfDays(self, strNumberOfDays):
        global strNumberOfDaysWithoutText
        if self.is_number(strNumberOfDays[0]):
            strNumberOfDaysWithoutText = strNumberOfDays[0]
            if self.is_number(strNumberOfDays[1]):
                strNumberOfDaysWithoutText += strNumberOfDays[1]
                if self.is_number(strNumberOfDays[2]):
                    strNumberOfDaysWithoutText += strNumberOfDays[2]

        intNumberOfDays = int(strNumberOfDaysWithoutText)
        return intNumberOfDays

    def doomsdayOfYearToDate(self, inputDate, universalDoomsday, strInputDate, doomsdayOfTheYear, restOfCalculation):
        # Move from the doomsday to the date in question.
        if inputDate <= universalDoomsday:
            strNumberOfDays = str(universalDoomsday - inputDate)
            intNumberOfDays = self.getIntNumberOfDays(strNumberOfDays)

            restOfDivisionBySeven = intNumberOfDays % 7

            rawIndexNumberOfDay = restOfCalculation - restOfDivisionBySeven

            return rawIndexNumberOfDay

        elif inputDate > universalDoomsday:
            strNumberOfDays = str(inputDate - universalDoomsday)
            intNumberOfDays = self.getIntNumberOfDays(strNumberOfDays)

            restOfDivisionBySeven = intNumberOfDays % 7

            rawIndexNumberOfDay = restOfCalculation + restOfDivisionBySeven

            return rawIndexNumberOfDay

    def getTheWeekday(self, rawIndexNumberOfDay, weekdays):

        if rawIndexNumberOfDay < 0:
            indexNumberOfDay = rawIndexNumberOfDay + 7
        else:
            indexNumberOfDay = rawIndexNumberOfDay

        weekdayOfUserInput = weekdays[indexNumberOfDay]

        return weekdayOfUserInput

if __name__ == '__main__':
    Main().main()