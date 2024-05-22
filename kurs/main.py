import csv
from matplotlib import pyplot as plt

def sort_arr_by_col(arr, sort_col):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]

        less = [i for i in arr[1:] if int(i[sort_col]) <= int(pivot[sort_col])]
        greater = [i for i in arr[1:] if int(i[sort_col]) > int(pivot[sort_col])]
        return sort_arr_by_col(less, sort_col) + [pivot] + sort_arr_by_col(greater, sort_col)

reader = csv.DictReader(open('shop.csv'))

file = open('shop.csv')
headers = next(file).rstrip().split(',')

entries = []


text = file.readline()
while text != '':
    entries.append(dict(zip(headers, text.rstrip('\n').split(','))))
    text = file.readline()

def get_entry(type_: str, value: str) -> dict:
    for item in entries:
        if item[type_] == value:
            return item

for i in entries:
    print(f"Название товара: {i['Название товара']}\n",
          f"Количество продаж: {i['Количество продаж']}")
    print("Доля в общей выручке: {:.3f}%".format(int(i['Общая стоимость'])
                                             * 100 / sum([int(i['Общая стоимость']) for i in entries])))



print('Общая выручка: ', sum([int(i['Общая стоимость']) for i in entries]))

max_count_sale = sort_arr_by_col(entries, 'Количество продаж')[-1]
print('Товар, который был продан наибольшее количество раз: ',
      max_count_sale['Название товара'], ' - ', max_count_sale['Количество продаж'])

max_sale = sort_arr_by_col(entries, 'Общая стоимость')[-1]
print('Товар, который принес наибольшую выручку: ',
      max_sale['Название товара'], ' - ', max_sale['Общая стоимость'])


#############matplotlib###############################
index = [i['Название товара'] for i in entries]
values = [int(i['Количество продаж']) for i in entries]
plt.figure(figsize=(20,10), num='Количество продаж всех товаров')
plt.barh(index,values)
plt.yticks(fontsize=4)
plt.show()


index = [i['Название товара'] for i in entries]
values = [int(i['Общая стоимость']) for i in entries]
plt.figure(figsize=(20,10), num='Общие выручки всех товаров')
plt.barh(index,values)
plt.yticks(fontsize=4)
plt.show()

labels = [f"самый продаваемый товар\nв сравнении с общим кол-ом\nпродаж:\n {max_count_sale['Название товара']}",'Другое']
values = [max_count_sale['Количество продаж'],
          sum([int(i['Количество продаж']) for i in entries]) - int(max_count_sale['Количество продаж'])]
colors = ['yellow','grey']
plt.figure(figsize=(20,10), num='Соотношение самого продаваемого товара с общим кол-вом')
plt.pie(values,labels=labels,colors=colors)

plt.axis('equal')
plt.show()


labels = [f"Товар который\nпринес наибольшую выручку:\n  {max_sale['Название товара']}",'Другое']
values = [max_sale['Общая стоимость'],
          sum([int(i['Общая стоимость']) for i in entries]) - int(max_sale['Общая стоимость'])]
colors = ['lightgreen','pink']
plt.figure(figsize=(20,10), num='Соотношение товара, принесшего наибольшую выручку с дургими')
plt.pie(values,labels=labels,colors=colors)

plt.axis('equal')
plt.show()


