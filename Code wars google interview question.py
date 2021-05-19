def get_strings():
    city_name = str.lower("Chicago")
    new_list= []
    

    for letter in city_name:

        counter = 1

        if letter in new_list:
            counter += 1
            letter.replace("*","*"*counter)
            continue 
        elif letter in city_name:
            new_list.append(letter)

        print((":"+("*")+",").join(new_list))

get_strings()
