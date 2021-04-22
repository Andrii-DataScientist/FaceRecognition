# Repeated-course Face Recognition
IT STEP University detection joke, Made by curators of university DataScienceClub: Andrii Varenytsia, Max Zhytnikov, Vitaliy Povstenko 
**Some notes:**
- As we know, predict by picture of student's face will the particular student will have the repeated course at the end of semester is unreal:D
- So we make simple steps, take about 30 pictures(of maybe 5-10 special people, for example on developers of this bot) on whom the model will always give "Survived" result and about 500+ pictures with faces of random people who will get the repeated course
- Our Keras model was learnt on two classes, and the output from prediction is a numpy array with 2 numbers that are floating between 0 and 1
- We were interested on the first number, which means if the first number is -> about 0, it means that the face is not similar to the special 5-10 people who should always get survive, so this person will get -> 'Повторний курс', otherwise if the first number is about 1, so it means that his face is similar to faces of special people and will get result from the bot -> 'Survived'.
