from Student import Student
studentlist = []
while True:
     print(f'''\n
          ======Manager Student System====
          0. Exit
          1. Add student
          2. Update information of student
          3. Delete student
          4. Show all student
          5. Show student by id
          6. Search student by name
          7. Count all student
           ''')
     select = int(input('Enter your choice: '))
     if str(select).isdigit():
          select = int(select)
          if select == 0:
               break
          elif select == 1:
               print("You had selected to add a student")
               id = input('Enter student id: ')
               name = input('Enter student name: ')
               BirthOfDate = input('Enter student Birth of date: ')
              # age = time.localtime - BirthOfDate
               address = input('Enter student address: ')
               phone = input('Enter student phone: ')
               DTB = input('Enter student DTB: ')
               sv = Student(id, name,BirthOfDate,address,phone,DTB)
               studentlist.append(sv)
               sv.show(studentlist)
          elif select == 2:
               print("You had selected to update information of student")
               id = input('Enter student id you need to update: ')
               for i in studentlist:
                    if i.get_id() == id:
                         while True:
                              print(f'''\n
                              ====Choose one of the following options====
                              0. Exit
                              1. Update Name of student
                              2. Update Birth of date of student
                              3. Update Address of student
                              4. Update Phone of student
                              5. Update DTB of student
                              ''')
                              choice = int(input('Enter your choice: '))
                              if str(choice).isdigit():
                                   choice = int(choice)
                                   if choice == 0:
                                        break
                                   if choice == 1:
                                        i.set_Name(input('Enter student name: '))
                                   if choice == 2:
                                        i.set_BirthOfDate(input('Enter student Birth of date: '))
                                   if choice == 3:
                                        i.set_Address(input('Enter student address: '))
                                   if choice == 4:
                                        i.set_Phone(input('Enter student phone: '))
                                   if choice == 5:
                                        i.set_DTB(input('Enter student DTB: '))
                              else:
                                   print("You must enter a number! Please try again")
                         i.show(studentlist)
                    elif i.get_id() == False:
                         print('Student have {} not found!'.format(id))
          elif select == 3:
               print("You had selected to delete student")
               id = input('Enter student id you need to delete: ')
               for i in studentlist:
                    if i.get_id() == id:
                         studentlist.remove(i)
                         print('Delete Successful!')
                         continue
          elif select == 4:
               if len(studentlist) == 0:
                    print('\nThere has no student in the system!')
               else :
                    print(f'\nThere has {len(studentlist)} student in the system')
                    for i in studentlist:
                         i.show(studentlist)
          elif select == 5:
               id = input('Enter student id you need to watch: ')
               for i in studentlist:
                    if i.get_id() == id:
                         i.show(studentlist)
                         continue
          elif select == 6:
               while True:
                    print(f'''
                          Choose method to search:
                          0.exit
                          1. Search Name
                          2. Search ID
                          ''')
                    choice = int(input('Enter your choice: '))
                    if str(choice).isdigit():
                         choice = int(choice)
                         if choice == 0:
                              break
                         if choice == 1:
                              name = input('Enter student name you need to search: ')
                              for i in studentlist:
                                   if i.get_Name() == name :
                                        i.show(studentlist)
                                   elif i.get_Name() == False:
                                        print('Student have name is {} not found!'.format(name))
                         if choice == 2:
                              id = input('Enter student id you need to search: ')
                              for i in studentlist:
                                   if i.get_id() == id:
                                        i.show(studentlist)
                                   elif i.get_id() == False:
                                        print('Student have id is {} not found!'.format(id))
                    else:
                         print("\n You must enter a number!Please try again!")
                         

          elif select == 7:
               print(f'\nThere has {len(studentlist)} student in the system') 
     else :
          print("\n You must enter a number! Please try again")
