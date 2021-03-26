# Bayesian Model for Probabilistic Weather and Air Quality Prediction
Using visibility as a proxy for weather and air quality monitoring. A Naive-Bayes and Rule-based approach.

Many urban areas in Africa do not have sufficient monitoring programs to understand their air quality. This study uses visibility as a proxy for PM pollution and the weather to provide insight into air pollution using a microcontroller.

![image](https://user-images.githubusercontent.com/26303032/112496613-f2ea0a80-8d95-11eb-8033-e64c7e0ae9f0.png)

This project includes five key files:
 - naive_bayes.py
 - airpollution.py
 - captureimage.py
 - sample_train.txt
 - sample_test.txt

Run `python3 naive_bayes.py [train dataset] [test dataset]` - to train and test the classifier.

Run `python3 airpollution.py` - to run the program on your pi.
