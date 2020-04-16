import pandas as pd


def open_file(file_name):  # @ToDO -> Try catch
    # Return the named file
    print("\nOpening File...")
    file = pd.read_excel(file_name)
    print("\nReturning File...")
    return file


if __name__ == '__main__':  # @ToDo -> try catch
    base_query = 'INSERT INTO sku_category (sku_id, category_id, main, last_updated, date_created) VALUES '  # Base query
    base_value = '({0}, 15199, 1, now(), now())'  # Base values of insert
    sql_file = open("insert.sql", "x")  # Create / Open the insert.sql (where we'll save the query
    sql_file.write(base_query)  # Write the base query into the insert.sql
    df = open_file('no_category.xlsx')  # Open file
    number_of_rows = df.shape[0]  # Get the number of rows in the dataframe
    print("\n Generating the Query...")
    for index, row in df.iterrows():  # Looping all rows
        sql_file.write(base_value.format(row['sku_id']))  # writing the column 1
        sql_file.write(',\n')
        sql_file.write(base_value.format(row['sku_id.1']))  # writing the column 2
        if index != number_of_rows - 1:  # check if isn't the last row
            sql_file.write(',\n')  # and if isn't, put the ',' (because there's more lines to add)
    sql_file.write(';')  # write the ; in the final of the sql_file
    sql_file.close()  # close the sql file (important)
    print("\nQuery generated...")  # message that the query was generated
