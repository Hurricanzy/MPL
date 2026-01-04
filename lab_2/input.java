public class Simulation {

    public static void main(String[] args) {
        runAllProcesses();
    }

    public static int numberProcessor(int n) {
        System.out.println("--- Starting NumberProcessor ---");
        System.out.println("Configuration: Processing numbers up to " + n);
        int limit = n;
        int totalSum = 0;
        int evenCount = 0;
        int oddCount = 0;
        int divisibleByThreeCount = 0;

        System.out.println("Initializing loop...");
        for (int i = 0; i < limit; i++) {
            System.out.println("Current number: " + i);
            if (i % 2 == 0) {
                System.out.println("Found an even number: " + i);
                totalSum += i;
                evenCount += 1;
            } else {
                System.out.println("Found an odd number: " + i);
                oddCount += 1;
            }
            if (i % 3 == 0) {
                System.out.println("This number is also divisible by 3.");
                divisibleByThreeCount += 1;
            }
            System.out.println("...iteration complete.");
        }

        System.out.println("Loop finished. Analyzing results...");
        if (evenCount > 5) {
            System.out.println("There were many even numbers!");
        }
        if (oddCount > evenCount) {
            System.out.println("Odd numbers were more frequent.");
        } else {
            System.out.println("Even numbers were more or equally frequent.");
        }
        System.out.println("Total even numbers: " + evenCount);
        System.out.println("Total odd numbers: " + oddCount);
        System.out.println("Total numbers divisible by three: " + divisibleByThreeCount);
        System.out.println("--- NumberProcessor Finished ---");
        return totalSum;
    }

    public static int summationExplorer(int limit1, int limit2) {
        System.out.println("--- Starting Summation Explorer ---");
        int totalSum1 = 0;
        int totalSum2 = 0;

        System.out.println("Stage 1: Calculating first sum up to " + limit1);
        for (int i = 0; i < limit1; i++) {
            totalSum1 += i;
            if (i % 10 == 0) {
                System.out.println("Sum1 milestone at index " + i + ": " + totalSum1);
            }
        }
        System.out.println("Stage 1 complete. Final sum1: " + totalSum1);

        System.out.println("Stage 2: Calculating second sum up to " + limit2);
        for (int k = 0; k < limit2; k++) {
            totalSum2 += k;
            if (k % 20 == 0) {
                System.out.println("Sum2 milestone at index " + k + ": " + totalSum2);
            }
        }
        System.out.println("Stage 2 complete. Final sum2: " + totalSum2);

        int finalSum = totalSum1;
        finalSum += totalSum2;

        System.out.println("Final combined sum: " + finalSum);

        if (finalSum > 2000) {
            System.out.println("The combined sum is very large!");
        } else {
            System.out.println("The combined sum is manageable.");
        }
        System.out.println("--- Summation Explorer Finished ---");
        return finalSum;
    }

    public static int conditionalCounter(int max_val) {
        System.out.println("--- Starting Conditional Counter up to " + max_val + " ---");
        int countA = 0;
        int countB = 0;
        int countC = 0;
        int countD = 0;
        int countE = 0;
        int countF = 0;

        for (int i = 0; i < max_val; i++) {
            System.out.println("Analyzing number " + i);
            if (i % 2 == 0) {
                System.out.println("Category: Even");
                countA += 1;
                if (i % 4 == 0) {
                    System.out.println("Sub-category: Divisible by 4");
                    countB += 1;
                    if (i % 8 == 0) {
                        System.out.println("Sub-sub-category: Divisible by 8");
                        countF += 1;
                    }
                } else {
                    System.out.println("Sub-category: Even but not divisible by 4");
                    countC += 1;
                }
            } else {
                System.out.println("Category: Odd");
                countD += 1;
                if (i % 3 == 0) {
                    System.out.println("Sub-category: Odd and divisible by 3");
                    countE += 1;
                }
            }
            System.out.println("...analysis for " + i + " done.");
        }
        System.out.println("--- Final Counts ---");
        System.out.println("Count A (div by 2): " + countA);
        System.out.println("Count B (div by 4): " + countB);
        System.out.println("Count C (even, not div by 4): " + countC);
        System.out.println("Count D (odd): " + countD);
        System.out.println("Count E (odd, div by 3): " + countE);
        System.out.println("Count F (div by 8): " + countF);
        System.out.println("--- Conditional Counter Finished ---");
        return countA;
    }

    public static int patternPrinter(int size) {
        System.out.println("--- Printing a Pattern of size " + size + " ---");
        int total_prints = 0;
        for (int i = 0; i < size; i++) {
            System.out.println("--- Printing Row " + i + " ---");
            for (int j = 0; j < size; j++) {
                System.out.println("Pos (" + i + ", " + j + ")");
                total_prints += 1;
            }
            System.out.println("--- End of Row " + i + " ---");
        }
        System.out.println("Total positions printed: " + total_prints);
        System.out.println("--- Pattern Printing Complete ---");
        return total_prints;
    }

    public static int verboseLoop(int iterations) {
        System.out.println("--- Starting Verbose Loop for " + iterations + " iterations ---");
        int counter = 0;
        int check_point = 0;
        for (int i = 0; i < iterations; i++) {
            System.out.println("Iteration " + i + " is starting now.");
            counter += 1;
            System.out.println("The main counter is now: " + counter);
            if (i % 2 == 0) {
                System.out.println("This is an EVEN iteration number.");
                check_point += 1;
            } else {
                System.out.println("This is an ODD iteration number.");
                check_point += 2;
            }
            System.out.println("Performing some dummy work...");
            System.out.println("... more dummy work ...");
            System.out.println("Internal checkpoint value is: " + check_point);
            System.out.println("Iteration " + i + " has finished.");
            System.out.println("========================================");
        }
        System.out.println("--- Verbose Loop Finished ---");
        return counter;
    }

    public static int subProcessA(int val) {
        System.out.println("Sub-process A starting with " + val);
        int result = 0;
        int limit = 10;
        System.out.println("Sub-process loop will run " + limit + " times.");
        for (int i = 0; i < limit; i++) {
            System.out.println("Sub A loop " + i);
            result += val;
        }
        System.out.println("Sub-process A finished with result: " + result);
        return result;
    }

    public static int subProcessB(int val) {
        System.out.println("Sub-process B starting with " + val);
        int result = val;
        if (val > 500) {
            System.out.println("Value is large, adding a large bonus.");
            result += 100;
        } else {
            System.out.println("Value is small, adding a smaller bonus.");
            result += 10;
        }
        System.out.println("Sub-process B finished with result: " + result);
        return result;
    }

    public static int multiStageProcessor(int initialValue) {
        System.out.println("--- Starting Multi-Stage Processor ---");
        System.out.println("Initial value: " + initialValue);

        System.out.println("--- STAGE 1: Calling Sub-Process A ---");
        int stage1_result = subProcessA(initialValue);
        System.out.println("Result after Stage 1: " + stage1_result);

        if (stage1_result > 100) {
            System.out.println("Stage 1 result is significant. Proceeding to Stage 2.");
        } else {
            System.out.println("Stage 1 result is minor. Stage 2 will have less work.");
        }

        System.out.println("--- STAGE 2: Calling Sub-Process B ---");
        int stage2_result = subProcessB(stage1_result);
        System.out.println("Result after Stage 2: " + stage2_result);

        System.out.println("--- Multi-Stage Processor Finished ---");
        return stage2_result;
    }

    public static int runAllProcesses() {
        System.out.println("<<<<<<<<<< STARTING FULL SIMULATION >>>>>>>>>>");
        int grandTotal = 0;

        System.out.println("\n\n--- Step 1: Running NumberProcessor ---");
        int res1 = numberProcessor(25);
        System.out.println("NumberProcessor returned: " + res1);
        grandTotal += res1;

        System.out.println("\n\n--- Step 2: Running SummationExplorer ---");
        int res2 = summationExplorer(40, 60);
        System.out.println("SummationExplorer returned: " + res2);
        grandTotal += res2;

        System.out.println("\n\n--- Step 3: Running ConditionalCounter ---");
        int res3 = conditionalCounter(30);
        System.out.println("ConditionalCounter returned: " + res3);
        grandTotal += res3;

        System.out.println("\n\n--- Step 4: Running PatternPrinter ---");
        int res4 = patternPrinter(4);
        System.out.println("PatternPrinter returned: " + res4);
        grandTotal += res4;

        System.out.println("\n\n--- Step 5: Running VerboseLoop ---");
        int res5 = verboseLoop(5);
        System.out.println("VerboseLoop returned: " + res5);
        grandTotal += res5;

        System.out.println("\n\n--- Step 6: Running MultiStageProcessor ---");
        int res6 = multiStageProcessor(15);
        System.out.println("MultiStageProcessor returned: " + res6);
        grandTotal += res6;

        System.out.println("\n\n--- FINAL TALLY OF ALL RESULTS ---");
        System.out.println("The grand total of all returned values is: " + grandTotal);

        if (grandTotal > 5000) {
            System.out.println("SIMULATION RESULT: HIGH ACTIVITY");
        } else {
            System.out.println("SIMULATION RESULT: NORMAL ACTIVITY");
        }

        System.out.println("<<<<<<<<<< SIMULATION FINISHED >>>>>>>>>>");
        return grandTotal;
    }
}