def route_summarization_in_ip_networks(data):
    ip_list = [('').join('{0:08b}'.format(int(number)) for number in ip.split('.')) for ip in data]# as a result we will get all ips from data[] joined into  strings with length 32
    subnet = 32  # defining subnet with maximum possible value
    while len(set(ip[:subnet] for ip in ip_list)) > 1:
        subnet -= 1

# getting summary route in binary using ljust() string method (filling it with '0' left justified until length of sting will be 32)
    route_in_binary = ip_list[0][:subnet].ljust(32, '0') 
    summary_route = '.'.join(str(int(route_in_binary[i:i+8], 2)) for i in range(0, 32, 8)) #getting summary_route in decimal
    return f'{summary_route}/{subnet}'
