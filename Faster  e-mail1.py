#!/usr/bin/python3

date1 = input('Enter the date ')
subject =input ('Enter the subject ')

print("$messagedate = \"%s\""% date1)
print("$messagesubject= \"%s\""% subject)
print("""$transportservers = Get-ExchangeServer nsbmdmx4*
$results = $transportservers | get-messagetrackinglog -start $messagedate -messagesubject $messagesubject | ?{$_.eventid -eq "DELIVER"}
$users = @()
foreach ($set in $results) {
$users += $set.recipients
}
$users = $users | sort -unique
$users
$users > users.txt 

Gc users.txt | get-mailbox | select sam* > users3.txt""")

print()
print("gc users3.txt | get-mailbox | search-mailbox -searchdumpster -deletecontent -searchquery \'sent:(%s) AND subject:(%s)\'"% (date1, subject))