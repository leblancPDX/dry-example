# DRY Principle Examples

The DRY principle states that "Every piece of knowledge must have a single, unambiguous, authoritative representation with a system."  The principle is usually taken to include code duplication, but was originally intended to refer to data and logic duplication.  Modern interpretations of DRY have come to include Process Duplication in addition to duplicate code.

Duplication can result from *Copy Paste Programming*, poor understanding of how to implement abstractions, failure to understand the data you're working with, or insufficient knowledge of the system as a whole. Regardless of the source of the duplication, it decreases the quality of the code and introduces technical debt. Defects are more likely, bugs are harder to fix, and maintenance will be more costly.

### DRY Example 1

https://github.com/leblancPDX/dry-example/blob/e773bafaca52c93153a86c74de69a9c8a90c992c/examples/dry_example1.py#L1-L9

