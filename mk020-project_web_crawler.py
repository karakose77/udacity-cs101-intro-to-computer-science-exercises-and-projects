# WEB CRAWLER PROJECT

# A web crawler is a program that collects content from the web.
# A web crawler finds web pages by starting from a seed page and
# following links to find other pages, and following links from
# the other pages it finds, and continuing to follow links until
# it has found many web pages.


cache = {
    'http://udacity.com/cs101x/urank/index.html': """<html> <body>
<h1>Dave's Cooking Algorithms</h1>
<p>
Here are my favorite recipies:
<ul>
<li> <a href="http://udacity.com/cs101x/urank/hummus.html">Hummus Recipe</a>
<li> <a href="http://udacity.com/cs101x/urank/arsenic.html">
        World's Best Hummus
    </a>
<li> <a href="http://udacity.com/cs101x/urank/kathleen.html">
        Kathleen's Hummus Recipe
    </a>
</ul>
For more expert opinions, check out the
<a href="http://udacity.com/cs101x/urank/nickel.html">Nickel Chef</a>
and <a href="http://udacity.com/cs101x/urank/zinc.html">Zinc Chef</a>.
</body>
</html>
""",
    'http://udacity.com/cs101x/urank/zinc.html': """<html>
<body>
<h1>The Zinc Chef</h1>
<p>
I learned everything I know from
<a href="http://udacity.com/cs101x/urank/nickel.html">the Nickel Chef</a>.
</p>
<p>
For great hummus, try
<a href="http://udacity.com/cs101x/urank/arsenic.html">this recipe</a>.
</body>
</html>
""",
    'http://udacity.com/cs101x/urank/nickel.html': """<html>
<body>
<h1>The Nickel Chef</h1>
<p>
This is the
<a href="http://udacity.com/cs101x/urank/kathleen.html">
best Hummus recipe!
</a>
</body>
</html>
""",
    'http://udacity.com/cs101x/urank/kathleen.html': """<html>
<body>
<h1>
Kathleen's Hummus Recipe
</h1>
<p>
<ol>
<li> Open a can of garbonzo beans.
<li> Crush them in a blender.
<li> Add 3 tablesppons of tahini sauce.
<li> Squeeze in one lemon.
<li> Add salt, pepper, and buttercream frosting to taste.
</ol>
</body>
</html>
""",
    'http://udacity.com/cs101x/urank/arsenic.html': """<html>
<body>
<h1>
The Arsenic Chef's World Famous Hummus Recipe
</h1>
<p>
<ol>
<li> Kidnap the <a href="http://udacity.com/cs101x/urank/nickel.html">
                    Nickel Chef
                </a>.
<li> Force her to make hummus for you.
</ol>
</body>
</html>
""",
    'http://udacity.com/cs101x/urank/hummus.html': """<html>
<body>
<h1>
Hummus Recipe
</h1>
<p>
<ol>
<li> Go to the store and buy a container of hummus.
<li> Open it.
</ol>
</body>
</html>
""",
}


def get_page(url):
    """
    Takes as input a url page and returns the content of that url page.
    """
    try:
        return cache[url]
    except KeyError:
        try:
            import requests
            return str(requests.get(url).content)
        except:
            return ""
        return ""


def get_next_target(page):
    """
    Takes a page as input, searches for the first link on that page,
    returns that as the value of url and also returns the position
    at the end of the quote as the starting point for the next search.
    """
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote


def get_all_links(page):
    """
    Takes as input a string that represents the text on a web page
    and produces as output a list containing all the URLs that are
    targets of link tags on that page.
    """
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    """
    Takes as inputs two lists and modifies the first input list to be
    the set union of the two lists.
    """
    for e in b:
        if e not in a:
            a.append(e)


def add_page_to_index(index, url, content):
    """
    Takes three inputs:
    - index (dictionary)
    - url (string)
    - content (string)
    Updates the index to include all of the word occurrences found in
    the page content by adding the url to the word's associated url list.
    """
    words = content.split()
    for word in words:
        add_to_index(index, word, url)


def add_to_index(index, keyword, url):
    """
     Takes three inputs:
     - a dictionary type index {"keyword": [[list1], [list2]], ...}
     - a keyword string
     - a url string
     If the keyword is already in the index, adds the url to the
     list of urls associated with that keyword. If the keyword is
     not in the index, adds an entry to to the index: [keyword, [url]]
    """
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]


def crawl_web(seed):  # returns index, graph of inlinks
    """
    Takes as input a seed page url, and returns a list of all the urls
    that can be reached by following links starting from the seed page
    and a dictionary, "graph" which gives a mapping from each page to all
    the pages it links to.
    """
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph


def compute_ranks(graph):
    """
    Takes as input a dictionary, "graph" which gives a mapping from
    each page to all the pages it links to and returns a dictionary
    which gives a rank for each page in the graph.
    """
    d = 0.8  # damping factor
    numloops = 10

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for node in graph:
                if page in graph[node]:
                    newrank = newrank + d * (ranks[node] / len(graph[node]))
            newranks[page] = newrank
        ranks = newranks
    return ranks


def look_up(index, keyword):
    """
    Takes two inputs:
    - A dictionary type index
    - The keyword to lookup in the index
    Returns a list of the urls associated with the keyword.
    If the keyword is not in the index, returns an empty list.
    """
    try:
        return index[keyword]
    except KeyError:
        return None


def lucky_search(index, ranks, keyword):
    """
    Takes as input an index, a ranks dictionary (the result of compute_ranks),
    and a keyword, and returns the one URL most likely to be the best site for
    that keyword. If the keyword does not appear in the index, lucky_search
    returns None.
    """
    pages = look_up(index, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for page in pages:
        if ranks[page] > ranks[best_page]:
            best_page = page
    return best_page


def record_user_click(index, keyword, url):
    """
    Takes three inputs:
    - A dictionary type index
    - The keyword to lookup in the index
    - A url
    Updates the list of the urls associated with the keyword
    returned by look_up function. If the input url is in that
    list increments the count by one.
    """
    urls = look_up(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1] + 1


def remove_tags(s):
    """
    When the words are added to the index, html tags such as
    <body>, <head>, <table>, <a href="..."> and so on should be removed.
    This function takes as input a string and returns a list of words,
    in order, with the tags removed.
    """
    start = s.find("<")
    while start != -1:
        stop = s.find(">", start)
        s = s[:start] + " " + s[stop+1:]
        start = s.find("<")
    return s.split()


# Here's an example of how your procedure should work on the test site:


index, graph = crawl_web('http://udacity.com/cs101x/urank/index.html')
ranks = compute_ranks(graph)
print(index)
print(ranks)

print(lucky_search(index, ranks, 'Hummus'))
# >>> http://udacity.com/cs101x/urank/kathleen.html

print(lucky_search(index, ranks, 'the'))
# >>> http://udacity.com/cs101x/urank/nickel.html

print(lucky_search(index, ranks, 'babaganoush'))
# >>> None
