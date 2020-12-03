from openpyxl import load_workbook

def get_graduates_list(fpath, fields_columns: dict):
    wb = load_workbook(fpath)
    sheet = wb['Sheet1']

    items = []
    ind = 1

    while (True):
        item = {k: sheet[v.format(ind)].value for k, v in fields_columns.items()}

        if not None in item.values():
            items.append(item)
        else:
            break

        ind += 1

    return items