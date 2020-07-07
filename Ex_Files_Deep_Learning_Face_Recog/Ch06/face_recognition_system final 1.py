#loops through all the .jpg files in the directory and checks against person_1, person_2, person-3
#unknown_5.jpg also has three faces, but algorithm could identify only persons 1 & 3.
#unknown_7.jpg is too small to detect faces with this code

import face_recognition
import os

# Load the known images
image_of_person_1 = face_recognition.load_image_file("person_1.jpg")
image_of_person_2 = face_recognition.load_image_file("person_2.jpg")
image_of_person_3 = face_recognition.load_image_file("person_3.jpg")

# Get the face encoding of each person. This can fail if no one is found in the photo.
person_1_face_encoding = face_recognition.face_encodings(image_of_person_1)[0]
person_2_face_encoding = face_recognition.face_encodings(image_of_person_2)[0]
person_3_face_encoding = face_recognition.face_encodings(image_of_person_3)[0]

# Create a list of all known face encodings
known_face_encodings = [
    person_1_face_encoding,
    person_2_face_encoding,
    person_3_face_encoding
]

# Load the image we want to check, loop through the directory for all .jpg files
directory = r'.'
for unknown_file in os.listdir(directory):
    # .jpg filter
    if unknown_file.endswith(".jpg"):
        print(f"Checking {unknown_file}")
        unknown_image = face_recognition.load_image_file(unknown_file)

        # Get face encodings for any people in the picture
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)

        # print(f" Length : {len(unknown_face_encodings)}")
        if len(unknown_face_encodings) > 1:
            print(f"{unknown_file} has multiple faces!!!!")

        # There might be more than one person in the photo, so we need to loop over each face we found
        for unknown_face_encoding in unknown_face_encodings:

            # Test if this unknown face encoding matches any of the three people we know
            results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, tolerance=0.6)



            #print(f" Length : {len(unknown_face_encoding)}")
            #print(f"{results[0]}")
            name = unknown_file

            if results[0]:
                name = "Person 1"
            elif results[1]:
                name = "Person 2"
            elif results[2]:
                name = "Person 3"

            print(f"Found {name} in the photo {unknown_file}!")