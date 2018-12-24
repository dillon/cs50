# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

a synonym for the disease known as silicosis

## According to its man page, what does `getrusage` do?

returns resource usage measures.

## Per that same man page, how many members are in a variable of type `struct rusage`?

16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

it's faster to point than to make copies of the values

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

for each character in the file, if it is alphabetical, append it to an array called "word", then if "word" is larger than 45 characters long, go to the next word, otherwise repeat the forloop. if the word is not alphabetical, then if it is a digit, skip to the next word, otherwise if it is not a digit and we have word length larger than 0, then we must have found a word. in that case, add '\0' to end the word, increment the words counter, and check its spelling by comparing it to a dictionary, then increment its stopwatch, then print if misspelled, and prepare for next word by clearing the index inside of word[]

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

the size of words in fscanf is unpredictable, whereas with fgetc we can set a limit (of 45 characters) to make the performance more predictable.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

They should not be allowed to edit the data they are given, only to read and/or copy it, so making them constant keeps the text file and the dictionary immutable.
