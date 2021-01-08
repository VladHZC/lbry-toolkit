#!/usr/bin/env python
import json
import requests

# LBRY JSON RPC URL
HOST = "http://localhost:5279"

# Do a claim list
response = requests.post(HOST, json={"method": "claim_list",
                                     "params": {}}).json()

f = open("vanity_names_output.txt", "w")

# Get the number of claims
num_claims = response["result"]["total_items"]

def write(s, end="\n", flush=False):
    """
    Write a string to stdout and the file
    """
    print(s, end=end, flush=flush)
    f.write(s)
    f.write(end)
    if flush:
        f.flush()

# Get the claim info
write(f"You have {num_claims} claims.")
write("Getting claim information. This might take a while...",
      flush=True, end="")
response = requests.post(HOST,
                         json={"method": "claim_list",
                               "params": {"page_size": num_claims,
                                          "resolve":   True}}).json()
claims = response["result"]["items"]
write("done.", end="\n\n", flush=True)

for claim in claims:

    claim_id = claim["claim_id"]

    # Vanity name and whether you're controlling it
    vanity_name = claim["name"]
    controlling = claim["meta"]["is_controlling"]
    staked_amount = float(claim["amount"]) + float(claim["meta"]["support_amount"])

    # Get multiplicity of the vanity name, and max LBC
    max_lbc = None
    response = requests.post(HOST,
                     json={"method": "claim_search",
                           "params": {"name": vanity_name}}).json()
    multiplicity = response["result"]["total_items"]
    response = requests.post(HOST,
                     json={"method": "claim_search",
                           "params": {"name": vanity_name,
                                      "page_size": multiplicity}}).json()

    competitors = 0
    for item in response["result"]["items"]:

        # Look at staked LBC
        item_lbc = float(item["amount"]) + float(item["meta"]["support_amount"])
        if item["claim_id"] != claim_id and \
                (max_lbc is None or item_lbc > max_lbc):
            max_lbc = item_lbc

        # Count competitors
        if (item["value_type"] != "repost" and item["claim_id"] != claim_id)\
                or ("reposted_claim_id" in item and \
                    item["reposted_claim_id"] == claim_id):
            competitors += 1

    # Print some information
    write("-------------------------------------------------------------------")
    write(f"Name: {vanity_name}")
    write("-------------------------------------------------------------------")
    write(f"Do you control it?: {'YES' if controlling else 'NO'}")
    write(f"Number of competing claims, excluding reposts of your claim: {competitors}")
    write(f"LBC on your claim: {staked_amount}")
    write(f"Maximum LBC on competing claims: {max_lbc}")
    if claim["value_type"] == "repost":
        write("This is a repost made by you, so you might not care anyway.")
    if max_lbc is not None:
        if controlling and max_lbc > staked_amount:
            write("TAKEOVER WARNING!")
        if not controlling and staked_amount > max_lbc:
            write("YOUR CLAIM HAS ENOUGH LBC BUT IS WAITING FOR TAKEOVER.")
    write("", end="\n\n", flush=True)

f.close()
print("Output saved to vanity_names_output.txt")


