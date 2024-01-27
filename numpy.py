import numpy as np

#function to replace the maximum value in an array of axis x and y based on the condition
def replace_maxmium(array, replace_value, axis):
    result = np.where(array == np.max(
        array, axis=1).reshape(-1, 1), 0 * array, array)
    print(result)


def main():

 #creating a random vector of size 29 which is having in the range of 1-20
    rand20 = np.random.random_sample(20) * 20 + 1
    print(rand20)
    
    #reshaping the array to 4 by 5 in random20
    rand20_4by5 = rand20.reshape((4, 5))
    print(rand20_4by5)

    replace_maxmium(rand20_4by5, 0, 1)#replacing the max value in each row by zero


if __name__ == "__main__":
    main()