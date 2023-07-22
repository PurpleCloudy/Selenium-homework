import csv

def append_csv(rows:list) -> None:
  for row in rows:
    with open('data.csv', 'a') as file:
      writer = csv.writer(file)