# Live-Facial-Recognition-
Python program that allows for live facial recognition given a data set with images and names.

# Instructions
1. Open up the project file
2. Add images of the people you want the webcam to scan for into the "people" directory
3. Pip install open-cv, deepface, threading
4. Run the program

# Math
![image](https://github.com/user-attachments/assets/bf8b07c2-418e-4b8e-85ec-16e2ec7c5188)

These formulas are used to compute the distances between the embeddings of the reference and the live image.
The computed distance is then compared to the threshold and if the number is below the threshold then the program will return a match.
Thresholds are selected based on loss functions and training and validation phases. Thresholds are chosen to maximize perfomance, often at the point where the false acceptance rate and false rejection rate are balanced.
## Example
### Reference image v_1: [0.2, 0.5, 0.8,...]
### Live input feed v_2: [0.3, 0.6, 0.7,..]
![image](https://github.com/user-attachments/assets/5f332022-5af0-4c4b-84b5-7f15dbc7aae3)

Image data is first converted into data points
The points are then fed into a distance formula.
The distance computed is 0.173. Let's assume that the threshold is 0.2.
Since 0.173 < 0.2, the program returns that the person being scanned is a match with one in the database.
