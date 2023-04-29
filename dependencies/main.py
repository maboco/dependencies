import requests
import argparse
import json
from Models.query import Query
from Models.package import Package

def args():
    parser = argparse.ArgumentParser(prog="Dependencies", description="Check requirements.txt vulns on OSV and PyPi ")
    parser.add_argument("-f", "--file", help="Specify path requirements.txt", required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = args()
    path = args.file

    
    url_pypi = ""
    url_osv  = "https://api.osv.dev/v1/querybatch"

    query = Query()

    with open(path, "r") as file:
        for package in file:
            name, version = package.strip().split("==")
            query.set_package(Package(name, version).get_combine())
    
    print(query.get_query())

    response = requests.request("POST", url=url_osv, data=json.dumps(query.__dict__))

    
    print(response.text)

    



    

