import urllib.request
import json

def print_results(data):
    # use the json module to load the string data into dictionary
    the_json = json.loads(data)

    # access the content of the JSON like any other Python object
    if "title" in the_json["metadata"]:
        print(the_json["metadata"]["title"])
        print("--------------\n")

    # output the number of events, plus the magnitude and each event name
    count = the_json["metadata"]["count"]
    print(str(count) + " events recorded")
    print("--------------\n")

    # for each event, print the place where it occurred
    for i in the_json["features"]:
        print(i["properties"]["place"])
    print("--------------\n")

    # print the events that only have a magnitude greater than 4
    for i in the_json["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("--------------\n")

    # print only the events where at least 1 person reported feeling something
    print("Events that were felt:")
    for i in the_json["features"]:
        felt_reports = i["properties"]["felt"]
        if felt_reports is not None:
            if felt_reports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
                      'reported ' + str(felt_reports) + " times")


def main():
    # define a variable to hold the source URL
    url_data = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # open the URL and read the data
    web_url = urllib.request.urlopen(url_data)
    print("result code: " + str(web_url.getcode()))
    print("--------------\n")

    if  web_url.getcode() == 200:
        data = web_url.read()
        print_results(data)
    else:
        print("receive error")

if __name__ == '__main__':
    main()