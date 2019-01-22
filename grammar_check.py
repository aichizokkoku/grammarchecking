from gingerit.gingerit import GingerIt

def main():
  input_text = input("input: ")
  #print(input_text)

  parser = GingerIt()
  json = parser.parse(input_text)
  #print(json)

  if (not json["corrections"]):
    print("All correct!")
  else:
    #なぜかしらないけど、最後の文字が出力されないからタス分類
    lastword = ""
    lastword = json["result"]
    if (lastword[-1] == input_text[-1]):
      print(lastword)
    else:
      print(lastword + input_text[-1])


if __name__ == '__main__':
    main()
