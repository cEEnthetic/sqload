def is_string(stri: str):
    ''' Check if the input needs the "" in sql syntax.'''
    if stri.count(".") > 1:
        # If the input has more than one ".", then it must be a date, so it needs the "".
        return True
    if stri.replace(".", "").isnumeric():
        return False
    return True


def to_sql(path: str, separator=",", encoding="utf-8", table_name="", column_names=tuple()) -> str:
    # Column name is tuple, because it is easy to format into sql syntax.
    file = open(path, "r", encoding=encoding)
    rows = file.read().splitlines()

    if not table_name:  # Using the filename as default.
        table_name = path.split("/")[-1][::-1]  # String reversed because the file format must have the last "."
        table_name = table_name[table_name.find(".")+1:][::-1]

    if not column_names:  # Using the first row of the file as default.
        column_names = tuple(rows.pop(0).split(separator))

    records = "INSERT INTO " + table_name + str(column_names).replace("'", "") + " VALUES "
    for row in rows:
        # Using data_i(index) because we need the index of the value we want to replace.
        row_data = row.split(separator)
        for data_i in range(len(row_data)):
            if not is_string(row_data[data_i]):
                row_data[data_i] = int(row_data[data_i])
        records += (str(tuple(row_data))) + ","

    records = records.rstrip(",") + ";"
    # We need a ; at the end of an sql INSERT function.
    file.close()
    return records


print(to_sql("cucc/emberek.txt"))
