def remove_every_other(my_list):
    # Your code here!
    # just make a list of every even index

    return [my_list[index] for index in range(0, len(my_list)) if index % 2 == 0]
    
   




test.assert_equals(remove_every_other(['Hello', 'Goodbye', 'Hello Again']),
                   ['Hello', 'Hello Again'])
test.assert_equals(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
                   [1, 3, 5, 7, 9])
test.assert_equals(remove_every_other([[1, 2]]), [[1, 2]])
test.assert_equals(remove_every_other([['Goodbye'], {'Great': 'Job'}]),
                   [['Goodbye']])
