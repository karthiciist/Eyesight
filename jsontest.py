import json

json_string = '{"1": {"xaxis": "1","yaxis": "2","width": "3","height": "4","rotate": "5","scalex": "6","scaley": "7","lable": "8","text": "9"}, "2": {"xaxis": "1","yaxis": "2","width": "3","height": "4","rotate": "5","scalex": "6","scaley": "7","lable": "8","text": "9"}, "3": {"xaxis": "1","yaxis": "2","width": "3","height": "4","rotate": "5","scalex": "6","scaley": "7","lable": "8","text": "9"}}'
json_dictionary = json.loads(json_string)
for key in json_dictionary:
    indi = json_dictionary[key]
    for key1 in indi:
        print(key1, ":", indi[key1])
    print("--------------------")