def hello(**kwargs):  #should not necessarily be named as kwargs, can also be named as big`blackniggaballs
    # print("hello "+kwargs['first']+" "+kwargs['last'])  #first and last is the key here which takes the value from the function  when called
    print("hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
        
hello(first="Sandeep", last="Roy")  #when the function is called a value is reqd to pass to a key to be identified by the kwargs