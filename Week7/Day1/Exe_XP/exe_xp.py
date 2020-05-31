def main():
    # exe1
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    d = {}
    for x, y in zip(keys, values):
        d[x] = y
    print(d)

    # exe2
    store = {"name": "Zara", "creation_date": 1975,
             "creator_name": "Amancio Ortega Gaona",
             "type_of_clothes": ["men", "women", "children", "home"],
             "international_competitors": ["Gap", "H&M", "Benetton"],
             "number_stores": 7000,
             "major_color": {"France": "blue", "Spain": "red", "US": ["pink", "green"]}}

    store["number_stores"] = 2
    print("{}'s clients are: {}".format(store["name"], ", ".join(store["type_of_clothes"])))
    store["country_creation"] = "Spain"
    if "international_competitors" in store:
        store["international_competitors"].append("desigual")
    del store["creation_date"]
    print(
        "the last international competitor of {} is: {}".format(store["name"], store["international_competitors"][-1]))
    print("the major colors of us are: {}".format(" & ".join(store["major_color"]["US"])))
    print(len(store))

    for x in store:
        print(x)
    more_on_store = {"creation_date": 1975,
                     "number_stores": 10000}
    store.update(more_on_store)
    print(store["number_stores"])


if __name__ == "__main__":
    main()
