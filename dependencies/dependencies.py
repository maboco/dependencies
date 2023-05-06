import requests
import argparse
import json
from Models.query import Query
from Models.package import Package

def args():
    parser = argparse.ArgumentParser(prog="Dependencies", description="Check requirements.txt vulns on OSV and PyPi ")
    parser.add_argument("-f", "--file", help="Specify path requirements.txt", required=True)
    parser.add_argument("-s", "--simple", action='store_true', help="Simple output", required=True)
    args = parser.parse_args()
    return args

def spaces():
        print("")
        print("------------------------------------------------------------------------------------")

def simple(pack):
    query = Query()

    for pack in packs:
        query.set_package(pack.get_osv_format())
    
    url_osv  = "https://api.osv.dev/v1/querybatch"
    
    response_osv = requests.request("POST", url=url_osv, data=json.dumps(query.__dict__)).json()

    for i in range(len(packs)):
        p = packs[i].get_pack() | response_osv["results"][i]
        p["url"] = "https://pypi.org/project/"+p['name']+"/"+p['version']

        print(p['name']+"/"+p['version']+" - "+p["url"])

        if "vulns" in p:
            for vuln in p["vulns"]:
                if "GHSA" in vuln["id"]:
                    print(vuln["id"]+" ---- https://github.com/advisories/"+vuln["id"])
                else:
                    print(vuln["id"]+" ---- hhttps://osv.dev/vulnerability/"+vuln["id"])
        else:
            print("No vulnerabilities")
        
        spaces()
        

def complex():
    # TODO: add full size outputs
    pass

if __name__ == "__main__":
    args = args()
    path = args.file
    mode = args.simple

    packs = []

    with open(path, "r") as file:
        for package in file:
            if "#" not in package:
                name, version = package.strip().split("==")
                pack = Package(name, version)
                packs.append(pack)

    if mode:
        simple(packs)
    else:
        complex()
            
    
    



    

