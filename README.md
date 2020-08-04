# Minecraft SFA Scripts
A couple scripts to help with usage of SFA accounts in sniping Minecraft usernames

## SFA Checker
Requires Python & aiohttp library (pip install aiohttp)

Place accounts in email:password format in a text file named "accounts.txt" in the same directory as the script

Set "check_for_nc" to True/False depending on if you want to check for namechange within last 30 days

## Get Valid Bearer
Requires Python, the requests and json library.

Used to get a valid bearer token from just the access token given by the authserver without a captcha (Only works for SFAs)

After that, it's fairly straight-forward and self explanatory but if you don't understand something, consult https://wiki.vg/Authentication#Authenticate
