# if url is just fuction argument
class testclass():

    def test(self, url):
        baseUrl =url
        print(baseUrl)


url = "fqdn.illumina.com"
class_obj = testclass()
class_obj.test(url)


# If url is object variable
class testclass():
    def __init__(self, url):
        self.baseUrl = url

    def test(self):
        baseUrl = self.baseUrl
        print(baseUrl)


url = "fqdn.illumina.com"
class_obj = testclass(url)
class_obj.test()
