->The execution or running time of the program indicates how quickly the output is delivered based on the algorithm you used to solve the problem. To calculate the execution time of the program, we need to calculate the time taken by the program from its initiation to the final result.

->It is important to calculate the execution time when working on a large project. When working on a large project, we have several approaches in mind. The best should be the one that takes the shortest execution time in all scenarios.

Scenarios:- 

-> Worst Case Analysis:
- In the worst-case analysis, we calculate the upper limit of the execution time of an algorithm. It is necessary to know the case which causes the execution of the maximum number of operations.
- For linear search, the worst case occurs when the element to search for is not present in the array. When x is not present, the search () function compares it with all the elements of arr [] one by one. Therefore, the temporal complexity of the worst case of linear search would be Θ (n).

-> Average Case Analysis:
- In the average case analysis, we take all possible inputs and calculate the computation time for all inputs. Add up all the calculated values ​​and divide the sum by the total number of entries.
- We need to predict the distribution of cases. For the linear search problem, assume that all cases are uniformly distributed. So we add all the cases and divide the sum by (n + 1).

-> Best Case Analysis:
- In the best case analysis, we calculate the lower bound of the execution time of an algorithm. It is necessary to know the case which causes the execution of the minimum number of operations. In the linear search problem, the best case occurs when x is present at the first location.
- The number of operations in the best case is constant. The best-case time complexity would therefore be Θ (1) Most of the time, we perform worst-case analysis to analyze algorithms. In the worst analysis, we guarantee an upper bound on the execution time of an algorithm which is good information.
- The average case analysis is not easy to do in most practical cases and is rarely done. In the average case analysis, we need to predict the mathematical distribution of all possible inputs. The Best Case analysis is wrong. Guaranteeing a lower bound on an algorithm does not provide any information because in the Worst Case scenario an algorithm can take years to run.
