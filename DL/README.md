## Exp 1:
1. What is Linear Regression? How does it differ from Logistic Regression? 
2 .Write the equation of a multiple linear regression model with n features. 
3 .What is the cost function used in Linear Regression? Why do we minimise it? 
4 .Explain Gradient Descent. How does it help find the optimal weights? 
5 .What does the R² score tell us? What is an ideal value? 
6 .What is the difference between MAE, MSE, and RMSE? 
Hint: MAE is robust to outliers; MSE penalises large errors more due to squaring; RMSE is in original units.
7 .Why is feature scaling important before applying Linear Regression? 
8 .What is multicollinearity? How does it affect the regression coefficients? 
9 .How do you detect and handle outliers in a regression dataset? 
10 .What is the difference between simple and multiple linear regression? 
11 .What does a positive vs negative regression coefficient mean? 
12 .What is the train-test split? Why don't we train and test on the same data? 
13 .Explain the concept of overfitting in a regression model. How can you detect it? 
14 .What is Ridge Regression (L2 regularisation)? How does it differ from plain Linear Regression? 
15 .What is Lasso Regression (L1 regularisation)? When would you prefer it over Ridge? 
16 .What is the Normal Equation? When is it preferred over Gradient Descent? 
17 .What is homoscedasticity? Why is it an assumption of Linear Regression? 
18 .How do residual plots help evaluate a regression model? 
19 .Explain the concept of the bias-variance tradeoff in regression. 
20 .What is cross-validation? How is k-fold CV better than a single train-test split? 
21 .What preprocessing steps did you apply to the USA Housing dataset? 
22 .How did you handle the categorical 'Address' column in the dataset? 
23 .What does the intercept term β₀ represent in your house price model? 
24 .Which feature had the highest correlation with house price? How did you find this? 
25 .What is the p-value of a regression coefficient? What does it tell you? 
26 .How would you improve the model if the RMSE was still high after Linear Regression? 
27 .What is polynomial regression? When would it be more appropriate than linear? 
28 .What is the difference between correlation and causation in your housing dataset? 
29 .Explain how you would deploy this trained model as an API for real estate agents. 
30 .What ethical concerns exist when using ML models to predict house prices?

## Exp 2:
1.What is a Convolutional Neural Network? How does it differ from a Dense network? 
2.Explain the convolution operation. What does a 3×3 filter detect?
3.What is a feature map (activation map)? How many feature maps does Conv2D(32) produce?
4.Why do we apply ReLU activation after convolution?
5.What is MaxPooling? How does a 2×2 MaxPool change the spatial dimensions?
6.Why is Softmax used in the output layer for MNIST? Write its formula.
7.What loss function is used for multiclass classification? Write the formula.
8.What is Dropout? How does dropout = 0.5 affect a layer with 256 neurons?
9.What is Batch Normalisation? Where is it placed in the network?
10.Why do we reshape MNIST images from (28,28) to (28,28,1)?
11.What does one-hot encoding do to the label '7' in a 10-class problem?
12.What is the Adam optimiser? What makes it better than plain SGD?
13.How does EarlyStopping work? What does patience=5 mean?
14.What is a confusion matrix? How do you read it for a 10-class problem?
15.Define Precision, Recall, and F1-score in the context of digit classification.
16.What is the effect of increasing the number of filters (e.g., from 32 to 64)?
17.What is padding='same' vs padding='valid' in Conv2D?
18.How do you compute the number of trainable parameters in a Conv2D(32, (3,3)) layer?
19.What is the Flatten layer and why is it needed before Dense layers?
20.What is the difference between training accuracy and validation accuracy?
21.Which MNIST digit pairs are most commonly confused and why?
22.What is data augmentation? Give three augmentation techniques suitable for MNIST.
23.Explain the concept of receptive field in a CNN.
24.What is transfer learning? Would it be useful for MNIST? Why or why not?
25.How does ReduceLROnPlateau help during training?
26.What is the vanishing gradient problem? How do ReLU and BatchNorm help address it?
27.What is the difference between a shallow and deep CNN? What are the tradeoffs?
28.How would you handle class imbalance if digit '1' appeared 10× more than digit '5'?
29.What does model.evaluate() return and how does it differ from model.predict()?
30.How would you convert this digit classifier into a real-time handwriting recognition app?

## Exp 3:

1.What is a Recurrent Neural Network? What makes it suitable for sequential data? 
2.What is the vanishing gradient problem in vanilla RNNs? Why does it occur?
3.Explain the architecture of an LSTM cell. What are the three gates?
4.Write the equations for the forget gate and cell state update in LSTM.
5.What is the difference between LSTM and GRU? List advantages of each.
6.What is an Embedding layer? How does it differ from one-hot encoding?
7.What is the vocabulary size parameter in Embedding? How did you choose 10,000?
8.What is sequence padding? Why is post-padding preferred for LSTM?
9.What does MAX_LEN = 300 mean? What happens to reviews longer than 300 tokens?
10.What is a Bidirectional LSTM? How does it improve sentiment analysis?
11.What is Binary Cross-Entropy loss? Write its formula.
12.What is the Sigmoid activation function? Why is it used in the output layer?
13.Explain SpatialDropout1D. How is it different from regular Dropout for sequences?
14.What is teacher forcing in sequence models? Is it used during inference?
15.What is the AUC-ROC score? What does a value of 0.92 mean?
16.How do you choose the decision threshold (default 0.5)? When would you lower it?
17.What is the difference between precision and recall? Give a sentiment analysis example.
18.How does recurrent dropout differ from regular dropout in an LSTM?
19.What is attention mechanism? How would it improve your sentiment model?
20.What is BERT? How does it outperform LSTM for sentiment tasks?
21.What is text tokenisation? Describe the process applied to IMDB reviews.
22.What is the difference between word-level and character-level models?
23.How would you handle negation in sentiment (e.g., 'not good')?
24.What is the purpose of the ReduceLROnPlateau callback in training?
25.What is SMOTE? When would you apply it to the IMDB dataset?
26.How would you extend this binary classifier to a 5-star rating predictor?
27.What is the effect of doubling the LSTM units from 64 to 128?
28.What does the training loss vs. validation loss graph tell you after 15 epochs?
29.How would you interpret the model's output of 0.82 for a movie review?
30.What are the limitations of LSTM for very long documents (e.g., 10,000 words)?

## Exp 5

1.What is hyperparameter tuning? How does it differ from training (learning parameters)? 
2.How does the learning rate affect convergence? What happened at LR = 0.1 vs 0.0001?
3.Compare SGD, Adam, and RMSprop. Which worked best in your experiment and why?
4.What is the effect of filter size (3×3 vs 5×5 vs 7×7) on feature extraction?
5.How does increasing the number of convolutional layers affect the model?
6.What is Transfer Learning? Name two pre-trained models and when you'd use them.
7.What is fine-tuning in transfer learning? How did you apply it?
8.What is Data Augmentation? List 5 techniques and explain each.
9.What is the ImageDataGenerator in Keras? How did you configure it?
10.What is Dropout regularisation? How does dropout=0.4 affect a Dense(512) layer?
11.What is L2 regularisation (weight decay)? How does it prevent overfitting?
12.What is GlobalAveragePooling2D? When is it preferred over Flatten?
13.Explain the concept of receptive field and how it grows with network depth.
14.What is Grid Search? How did you use it to tune hyperparameters?
15.What is Random Search? Why is it sometimes better than Grid Search?
16.What is the difference between overfitting and underfitting? How did your training curves indicate which occurred?
17.What is class activation mapping (CAM)? How does it help interpret CNN decisions?
18.Why is it important to use a separate validation set during hyperparameter tuning?
19.What is Batch Size? How does choosing batch=32 vs batch=256 affect training?
20.What is the difference between local minima, global minima, and saddle points in optimisation?
21.What is weight initialisation? Why does it matter for deep CNN training?
22.What is a learning rate scheduler? Describe the ReduceLROnPlateau strategy.
23.Why is it important to freeze base model layers during the first training phase of transfer learning?
24.What metrics beyond accuracy would you use for an imbalanced medical image dataset?
25.How do you prevent data leakage when using augmentation with train/test split?
26.What is the purpose of the Sigmoid activation in a binary image classifier output?
27.What is Grad-CAM? How does it differ from basic CAM?
28.How would you handle a medical imaging dataset with only 500 labelled images?
29.What is the confusion matrix for binary image classification? Define TP, TN, FP, FN.
30.What hardware would you recommend for training deep CNNs and why?
