---
title: "Why sorted array faster than unsorted array?"
categories:
  - Software-Development
tags:
  - backend
  - computer science
---

There is a great explanation for this question. In short, it's because of [Branch Prediction](https://en.wikipedia.org/wiki/Branch_predictor).

## What is Branch Prediction?
Consider a railroad junction:
![image-center](/assets/images/post/2020-07-21-branch-prediction-1.jpg){: .align-center}

Now for the sake of argument, suppose this is back in the 1800s - before long-distance or radio communication.

You are the operator of a junction and you hear a train coming. You have no idea which way it is supposed to go. You stop the train to ask the driver which direction they want. And then you set the switch appropriately.

*Trains are heavy and have a lot of inertia. So they take forever to start up and slow down.*

Is there a better way? You guess which direction the train will go to!

- If you guessed right, it continues on.
- If you guessed wrong, the captain will stop, back up, and yell at you to flip the switch. Then it can restart down the other path.

**If you guess right every time**, the train will never have to stop.
**If you guess wrong too often**, the train will spend a lot of time stopping, backing up, and restarting.

---

Consider an if-statement: At the processor level, it is a branch instruction:
![image-center](/assets/images/post/2020-07-21-branch-prediction-2.png){: .align-center}

You are a processor and you see a branch. You have no idea which way it will go. What do you do? You halt execution and wait until the previous instructions are complete. Then you continue down the correct path.

*Modern processors are complicated and have long pipelines. So they take forever to "warm-up" and "slow down".*

Is there a better way? You guess which direction the branch will go to!

- If you guessed right, you continue executing.
- If you guessed wrong, you need to flush the pipeline and roll back to the branch. Then you can restart down the other path.

**If you guess right every time**, the execution will never have to stop.
**If you guess wrong too often**, you spend a lot of time stalling, rolling back, and restarting.

---

This is branch prediction. I admit it's not the best analogy since the train could just signal the direction with a flag. But in computers, the processor doesn't know which direction a branch will go until the last moment.

So how would you strategically guess to minimize the number of times that the train must back up and go down the other path? You look at the past history! If the train goes left 99% of the time, then you guess left. If it alternates, then you alternate your guesses. If it goes one way every three times, you guess the same...

***In other words, you try to identify a pattern and follow it***. This is more or less how branch predictors work.

Most applications have well-behaved branches. So modern branch predictors will typically achieve >90% hit rates. But when faced with unpredictable branches with no recognizable patterns, branch predictors are virtually useless.

Further reading: ["Branch predictor" article on Wikipedia](https://en.wikipedia.org/wiki/Branch_predictor).

## As hinted from above, the culprit is this if-statement
```c
if (data[c] >= 128) {
    sum += data[c];
}
```

Notice that the data is evenly distributed between 0 and 255. When the data is sorted, roughly the first half of the iterations will not enter the if-statement. After that, they will all enter the if-statement.

This is very friendly to the branch predictor since the branch consecutively goes the same direction many times. Even a simple saturating counter will correctly predict the branch except for the few iterations after it switches direction.

### Quick visualization:
```
T = branch taken
N = branch not taken

data[] = 0, 1, 2, 3, 4, ... 126, 127, 128, 129, 130, ... 250, 251, 252, ...
branch = N  N  N  N  N  ...   N    N    T    T    T  ...   T    T    T  ...

       = NNNNNNNNNNNN ... NNNNNNNTTTTTTTTT ... TTTTTTTTTT  (easy to predict)
```

However, when the data is completely random, the branch predictor is rendered useless, because it can't predict random data. Thus there will probably be around 50% misprediction (no better than random guessing).

```
data[] = 226, 185, 125, 158, 198, 144, 217, 79, 202, 118,  14, 150, 177, 182, 133, ...
branch =   T,   T,   N,   T,   T,   T,   T,  N,   T,   N,   N,   T,   T,   T,   N  ...

       = TTNTTTTNTNNTTTN ...   (completely random - hard to predict)
```

### So what can be done?
If the compiler isn't able to optimize the branch into a conditional move, you can try some hacks if you are willing to sacrifice readability for performance.

Replace:
```c
if (data[c] >= 128) {
    sum += data[c];
}
```

with:
```c
int t = (data[c] - 128) >> 31;
sum += ~t & data[c];
```

This eliminates the branch and replaces it with some bitwise operations.

*(Note that this hack is not strictly equivalent to the original if-statement. But in this case, it's valid for all the input values of `data[]`.)*

### Benchmarks: Core i7 920 @ 3.5 GHz
C++ - Visual Studio 2010 - x64 Release

```
//  Branch - Random
seconds = 11.777

//  Branch - Sorted
seconds = 2.352

//  Branchless - Random
seconds = 2.564

//  Branchless - Sorted
seconds = 2.587
```

Java - NetBeans 7.1.1 JDK 7 - x64
```
//  Branch - Random
seconds = 10.93293813

//  Branch - Sorted
seconds = 5.643797077

//  Branchless - Random
seconds = 3.113581453

//  Branchless - Sorted
seconds = 3.186068823
```

Observations:

- **With the Branch**: There is a huge difference between the sorted and unsorted data.
- **With the Hack**: There is no difference between sorted and unsorted data.
- In the C++ case, the hack is actually a tad slower than with the branch when the data is sorted.

A general rule of thumb is to avoid data-dependent branching in critical loops (such as in this example).

> Check out [original post](https://stackoverflow.com/questions/11227809/why-is-processing-a-sorted-array-faster-than-processing-an-unsorted-array) for other explanations.