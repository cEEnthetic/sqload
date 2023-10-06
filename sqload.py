def is_string(stri: str):
    if stri.count(".") > 1:
        return True
    if stri.replace(".", "").isnumeric():
        return False
    return True


def to_sql(path: str, separator=",", encoding="utf-8", table_name="", column_names=tuple()):
    file = open(path, "r", encoding=encoding)
    rows = file.read().splitlines()

    if not table_name:
        table_name = path.split("/")[-1][::-1] #string reversed because the file format has the last "."
        table_name = table_name[table_name.find(".")+1:][::-1] #reversing it back and trimming file format

    if not column_names:
        column_names = tuple(rows.pop(0).split(separator))

    records = "INSERT INTO " + table_name + str(column_names).replace("'", "") + " VALUES "
    for row in rows:
        row_data = row.split(separator)
        for data_i in range(len(row_data)):
            if not is_string(row_data[data_i]):
                row_data[data_i] = int(row_data[data_i])

        records += (str(tuple(row_data))) + ","
    records = records.rstrip(",") + ";"
    print(records)


to_sql("cucc/emberek.txt")
