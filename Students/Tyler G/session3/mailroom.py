from textwrap import dedent
import math

# Original list of historical donors and their amounts donated
donations = []
donations.append( ("Marshawn Lynch", [238.99, 159.23]) )
donations.append( ("Russell Wilson", [9910.00, 159.23, 357.00]) )
donations.append( ("Richard Sherman", [426.48, 3859.94, 5496.00]) )
donations.append( ("Kam Chancellor", [999.99]) )
donations.append( ("Bobby Wagner", [999.99]) )

def show_donations():
    x = 0
    print "\nThe names of previous donors are: "
    for person in donations:
        print donations[x][0]
        x += 1

def write_thank_you(name, amount):
    print dedent('''
        Dear %s,
            Thank you for your very kind donation of $%d.
            It will be put to very good use.
                Sincerely,
        -The Team
        ''') % (name, amount)
        
def check_add_donators(name):
    x = 0
    move_on = False
    for person in donations:
        if name.lower() == donations[x][0].lower():
            print "\n%s is a previous donor!" % donations[x][0]
            choice = None
            while not choice:
                amount = raw_input("Please add another donation entry for this individual. Be sure to enter an integer or float: ")
                try:
                    choice = float(amount)
                except ValueError:
                    print "Must be an integer or float value!"                
            donations[x][1].append(float(amount))
            write_thank_you(donations[x][0], float(amount))
            move_on = True
        x += 1
    if move_on == False:
        print "\n%s is a new donor! Adding the name to registry." % name
        choice = None
        while not choice:
            amount = raw_input("How much $ did this individual donate? Be sure to enter an integer or float: ")
            try:
                choice = float(amount)
            except ValueError:
                print "Must be an integer or float value!"
        donations.append( (name, [float(amount)]) )
        write_thank_you(name, float(amount))

def sort_key(item):
	    return item[1]        
        
def create_report():
    report = []
    for (name, amount) in donations:
        total = sum(amount)
        count = len(amount)
        avg = total / count
        report.append( (name, total, count, avg) )
    report.sort(key=sort_key)
    print "%25s | %11s | %9s | %12s" % ("Name", "Total Donated", "Freq Donated", "Avg Donated")
    print "-"*66
    x = 0
    for row in report:
        print "%25s %11.2f %12i %17.2f" % row

print "\n"
print "*"*10, "Welcome to the Mailroom command-line script", "*"*10 
while True:
    print dedent('''
    Type "list" to show the names of our donors. Type "Thank You" to generate 
    a thank-you letter to a donor. Type "Create Report" to generate a report
    of our donors which includes their number of donations, average donation, 
    and total donation amounts. Finally, type "Exit" to exit the program.''')
    response = raw_input("\nWhich option you like to select?: ")
    if response.lower() == "list":
       show_donations()
    if response.lower() == "thank you":
        name_query = raw_input("Enter the full name of the donor: ")
        check_add_donators(name_query)
    if response.lower() == "create report":
        create_report()
    if response.lower() == "exit":
        print "Exiting now..."
        break
       