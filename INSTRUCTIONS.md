# Interview problem solving test

This is a test of general computer knowledge and use, and problem solving skills. It is originally aimed at developers, but could be applicable to any technical position. There are different levels of this test, which might range from do-able without any code, to challenging for intermediate coders.

My intention is to keep it at the easier side and to not prompt the test taker too much. The theory here is coding is not the first thing a person should reach for when solving a problem, but instead, only write code after you've exhausted other possibilities, or you need to "codify" a solution. Another way of saying this is we're testing for lateral thinking.

## Introduction for test taker

Welcome to Usurper Technologies, maker of fine custom applications. On your first day your boss approaches you and tells you the application you work on is behaving strangely. Helpdesk has been getting reports of non-standard error codes. She wants you to get to the bottom of the issue, preferably before lunch. When you ask for more details, she shrugs, and sends you a log dump in a text file.

Your mission is to figure out what the non-standard error is, and where to start looking for the bug.

## Answer

The answer doesn't really matter, what we want to see if how someone solves the problem. I have a particular solution in mind. I know it's not the only solution, and part of this test will be watching people solve it in different ways, and adjusting it in response.

Here's my solution #1:
- Open the log file in a text editor
- Find replace all spaces with `,`
- Save as a `.csv`
- Open in a spreadsheet
- Sort by the error code column
- Find the non-standard `456` errors

In this solution the testee shows knowledge of:
1. Lateral thinking
2. Basic text editor find/replace and maybe regex
3. A common data excahnge format
4. Spreadsheets
5. Familiarity of error codes
6. Google skills (Unless they know all the error codes off the top of their heads)

Of course other solutions will demonstrate other skills knowledge. Some to look for:
- `sed` or `awk` command line tools
- bash scripting
- file reading in code
- others...
