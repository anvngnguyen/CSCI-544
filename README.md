<h2>CSCI 544: Applied Natural Language Processing</h2>
<h3>Homework 1: Spam filtering using a naïve Bayes classifier</h3>
<p>Objectives: Implementing a Naive Bayes Classifier and applying it to a 
binary text classification task (i.e, spam detection)</p>
<ul>
    <li>
        Task1: Implementing a standard Naive Bayes classfier with add-one 
        smoothing to prevent the probability becomes 0 for unseen data
    </li>
    <li>
        Task2: Experimenting by training the classifier with only 10% of the 
        training dataset to see how the classifier performs (spoiler: 
        performance descreases) 
    </li>
    <li>
        Task3: Implementing at least 1 modification to the standard classifier
        Modifications implemented:
        <ul>
            <li>
                Ignore the common words the datasets by setting both of its
                spam and ham probability to 1
            </li>
            <li>
                Using Zipf's Laws to calculate probability of unseen data
                instead of add-one smoothing
            </li>
            <li>
                Removing punctuation from the text
            </li>
        </ul> 
    </li>
</ul>
