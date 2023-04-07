# Movie_Recommender_System

Movie recommendation system using the K-nearest neighbors (KNN) algorithm and and natural language processing (NLP) techniques, specifically the bag-of-words technique for feature extraction. The system takes input from the user in the form of a movie title and recommend similar movies based on the genre, cast, and director, and other features extracted from their synopsis.

The KNN algorithm is used to identify the K-nearest movies to the input movie in terms of feature similarity. The bag-of-words technique is applied to extract features from the movie dataset, where each movie synopsis is represented as a set of words, which are then used to calculate the similarity between movies.


# KNN Algorithm

The K Nearest Neighbor algorithm is classified as supervised learning and is commonly used for classification and regression. It is a versatile algorithm that can also be used to impute missing values and resample datasets. The nearest neighbours are those data points that are the shortest distance away in feature space from our new data point. And K is the number of such data points that we consider in our algorithm implementation. As a result, the distance metric and K value are two critical considerations when employing the KNN algorithm.



For Project datasets (TMDb 5000 movie datasets) are downloaded from kaggle.com. Datasets contains information about 5000 movies.


![movie](https://user-images.githubusercontent.com/83577844/226948187-ad5abcbf-0c77-49c0-87eb-d0222443078e.jpg)
