## Many URLs can refer to the same web resource. In order to ensure that you crawl 40,000 distinct web sites, you
# should apply the following canonicalization rules to all URLs you encounter.
from url_normalize import url_normalize

def get_domain(url):
    url = canonicalize_single_url(url)
    url_split = url.split("/")
    domain = url_split[2]
    return domain


def canonicalize_single_url(url, domain=""):

    # If the URL is relative, make it absolute
    if url.startswith(".."):
        url = url.strip("..")

        ## Normalize domain name
        domain = get_domain(domain)

        # Add final slash just in case (gets removed later if it's a double)
        domain = domain + "/"
        url = domain + url

    # Another way for the URL to be relative (starting with /, not ..):
    if url.startswith("/"):
        ## Normalize domain name
        domain = get_domain(domain)
        url = domain + url

    # Another way for the URL to be relative (starting with #):
    if url.startswith("#"):
        ## Normalize domain name
        domain = get_domain(domain)
        url = domain + url

    # Used to normalize everything to http or https
    if "http://www." in url:
        schema = "http://"

    elif "https://www." in url:
        schema = "https://"

    elif "http://" in url:
        schema = "http://"

    else:
        schema = "https://"

    # Remove initial http or www
    url = url.replace("http://www.", "")
    url = url.replace("https://www.", "")
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")

    # Remove hash suffixes
    url = url.split("#")[0]

    url = schema + url
    url = url_normalize(url)
    return url



def run_tests():
    print(canonicalize_single_url("https://www.abc.com"))
    print(canonicalize_single_url("http://www.abc.com"))
    print(canonicalize_single_url("http://www.abc.html"))
    print(canonicalize_single_url("/wiki/SomeText", "wikipedia.com"))
    print(canonicalize_single_url("../wiki/SomeText", "Wikipedia.com"))
    print(canonicalize_single_url("#jumplink", "Wikipedia.com"))
    print(canonicalize_single_url("www.wikipedia.org/wiki/SomeText"))
    print(canonicalize_single_url("HTTP://www.Example.com/SomeFile.html"))
    print(canonicalize_single_url("http://www.example.com:80"))
    print(canonicalize_single_url("../c.html", "example.com"))
    print(canonicalize_single_url("http://www.example.com/a.html#anything"))
    print(canonicalize_single_url("http://www.example.com//a.html"))
    print(canonicalize_single_url("https://www.google.com/search?q=hash+table&oq=hash+table&aqs=chrome..69i57j0i67j0l3j0i10j0i67j0l3.3698j0j9&sourceid=chrome&ie=UTF-8"))
    print(url_normalize("https://www.google.com/search?q=hash+table&oq=hash+table&aqs=chrome..69i57j0i67j0l3j0i10j0i67j0l3.3698j0j9&sourceid=chrome&ie=UTF-8"))
    print(get_domain("http://www.example.com/a.html"))
    print(get_domain("https://www.abc.com"))
    print(get_domain("abc.com"))
    print(get_domain("www.abc.com"))
    print(get_domain("www.abc.com/"))
    print(get_domain("www.abc.com/hi"))
    print(get_domain("https://www.google.com/search?q=hash+table&oq=hash+table&aqs=chrome..69i57j0i67j0l3j0i10j0i67j0l3.3698j0j9&sourceid=chrome&ie=UTF-8"))
    print(canonicalize_single_url("https://abc.com"))
    print(canonicalize_single_url("http://abc.com"))

#run_tests()
