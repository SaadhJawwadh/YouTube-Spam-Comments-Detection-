
<!-- Give me a table of contents of h1-->
<a href = '#part-a-–-application-area-review'>Part A – Application area review</a>
</p>
<p>
<a href = '#part-b-–-compare-and-evaluate-ai-techniques'>Part B – Compare and evaluate AI techniques</a>
</p>

<h1 id="part-a-–-application-area-review">Part A – Application area review</h1>

<p>
Prior to the implementation I did a proper Literature review to acknowledge the state of art techniques for detecting YouTube spam comments and ended up with the following findings.
</p>

<table>
  <tr>
   <td><strong>Citation</strong>
   </td>
   <td><strong>Techniques</strong>
   </td>
  </tr>
  <tr>
   <td><a href="https://doi.org/10.1109/ICMLA.2015.37">(Alberto, Lochter and Almeida, 2015)</a>
   </td>
   <td>NB, LR, KNN, RF
   </td>
  </tr>
  <tr>
   <td><a href="https://doi.org/10.1016/j.procs.2018.05.181">(Aiyar and Shetty, 2018)</a>
   </td>
   <td>N-Gram
   </td>
  </tr>
  <tr>
   <td><a href="https://doi.org/10.1109/ICACCI.2018.8554405">(Kanodia, Sasheendran and Pathari, 2018)</a>
   </td>
   <td>Markov’s decision process
   </td>
  </tr>
  <tr>
   <td><a href="https://www.irjet.net/archives/V7/i4/IRJET-V7I488.pdf">(Selvaraj, Konatham and Anand, 2020)</a>
   </td>
   <td>LR
   </td>
  </tr>
  <tr>
   <td><a href="https://doi.org/10.1109/ACCESS.2021.3121508">(Oh, 2021)</a>
   </td>
   <td>Decision Tree, LR, NB, SVM
   </td>
  </tr>
  <tr>
   <td><a href="https://www.semanticscholar.org/paper/A-COMPARATIVE-STUDY-ON-YOUTUBE-SPAM-COMMENT-USING-Ruth-Khan/644b2af51efb2ddbff0634af974b6c0d5abea30d">(Ruth, Khan and Reddy, 2022)</a>
   </td>
   <td>RF, NB, SVM
   </td>
  </tr>
</table>

<p>
Even though techniques like Markov’s decision process and N-Gram have been researched and used for this problem <em>(Aiyar and Shetty, 2018; Kanodia, Sasheendran and Pathari, 2018)</em> classification methods like Naive Bayes (NB), Random Forest (RF), Support Vector Machine (SVM), Logistic Regression (LR), K-nearest Neighbors (KNN)  showed a promising results <em>(Alberto, Lochter and Almeida, 2015; Kanodia, Sasheendran and Pathari, 2018; Selvaraj, Konatham and Anand, 2020; Ruth, Khan and Reddy, 2022) </em>which clearly stated that classification is the optimal technique to address this problem.
</p>
<h1 id="part-b-–-compare-and-evaluate-ai-techniques">Part B – Compare and evaluate AI techniques.</h1>

<p>
Out of the above state of art techniques I have taken Random Forest (RF), Logistic Regression (LR) and  Support Vector Machine (SVM) to compare and evaluate.
</p>

<table>
  <tr>
   <td><strong>Algorithm</strong>
   </td>
   <td><strong>Strength</strong>
   </td>
   <td><strong>Weakness</strong>
   </td>
   <td><strong>Advantage</strong>
   </td>
   <td><strong>Disadvantage</strong>
   </td>
   <td><strong>Input</strong>
   </td>
   <td><strong>Output</strong>
   </td>
  </tr>
  <tr>
   <td>Random Forest (RF)
   </td>
   <td>Good performance on large datasets, handling missing data and high dimensional spaces, ability to identify important features
   </td>
   <td>Computationally expensive, not suitable for real-time applications
   </td>
   <td>Ensemble method that improves overall performance, good for identifying important features
   </td>
   <td>Computationally expensive, not suitable for real-time applications
   </td>
   <td>Numerical or categorical features
   </td>
   <td>Binary class label (spam or not spam)
   </td>
  </tr>
  <tr>
   <td>Logistic Regression (LR)
   </td>
   <td>Simple to implement, requires less computational resources, easily interpretable
   </td>
   <td>Sensitive to outliers, not robust for non-linear problems
   </td>
   <td>Good for binary classification problems, easy to implement and interpret
   </td>
   <td>Sensitive to outliers, not robust for non-linear problems
   </td>
   <td>Numerical or categorical features
   </td>
   <td>Binary class label (spam or not spam)
   </td>
  </tr>
  <tr>
   <td>Support Vector Machine (SVM)
   </td>
   <td>Good for high dimensional spaces and non-linear problems
   </td>
   <td>Sensitive to choice of kernel, selection of parameters
   </td>
   <td>Good for classification and regression problems, useful when number of features is greater than number of samples
   </td>
   <td>Sensitive to choice of kernel, selection of parameters
   </td>
   <td>Numerical or categorical features
   </td>
   <td>Class label, boundary that separates the two classes
   </td>
  </tr>
</table>

<p>
In the context of YouTube comment spam detection, RFs can be used to classify comments as spam or not spam based on various features such as the text content, user information, and comment history. LR can be used to predict the probability of a comment being spam, based on a set of features, and SVM can be used to build a model that separates spam comments from non-spam comments.
</p>
