import speedtest
test=speedtest.Speedtest()
options=int(input('''Which options do you want ? :
1/ Download Speed

2/ Upload Speed

3/ Ping

Your Choice:'''))

if options == 1:
	print(test.download()/(1025*1025), "Mbps")
elif options == 2:
	print(test.upload()/(1025*1025), "Mbps")
elif options == 3:
	servernames =[]
	test.get_servers(servernames)
	print(test.results.ping)
else:
	print("Please enter the correct Choice !")