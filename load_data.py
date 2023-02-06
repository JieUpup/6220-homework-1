

file_list = ["combined_data_1.txt", "combined_data_2.txt", "combined_data_3.txt", "combined_data_4.txt"]

total_record = 0
'''
- MovieIDs range from 1 to 17770 sequentially.
- CustomerIDs range from 1 to 2649429, with gaps. There are 480189 users.
- Ratings are on a five star (integral) scale from 1 to 5.
- Dates have the format YYYY-MM-DD.
'''
#r_a = np.array()
#d_a = np.array()
output = []
output.append("movie_id,user_id,rate,date")

for file in file_list:
    file_name = "archive/" + file
    f = open(file_name)
    for line in f.readlines():
        arr = line.split(',')
        movie_id = 0
        if len(arr) < 3:
            movie_id = line.split(':')[0]
            #movie_id = int(movie_id)
            #if movie_id < 1 or movie_id > 17770:
            #    print(str(movie_id) + "is invalid")
        else:
            total_record += 1
            userId = int(arr[0])
            # 1 to 2649429
            if 1 > userId or userId > 2649429:
                print(line + "has invalid userId")
            rating = int(arr[1])
            #np.append(r_a, rating)

            if 0 > rating or rating > 5:
                print(line + "has invalid rating")

            date_str = arr[2]
            output.append(str(movie_id) + "," + line)

            #np.append(d_a, date_str)
            #try:
            #    date_object = datetime.strptime(date_str, '%Y-%m-%d').date()
            #except:
            #    print(line + "has invalid date")



print(total_record)

output_file = "data.csv"
dfile = open(output_file, "w")
dfile.writelines(output)
dfile.close()