import os

def read_file(filename):
    # backslash = "\\"
    filepath = "data\\"
    filepath += filename + '.txt'
    # f = open(filepath, "r")

    info = []

    # lists = f.readlines()
    
    with open(filepath, "r") as fd:
        for line in fd:
            line = line.replace("\r", "").replace("\n", "")

            info.append(str(line))

    # f.close()
    return info


def write_to_file(filename, lst):
    subdirectory = "queries" 
    filename += '.txt'
    with open(os.path.join(subdirectory, filename), 'w') as filehandle:
        for query in lst:
            filehandle.write("%s\n" % query)
    print('queries written to ' + filename)



if __name__ == '__main__':
    lst_author_name = read_file('author_name')
    lst_author_no = read_file('author_no')
    lst_city = read_file('cust_city')
    lst_country = read_file('country')
    lst_cust_addr = read_file('cust_addr')
    lst_cust_company = read_file('cust_company')
    lst_cust_fname = read_file('cust_fname')
    lst_cust_id = read_file('cust_id')
    lst_cust_lname = read_file('cust_lname')
    lst_isbn = read_file('isbn')
    lst_odate = read_file('odate')
    lst_order_no = read_file('order_no')
    lst_pub_addr = read_file('pub_addr')
    lst_pub_year = read_file('pub_year')
    lst_publisher_name = read_file('publisher_name')
    lst_publisher_no = read_file('publisher_no')
    lst_qty = read_file('qty')
    lst_title = read_file('title')
    lst_unit_price = read_file('unit_price')    
    lst_year = read_file('year')
    lst_cust_phone = read_file('cust_phone')

    for author_name in lst_author_name:
        print(author_name)

    
     
    # author queries
    
    # assert(len(lst_country) == len(lst_author_no) == len(lst_author_name))
    initial_query = "insert into author values("
    query = ""
    sym = '"'
    comma = ','
    queries_lst = list()

    print("author queries... \n")
    for author_no, author_name, country in zip(lst_author_no, lst_author_name, lst_country):
        query = initial_query + str(author_no) + comma
        query += sym + str(author_name) + sym + comma
        query += sym + str(country) + sym
        query += ');'

        queries_lst.append(query)
        print(query)

    write_to_file('queries_author', queries_lst)

    # book queries
    # assert(len(lst_isbn) == len(lst_title) == len(lst_unit_price) == len(lst_publisher_no) == len(lst_pub_year))
    initial_query = "insert into book values("
    query = ""
    sym = '"'
    comma = ','
    queries_lst = list()

    print("\nbook queries...")
    for isbn, title, unit_price, author_no, publisher_no, pub_year in zip(lst_isbn, lst_title, lst_unit_price, lst_author_no ,lst_publisher_no, lst_pub_year):
        query = initial_query + str(isbn) + comma
        query += sym + str(title) + sym + comma
        query += str(unit_price) + comma
        query += str(author_no) + comma
        query +=  str(publisher_no) + comma
        query += str(pub_year)
        query += ');'

        print(query)
        queries_lst.append(query)

    write_to_file('queries_book', queries_lst)
    for query in queries_lst:
        print(str(query))
    
    # orders queries
    # assert(len(lst_isbn) == len(lst_title) == len(lst_unit_price) == len(lst_publisher_no) == len(lst_pub_year))
    initial_query = "insert into orders values("
    query = ""
    sym = '"'
    comma = ','
    queries_lst = list()

    print("\norders queries...")
    for order_no, cust_no, isbn, qty, odate in zip(lst_order_no, lst_cust_id, lst_isbn, lst_qty ,lst_odate):
        query = initial_query + str(order_no) + comma
        query += str(cust_no) + comma
        query += str(isbn) + comma
        query += str(qty) + comma
        query += sym + str(odate) + sym
        query += ');'

        print(query)
        queries_lst.append(query)

    write_to_file('queries_orders', queries_lst)
    
    # publisher queries
    initial_query = "insert into publisher values("
    query = ""
    sym = '"'
    comma = ','
    queries_lst = list()

    print("\nqueries publisher..")
    for publisher_no, publisher_name, publisher_addr, year in zip(lst_publisher_no, lst_publisher_name, lst_pub_addr, lst_year):
        query = initial_query + str(publisher_no) + comma
        query += sym + str(publisher_name) + sym + comma
        query += sym + str(publisher_addr) + sym + comma
        query += str(year)
        query += ');'

        print(query)
        queries_lst.append(query)

    write_to_file('queries_publisher', queries_lst)

    # customer queries
    initial_query = "insert into customer values ( "
    query = ""
    sym = '"'
    comma = ' , '
    queries_lst = []
    for id_name, fname, lname, company, addr, city, phone in zip(lst_cust_id, lst_cust_fname, lst_cust_lname, lst_cust_company, lst_cust_addr, lst_city, lst_cust_phone):
        query = initial_query + id_name +  comma
        query += sym + fname + sym + comma
        query += sym + lname + sym + comma
        query +=  sym + company + sym + comma
        query +=  sym + addr + sym + comma
        query +=  sym + city + sym + comma
        query +=  sym + phone + sym
        query += ');'

        print(query)
        queries_lst.append(query)

    write_to_file('queries_customer', queries_lst)
    