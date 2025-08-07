try:
    with open("C:\\Users\\sande\\OneDrive\\Desktop\\DysonSphere\\ML\\PythonCourseYT\\test.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found. Please check the file path.")