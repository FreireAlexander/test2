"""
Just imagine that we have already prepared lists of articles that are similar.  You can see an example below: 
Retrieve an article in PubMed: https://pubmed.ncbi.nlm.nih.gov/ 
Click on the desired record to display the Abstract view. 
Examine links to Related Articles, including Reviews, on the right side of the page, or click "See all" to display all related records. 

https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed&from_uid=33400058 
you can see that: 
PMID: 33400058 (Recent Developments on Therapeutic and Diagnostic Approaches for COVID-19) 
has the following similar articles: 
33400058: [32889088, 32935333, 33261606, 33781287, 33334802, 33070079, etc.] (623 results) 
https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed&from_uid=33070079 
33070079: [34276652, 33371468, etc.] 
. . .  
The task is to find all 2‑tuple (ordered pair or couple) for the given lists. For simplification just let’s have the following: 
similar_ids = { 
    123: [458, 812, 765], 
    458: [123, 812, 765], 
    812: [123, 458], 
    765: [123, 458], 
    999: [100], 
    100: [999] 
}
The expected result will be: 
expected = { 
    (123, 458), (123, 812), (123, 765), (458, 812), (458, 765), (100, 999) 
}
The tuples are ordered and appear only once, so if you have (123, 458) the (458, 123) is not possible. 
Please write a program on Python. You can put a link to your code (https://pastebin.com/ for example or a link to GitHub, GitLab, etc.).
The scripts which are not working wouldn't be evaluated. Any comments are also welcome.
The extra points will be given if you write tests for different input and outputs and if you follow PEP8.
"""
def find_ordered_pairs(similar_ids):
    ordered_pairs = set()
    for article_id, related_ids in similar_ids.items():
        for related_id in related_ids:
            if article_id < related_id:
                ordered_pairs.add((article_id, related_id))
            else:
                ordered_pairs.add((related_id, article_id))
    return ordered_pairs


# Test the function with the provided example
similar_ids = {
    123: [458, 812, 765],
    458: [123, 812, 765],
    812: [123, 458],
    765: [123, 458],
    999: [100],
    100: [999]
}

expected = {
    (123, 458), (123, 812), (123, 765),
    (458, 812), (458, 765), (100, 999)
}

result = find_ordered_pairs(similar_ids)

print("Expected Result:", expected)
print("Actual Result:  ", result)
print("Test Passed:", result == expected)
