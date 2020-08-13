from covid import Covid
cov = Covid()
cases = cov.get_status_by_country_name("india")
for x in cases:
	print(x,":" , cases[x])