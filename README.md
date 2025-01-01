# Live-Facial-Recognition-
Python program that allows for live facial recognition given a data set with images and names.

# Instructions
1. Open up the project file
2. Add images of the people you want the webcam to scan for into the "people" directory
3. Pip install open-cv, deepface, threading
4. Run the program

# Math & How it Works
The deepface libary processes an image using: Convolutional Neural Networks (CNNs) <br />
CNN analyzes the image and extract high-level features, such as the shape of the nose, eyes, and other facial structures. <br />
These features are converted into a numerical representation called an embedding or feature vector.<br />
Each face is represented as a vector in a high-dimensional space (e.g., a 128-dimensional vector for many models).
Mathematically, this is: <br />
### embedding = f(inputIMG)

![image](https://github.com/user-attachments/assets/bf8b07c2-418e-4b8e-85ec-16e2ec7c5188)

These formulas are used to compute the distances between the embeddings of the reference and the live image.
The computed distance is then compared to the threshold and if the number is below the threshold then the program will return a match.
Thresholds are selected based on loss functions and training and validation phases. Thresholds are chosen to maximize perfomance, often at the point where the false acceptance rate and false rejection rate are balanced.
## Example
### Reference image v_1: [0.2, 0.5, 0.8,...]
### Live input feed v_2: [0.3, 0.6, 0.7,..]
![image](https://github.com/user-attachments/assets/5f332022-5af0-4c4b-84b5-7f15dbc7aae3)

1. Image data is first converted into data points
2. The points are then fed into a distance formula.
3. The distance computed is 0.173. Let's assume that the threshold is 0.2.
4. Since 0.173 < 0.2, the program returns that the person being scanned is a match with one in the database.
