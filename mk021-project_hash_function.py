# HASH FUNCTION PROJECT

# Given a keyword, the hash function will tell where to look in the index.
# It will map the keyword to a number(takes in a keyword and outputs a number)
# which is the position in the index where you should look for the keyword.
# This means we don't have to start at the beginning and look all the way
# through the index to find the keyword we are looking for making the search
# process faster.


def hash_table_update(hash_table, keyword, value):
    """
    Updates the value associated with key. If key is already in the table,
    changes the value to the new value. Otherwise add a new entry for the
    key and value.
    """
    # for entry in hash_table_get_bucket(hash_table, keyword):
    #     if entry[0] == keyword:
    #         entry[1] = value
    entry = hash_table_lookup(hash_table, keyword)
    if entry:
        entry = value
    else:
        hash_table_add(hash_table, keyword, value)


def hash_table_lookup(hash_table, keyword):
    """
    Takes two inputs, a hash_table and a keyword (string),
    and returns the value associated with that keyword.
    If the key is not in the table, outputs None.
    """
    for entry in hash_table_get_bucket(hash_table, keyword):
        if entry[0] == keyword:
            return entry[1]


def hash_table_add(hash_table, keyword, value):
    """
    Takes inputs as a hash_table, a keyword, and its value and adds
    the keyword and its value to the hash_table (in the correct bucket)
    the bucket where the keyword could occur.
    """
    hash_table_get_bucket(hash_table, keyword).append([keyword, value])


def hash_table_get_bucket(hash_table, keyword):
    """
    Takes two inputs a hash_table, and a keyword, and returns
    the bucket where the keyword could occur. Note that the bucket
    returned by the procedure may not contain the searched for
    keyword in case the keyword is not present in the hash table.
    """
    return hash_table[hash_string(keyword, len(hash_table))]


def make_hash_table(nbuckets):
    """
    Takes as input a number, nbuckets, and outputs an
    empty hash table with nbuckets empty buckets.
    """
    return [[] for i in range(nbuckets)]


def hash_string(keyword, buckets):
    """
    Takes as its inputs a string and the number of buckets, b,
    and returns a number between 0 and b - 1, which gives the
    position where that string belongs.
    """
    h = 0
    for char in keyword:
        h = (h + ord(char)) % buckets
    return h


def test_hash(hash_function, url, size):
    """
    Takes as input hash_function to be tested, url and bucket size.
    Returns bucket counts. For a better hash_function the counts
    should not differ much.
    """
    def source_get(url):
        """
        Takes as input a url page and returns the content of that url page.
        """
        def source_clean(source):
            """
            Takes as input a url page source and
            returns the cleaned content of that url page.
            """
            for char in source:
                if not char.isalnum():
                    source = source.replace(char, " ")
            return source

        try:
            import requests
            return source_clean(str(requests.get(url).content))
        except:
            return ""

    keys = source_get(url).split()
    results = [0] * size
    key_used = []

    for key in keys:
        if key not in key_used:
            hash_value = hash_function(key, size)
            results[hash_value] += 1
            key_used.append(key)

    return results


print(hash_string("", 12))
print(hash_string("udacity", 1000))
url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
count = test_hash(hash_string, url, 12)
print(count)
