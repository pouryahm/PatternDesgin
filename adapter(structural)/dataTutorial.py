import xmltodict, json

# کلاس شبیه‌ساز منبع داده XML
class XmlDataSource:
    def get_data(self):
        xml_data = """
        <person>
            <name>Pouria</name>
            <age>25</age>
            <email>pouria@example.com</email>
        </person>
        """
        return xml_data


# کلاس شبیه‌ساز موتور تحلیل JSON
class JsonAnalyticsEngine:
    def analyze(self, data):
        print("Analyzing JSON data:")
        print(data)


# 🎯 Adapter
class DataAdapter:
    def __init__(self, xml_source: XmlDataSource):
        self.xml_source = xml_source

    def xml_to_json(self):
        xml_data = self.xml_source.get_data()  # ✅ داده XML واقعی رو بگیر
        json_data = json.dumps(xmltodict.parse(xml_data))
        return json_data


if __name__ == "__main__":
    x1 = XmlDataSource()
    j1 = JsonAnalyticsEngine()

    adaptor = DataAdapter(x1)

    json_data = adaptor.xml_to_json()  # ✅ بدون پارامتر
    j1.analyze(json_data)
