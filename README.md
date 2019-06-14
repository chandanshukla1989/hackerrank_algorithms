This is a recursive problem and one of hackerranks challenges in which we are getting stream of array datasets like this: 
([1,67,5,4,60],3,632)
The output is one array, and should be derived from input array in such a way that array's length should be equal second argument(3) and 
sum of array elements should be equal to third argument(632)
so here output array will be [167,5,460]

We know as a common practice we place comma in large/big integers. So here 1,67 can be 1 and 67 or only 167 but it can't be 671. 

some more examples to understand it clearly:
    ([5,978,10,7],2,6085) output array will be [5978,107]
