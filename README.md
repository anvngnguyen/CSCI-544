<h2>CSCI 544: Applied Natural Language Processing</h2>
<h3>Homework 1: Spam filtering using a naïve Bayes classifier</h3>
<p>
    Objectives: Implementing a Naive Bayes Classifier and applying it to a 
    binary text classification task (i.e, spam detection)
</p>
<ul>
    <li>
        Task 1: Implementing a standard Naive Bayes classfier with add-one 
        smoothing to prevent the probability becomes 0 for unseen word in 
        the testing data
    </li>
    <li>
        Task 2: Experimenting by training the classifier with only 10% of the 
        training dataset to see how the classifier performs (spoiler: 
        performance descreases) 
    </li>
    <li>
        Task 3: Implementing at least 1 modification to the standard classifier
        Modifications implemented:
        <ul>
            <li>
                Ignore the common words the datasets by setting both of its
                spam and ham probability to 1
            </li>
            <li>
                Using Zipf's Laws to calculate probability of unseen words
                instead of add-one smoothing
            </li>
            <li>
                Removing punctuation from the text
            </li>
        </ul> 
    </li>
</ul>
<h3>Homework 2: Sequence Labeling</h3>
<p>
    Objectives: Using CRFSuite to assign dialogue acts to sequences of 
    utterances in conversations from a corpus
</p>
<ul>
    <li>
        Task 1: Creating a baseline features set for CRFSuite. The set includes:
        <ul>
            <li>
                A feature for whether or not the speaker has changed in 
                comparison with the previous utterance
            </li>
            <li>
                A feature marking the first utterance of the dialogue
            </li>
            <li>
                A feature for every token in the utterance (see the description 
                of CRFsuite for an example)
            </li>
            <li>
                A feature for every part of speech tag in the utterance (e.g., 
                POS_PRP POS_RB POS_VBP POS_.)
            </li>
        </ul> 
    </li>
    <li>
        Task 2: Creating a advanced features set for CRFSuite. The set includes:
        <ul>
            <li>
                All the features from the baseline set with some modification
                for the first utterance feature
            </li>
            <li>
                A feature marking the last utterance of each dialogue
            </li>
            <li>
                A feature marking the length of the part-of-speech in each 
                utterance
            </li>
            <li>
                A feature marking the length of the part-of-speech in each 
                utterance
            </li>
            <li>
                A feature marking the first part-of-speech of each utterance
            </li>
            <li>
                A feature marking the bigram part-of-speech and bigram token
            </li>
        </ul> 
    </li>
</ul>
