text = input("Enter text to write to file: ")

try:
    with open("C:\\Users\\sande\\OneDrive\\Desktop\\DysonSphere\\ML\\PythonCourseYT\\test.txt", "w") as file:
        file.write(text)
        print("File written successfully.")
        with open("C:\\Users\\sande\\OneDrive\\Desktop\\DysonSphere\\ML\\PythonCourseYT\\test.txt", "r") as file:
            print(file.read())
        print("File read successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
    