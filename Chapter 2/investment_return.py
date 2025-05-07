"""7% Investment Return"""
principal = float(1000)
annual_rate = float(7)

year_ten_amount = principal * ((1 + (annual_rate / 100)) ** 10)
year_twenty_amount = principal * ((1 + (annual_rate / 100)) ** 20)
year_thirty_amount = principal * ((1 + (annual_rate / 100)) ** 30)

print("""
Amount at end of 10 years is %.2f
Amount at end of 20 years is %.2f
Amount at end of 30 years is %.2f
""" % (year_ten_amount, year_twenty_amount, year_thirty_amount))


