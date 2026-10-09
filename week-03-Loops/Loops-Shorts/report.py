# Write a report on some given spacecraft that's out there in universe.
# Use dictionaries to make the report.

def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
=============REPORT===========

Name: {spacecraft["name"]}
Distance: {spacecraft["distance"]} AU

==============================
"""

main()

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01
    print(create_report1(spacecraft))

def create_report1(spacecraft):
    return f"""
=============REPORT===========

Name: {spacecraft["name"]}
Distance: {spacecraft["distance"]} AU

==============================
"""

main()


# Use .get() to print the report, if there are no values to print, print unknown as the output.
def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    print(create_report2(spacecraft))

def create_report2(spacecraft):
    return f"""
=============REPORT===========

Name: {spacecraft.get("name", "unknown")}
Distance: {spacecraft.get("distance", "Unknown")} AU

==============================
"""

main()


# Update the create dictionary using .update()
def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report3(spacecraft))

def create_report3(spacecraft):
    return f"""
=============REPORT===========

Name: {spacecraft.get("name", "unknown")}
Distance: {spacecraft.get("distance", "Unknown")} AU
Orbit: {spacecraft.get("orbit", "Unknown")}

==============================
"""

main()