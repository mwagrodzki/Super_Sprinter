import csv

def export_data(data_base):
    with open("data.csv", "w") as f:
        fields = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']

        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for key, val in sorted(data_base.items()):
            row = {'id': key}
            row.update(val)
            writer.writerow(row)


def import_data():
    dictionary = {}
    fields = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
    rows = []
    index = 0
    with open("data.csv", "r") as f:
        reader = csv.reader(f)

        for line in reader:
            if index > 0:
                rows.append(line)
            index += 1

    for row in rows:
        for i, field in enumerate(fields):
            if field == 'id':
                dictionary[row[0]] = {}
            else:
                dictionary[row[0]][field] = row[i]

    return dictionary