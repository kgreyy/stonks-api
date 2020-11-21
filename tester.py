from stockapi import *
from time import sleep

def massRip(formCode, recent=None):
    if recent is None:
        recent = True
    logger = {}
    for x in CompanyDir().listing:
        sleep(1)
        comp = Company(x["companyID"],cons=True)
        sleep(1)
        stuff = comp.parseDisclosures(comp.getDisclosureByPageNum(1)) if recent else comp.getDisclosures()
        for disc in stuff:
            if disc["formNumber"] == formCode:
                print(formCode+" found!")
                logger[comp.compID] = comp.downloadDisclosure(disc["edge_no"])
                break
        if len(stuff) == 0:
            print(x + " has no data.")
    return logger

def main():
    with open('log.txt','w+',encoding='utf-8') as f:
        f.write(str(massRip("", recent=True))) # POR-1 and 17-12
