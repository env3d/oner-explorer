# oner-explorer

Imagine you are working as a new bank officer.

Your job is to approve loans, but you don't want to make any mistakes, so you decided to look at some historical data. 

Can we use this to determine who to approve if someone comes in our office?

```
    Gender Income Martial Status Approved
0     Male    LOW        Married       No
1     Male   HIGH        Married      Yes
2   Female    LOW         Single      Yes
3     Male   HIGH        Married       No
4   Female   HIGH         Single       No
5     Male    LOW        Married       No
6   Female    LOW         Single      Yes
7     Male    LOW        Married       No
8   Female    LOW         Single       No
9   Female   HIGH        Married      Yes
10  Female   HIGH        Married      Yes
11  Female    LOW         Single      Yes
12    Male   HIGH         Single       No
13    Male   HIGH         Single       No
14    Male   HIGH         Single       No
15  Female   HIGH        Married      Yes
16  Female   HIGH        Married      Yes
17  Female    LOW         Single      Yes
18  Female    LOW         Single      Yes
19    Male   HIGH         Single       No
20    Male   HIGH         Single       No
21  Female    LOW         Single      Yes
22  Female    LOW         Single       No
23    Male    LOW         Single       No
24  Female   HIGH        Married      Yes
25  Female    LOW         Single      Yes
```

# Counting

"Eyeballing" the data may give us an idea, but let's take a more systemic approach. To start, our end goal is to predict if we want to approve someone when they walk into our office, and we only want to base our approval decision on just ONE of their attribute. We need to determine which attribute is most influential. So we simply look at one attribute at a time. Let's start with the 'Gender' attribute.

## Gender
```
Gender Approved       
Female No            3
       Yes          12
Male   No           10
       Yes           1
```

I have counted all the "Gender - Approval" combinations. It seems like when someone is a female, they are more likely to be approved (12 cases approved, 3 cases reject).

If someone is male, they are most likely rejected (10 cases reject, 1 case approve). What rules can we derive from this knowledge?

   1. If female, approve.  If male, reject.
   1. If female, reject.  If male, reject.
   1. If female, approve.  If male, approve.
   1. If female, reject.  If male, reject.

## Income

Let's do the same for the income column.  Here is the count:

```
Income Approved       
HIGH   No            7
       Yes           6
LOW    No            6
       Yes           7
```

What rule would be the most logical?
 1. High income reject, low income approve
 1. High income approve, low income reject
 1. High income approve, low income approve
 1. High income reject, low income reject

## Martial Status

```
Married        No            4
               Yes           6
Single         No            9
               Yes           7
```

Look at the above count for the martial status column. What rule would be best?
 1. Married approved, single reject
 1. Married approved, single approved
 1. Married reject, single approved
 1. Married reject, single reject

## Deciding on a rule

So now we have 3 rules we can use:

   1. If female, approve.  If male, reject. 84.62% accuracy.
   1. High income reject, low income approve. 53.85% accuracy.
   1. Married approved, single reject. 57.69% accuracy.

Which one should we use if we can only pick one?
 1. Gender
 1. Income
 1. Martial Status


# Discussion

What I just shown you is called the OneR algorithm, and is a real machine learning algorithm
that is used in the real world.

So if we are a bank using historical data to create an automatic approval process, we may
indeed use the gender rule. 

What are the implications?

Check out the OneR result for titanic: https://env3d.github.io/oner-explorer/?dataset=titanic