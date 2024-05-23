Problem Description
===================

Your task is to simulate the internal workings of a new ATM model.
The prototype ATM allows users to only withdraw and deposit money;
it also does not (yet) keep track of who put it in or withdrew it.

Only paper money can be deposited or withdrawn, in these denominations:

- 5 $CURRENCY
- 10 $CURRENCY
- 20 $CURRENCY
- 50 $CURRENCY
- 100 $CURRENCY

When withdrawing, users can only specify a total amount of money.
What bills are given out is decided entirely by your ATM program.

Management has decided that example-based unit tests are not reliable enough.
They instruct your team to use property testing, to “prove” that propositions
are true for all possible inputs.

Nevertheless, to show new developers usage examples, example-based unit tests
have to be written as well.

You sigh, as you start a task that seems like twice as much work as usual. You
decide that whenever possible you will write an example-based test first, then
write a simple function that makes it pass, then write a property test … after
which you fearlessly refactor the original function to make it work perfectly.

Step 1
======

The example code written by the architect contains a single property test that
tests if after depositing money into an empty ATM, the ATM contains that exact
amount of money; and that this is true for any combination of bills deposited.

However, it seems the architect has erroneously included a typo before making
their commit. Using the property test, find a minimal set of bills that shows
the error, then write an example-based unit test that fails with those bills.

Finally, fix the typo.

Step 2
======

Management asks you to implement some minimal withdrawal functionality. For
testing purposes, you get 1000 of each bill in monopoly money. Your testing
procedure has to prove that for a set of bills with a total value between 5
and 50000 inclusive, depositing them and withdrawing the same amount always
works flawlessly.

Step 3
======

The company dog (german “Hund im Büro”) ate all the 20 $CURRENCY bills. You
are glad it was only monopoly money, but you have to make sure your ATM can
handle multiples of 20 $CURRENCY even if it contains no corresponding bills.

Before every single test run, 1000 of each bill (except 20 $CURRENCY bills)
are deposited into the ATM. During the test, some money is withdrawn again.

A QA person tells you in the lunch break they will test withdrawing 20000 &
joke that they do not expect your code to be able to handle such an amount.

Step 4
======

It is time to test your ATM code with real money. Due to the company
being cash-strapped, management has only given you 10 $CURRENCY bills
of each denomination. You calculate how much money is in the ATM, then
set out to prove that amounts up to that value can still be withdrawn,
making sure the ATM contains exactly 10 of each note before each test.
