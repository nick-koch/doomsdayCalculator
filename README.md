# The Doomsday Algorithm - Calculating the Weekday of any given Date

In 1970, British mathematician John Conway devised a way to quickly calculate the weekday of any given date without the help of calculators, computers, or calendars

Conway's algorithm bases on the fact that some dates always fall on the same weekday within any given year. These dates are called *doomsdays*.



## What are Doomsdays?

Apart from being a term for the end of the world, doomsday also refers to a mathematical phenomenon in the Gregorian calendar we use today.

In 1970, British mathematician John Conway devised a way to use the doomsday phenomenon to quickly calculate the weekday of any given date without the help of calculators, computers, or calendars.

His algorithm is based on the fact that there are some dates that inevitably share the same weekday within any given year:

- the last day in February (February 28 in a common year, February 29 in a leap year)
- March 7
- April 4 (or 4/4)
- May 9 (or 5/9)
- June 6 (or 6/6)
- July 11 (or 7/11)
- August 8 (or 8/8)
- September 5 (or 9/5)
- October 10 (or 10/10)
- November 7 (or 11/7)
- December 12 (or 12/12)
- some other dates, including July 4 (U.S. Independence Day) and Halloween

In January, the date varies: it is January 3 in a common year; in a leap year, it falls on January 4.

The weekday these dates fall on is called *doomsday*. The phenomenon is based on the fact that the number of days between these dates are always evenly divisible by 7, which is the number of days per week.



## Calculating the Weekday for any Date 

### Weekdays as numbers

In Conway's concept, each weekday is represented by a number:

Sunday = 0

Monday = 1

Tuesday = 2

Wednesday = 3

Thursday = 4

Friday = 5

Saturday = 6



### The anchor days

Calendars repeat themselves every 400 years, so all you need to do is to remember the anchor days for 4 centuries. As most dates you will come across lie in the time span between 1800 and 2100 it is most practical to remember the anchor days for the 19th, 20th, 21st and 22nd century:

1800 - 1899: Friday

1900 - 1999: Wednesday

2000 - 2099: Tuesday

2100 - 2199: Sunday

For dates outside of this time frame you can simply rely on the 400-year calendar cycle. This means that the anchor day for 1700 - 1799 is again Sunday, in 1600 - 1699 it is Tuesday, and so on.

**Note:** The rules described here apply only to the Gregorian calendar (“Western calendar”). 



### Calculating the doomsday of any given year

To illustrate the calculations, an example is given for each - let's say we want to find out which day of the week February 11, 1978 fell on...

1. ##### How many times does the number 12 fit as a whole into the two last digits of the year number?

   Example date: February 11, 1978. The number 12 fits 6 whole times into 78 (6 x 12 = 72), so the result is **6**.

2. ##### What is the difference between the two last digits of the year number and the product of the multiples of 12 from calculation 1?

   Example: The product of 6 x 12 is 72 (see calculation 1). The difference between 72 and 78 is 6, so the result is **6**.

3. ##### How many times does the number 4 fit into the result of calculation 2?

   Example: The result of calculation 2 was 6. The number 4 fits only once into the number 6, so the result is **1**.

4. ##### [What is the century's anchor day?](#The anchor days) Example: The anchor day of the 1900s is Wednesday, which corresponds to number 3 , so the result is **3**.

5. ##### Add up all the results.

   Example: 6 + 6 + 1 + 3 = 16, so the result is **16**.

6. ##### Subtract whole multiples of 7 from the result of calculation 5. This will result in a number between 0 and 6, which corresponds to the doomsday of the year.

   Example: 16 - 14 = 2, so the result is **2**. This means that the doomsday in 1978 was a **Tuesday**.



### Move from the doomsday to the date in question

Now it is only a small step to the final result. You know the doomsday of the year (in 1978, it was Tuesday), and you know [which dates of the year are doomsdays](#What are Doomsdays?). Now you can simply use the doomsday closest to the date in question to find out which weekday it falls on.

In the example date of February 11, 1978, the closest doomsday is the last day of February, which was February 28 because 1978 was not a leap year. Use multiples of 7 to move closer to the date: 28 - 14 = 14. So you know that February 14 was a Tuesday. Now count the days back to February 11, and you will see: February 11, 1978 fell on a **Saturday**.
