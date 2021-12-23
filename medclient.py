import requests
import string

class Formatter:
	dont_keep = '''!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''

	@staticmethod
	def get_categories(data):
		types = ("research", "program", "volunteering", "shadowing")
		if isinstance(data, str):
			data = [data]
		categories = ",".join([c for c in data if c in types])
		if not categories:
			categories = "undefined"
		return categories

	@staticmethod
	def get_query(data):
		return data if data else "undefined"

	@staticmethod
	def get_area_of_study(data, areas):
		if not data:
			data = 'undefined'
		data = data.lower().translate(str.maketrans('','',Formatter.dont_keep))
		area = areas.get(data, 'undefined')
		return area

	@staticmethod
	def get_institution(data, institutions):
		if not data:
			data = 'undefined'
		data = data.lower().translate(str.maketrans('','',Formatter.dont_keep))
		institution = institutions.get(data, 'undefined')
		return institution

	@staticmethod
	def get_location(data, locations):
		if not data:
			data = 'undefined'
		data = data.lower().translate(str.maketrans('','',Formatter.dont_keep))
		location = locations.get(data, 'undefined')
		return location

	@staticmethod
	def get_dates(data):
		types = ("all year", "summer", "academic year")
		if isinstance(data, str):
			data = [data]
		dates = ','.join([repr(types.index(d)) for d in data if d in types])
		return dates if dates else "undefined"

	@staticmethod
	def get_eligibility(data):
		types = ("9", "10", "11", "12", "freshman", "sophomore", "junior", "senior")
		if isinstance(data, str):
			data = [data]
		eligibility = ','.join([e.replace('th','') for e in data if e.replace('th','') in types])
		return eligibility if eligibility else "undefined"

	@staticmethod
	def get_stipend(data):
		if data:
			return "true"
		else:
			return "undefined"

	@staticmethod
	def get_page(data):
		try:
			page = int(data)
			return data if data > 0 else "undefined"
		except:
			return "undefined"



class MedClient:
	__slots__ = ["s", "areas", "locations", "institutions"]

	def __init__(self):
		self.s = requests.Session()
		self.s.headers.update({"user-agent": "MedClient"})
		get_ids = self.s.get(
			"https://projectmeded.herokuapp.com/api/opportunities?c=research,program,volunteering,shadowing&q=test"
		)
		self.areas, self.locations, self.institutions = [{}, {}, {}]
		if get_ids.ok:
			dont_keep = '''!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''
			self.s.cookies.update(get_ids.cookies)
			data = get_ids.json()
			self.areas = {
				i["name"].lower().translate(str.maketrans('','',dont_keep)): i["id"]
				for i in data["areas"]
			}
			self.locations = {
				i["name"].lower().translate(str.maketrans('','',dont_keep)): i["id"]
				for i in data["locations"]
			}
			self.institutions = {
				i["name"].lower().translate(str.maketrans('','',dont_keep)): i["id"]
				for i in data["institutions"]
			}

	def search(self, 
		categories=[],
		query=None,
		area_of_study=None,
		institution=None,
		location=None,
		dates=[],
		eligibility=[],
		stipend=False,
		page=0
	):
		url = "https://projectmeded.herokuapp.com/api/opportunities?c={}&q={}&a={}&i={}&l={}&d={}&e={}&f={}&p={}"

		categories = Formatter.get_categories(categories)
		query = Formatter.get_query(query)
		area_of_study = Formatter.get_area_of_study(area_of_study, self.areas)
		institution = Formatter.get_institution(institution, self.institutions)
		location = Formatter.get_location(location, self.locations)
		dates = Formatter.get_dates(dates)
		eligibility = Formatter.get_eligibility(eligibility)
		stipend = Formatter.get_stipend(stipend)  # aka, funding
		page = Formatter.get_page(page)

		res = self.s.get(
			url.format(
				categories,
				query,
				area_of_study,
				institution,
				location,
				dates,
				eligibility,
				stipend,
				page
			)
		)
		if res.ok:
			return res.json()['opportunities']
		else:
			return []
