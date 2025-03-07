# This program creates a tuple 
# That stores months of the year
# from that tuple it will create
# another tuple with just the summer months
# (May, Jun, Jul)
# print out the summer months  one at a time

months = ("January",
          "February",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"
          )

summer = months[3:6]
for month in summer:
    print(month)

# lab has [4:7] but this prints Jun, Jul, Aug
# Amended to [3:6] to reflect May, Jun, Jul