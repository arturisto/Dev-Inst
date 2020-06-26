import json


def main():
    # exe 1
    with open("exe1.json", "r") as f:
        data = json.load(f)
        print(data["company"]["employee"]["payble"]["salary"])

    # exe1
    with open("exe2.json", "w") as f:
        sampleJson = {"id": 1, "name": "value2", "age": 29}
        dict_keys  = sampleJson.keys()
        dict_keys = sorted(dict_keys)
        new_dict = {}
        for key in dict_keys:
            new_dict[key] = sampleJson[key]
        json.dump(new_dict, f)


if __name__ == "__main__":
    main()
