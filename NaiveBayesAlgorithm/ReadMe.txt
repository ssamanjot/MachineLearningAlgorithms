Naive Bayes Classification program contains different functions and each one is used to perform different tasks.

1. BUILDING A NAIVE BAYES CLASSIFIER
The dataset contains a total of 120 blogs, among which 56 were identified by their author as being “liberal”, with the remaining 64 considered by their author to be “conservative”. Each blog is stored in a separate file, within which each line is a separate word. Files with a name of the form “lib*.txt” are liberal blogs, and files with a name of the form“con*.txt” are conservative. The files split.train and split.test contain lists of files to be used for training and testing a classifier.

Implement the Naive Bayes algorithm, using smoothing. Your program should output predicted labels for the test data, one per line, in the order they are listed in split.test.

2. INTERPRETING THE OUTPUT
Write a program to take a training dataset as input and print out the top 20 words (all in lowercase) with the highest word probabilities in the liberal category as well as in the conservative category (i.e., pˆ(wjCl ib) and pˆ(wjCcons ), where Cl ib is the liberal class and Ccons is the conservative class). As in the previous question, your calculations should use smoothing. The format should be oneword per line, sorted with the highest probability first. Use the same smoothing as in Question 1 above. Print the probabilities with 4 digits after the decimal place (i.e. use “%.04f”). Output the top 20 liberal words and probabilities first, then print a blank line, then print the top 20 conservative words and probabilities.

3. STOP WORDS
It is general practice to preprocess datasets and remove words like “the”, “a”, “of”, etc. before training a classifier. Rather than prespecifying a list of stop words, we can simply exclude the N most frequent words. Write a new classifier which additionally takes a parameter N and excludes the N most frequent words from its vocabulary before training the classifier.Put your observations in nbStopWords.txt.

4. LOG ODDS
Write a program to print out the top 20 words (all in lower case) with the highest log-odds ratio for each class, i.e. log pˆ(wjCl ib ) pˆ(wjCcons ) and log pˆ(wjCcons ) pˆ(wjCl ib ) . Assume the same input and output format as in topwords.py. Print the log-odds with 4 digits after the decimal place (i.e. use “%.04f”). Use natural log (log base e):