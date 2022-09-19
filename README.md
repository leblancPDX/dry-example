# DRY Principle Examples

The DRY principle states that "Every piece of knowledge must have a single, unambiguous, authoritative representation with a system."  The principle is usually taken to include code duplication, but was originally intended to refer to data and logic duplication.  Modern interpretations of DRY have come to include Process Duplication in addition to duplicate code.

Duplication can result from *Copy Paste Programming*, poor understanding of how to implement abstractions, failure to understand the data you're working with, or insufficient knowledge of the system as a whole. Regardless of the source of the duplication, it decreases the quality of the code and introduces technical debt. Defects are more likely, bugs are harder to fix, and maintenance will be more costly.

References used to create these examples:
- [DRY - Don't Repeat Yourself](https://apiumhub.com/tech-blog-barcelona/dry-dont-repeat-yourself/)
- [Common Beginner Mistake: Overusing the DRY Principle](https://www.youtube.com/watch?v=ZN6t8AqAONM)

### DRY Example 1

In our first example we can clearly see duplication of both logic and information.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example1.py#L1-L9

The `marketplace_fee` appears in multiple places and the logic to calculate the `processing_fee` is duplicated.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example1_fixed.py#L1-L7

### DRY Example 2

Our second example is a little harder to see, but does contain duplicated logic.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example2.py#L1-L19

The string created when we print the `Animal` is equivalent to what is written to a file. To eliminate this we can create a `serializeAnimal` function that creates the required string, and then call that function from the existing ones.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example2_fixed.py#L1-L21

### DRY Example 3

The third example is a case where the DRY principle should not be used. Looking at the code it seems obvious that the created strings are logically equivalent.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example3.py#L1-L28

So it seems like adding a parent class for the two makes sense.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example3_bad_abstraction1.py#L1-L25

Duplicate logic is now removed. But consider what happens when we want to add new fields, a `breed` for the `Animal` class and `make` and `model` for the `Car` class. If we want to include those strings in the output we have to find a way to force them to be equivalent in some fashion. For example, we could add a `getClassification` that creates an appropriate combined string.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example3_bad_abstraction2.py#L1-L35

This still doesn't look too bad, but consider what happens if we add a new field to just the `Car` object that we want to include in the string. Doing so requires us to know what class we are working with.

https://github.com/leblancPDX/dry-example/blob/main/examples/dry_example3_bad_abstraction3.py#L1-L38

Checking which subclass you have is definitely a Code Smell and may be a sign of a bad abstraction. For this case the apparent code duplication implied that the classes were equivalent, which is not the case. This issue could have been avoided by talking to the product owner about the class.

#### The Code of Duplicate Code is Much Lower than the Cost of a Bad Abstraction