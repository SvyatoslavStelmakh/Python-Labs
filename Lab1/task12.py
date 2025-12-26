minut = int(input("Введите количество израсходованных минут разговора: "))
sms = int(input("Введите количество отправленных сообщений: "))
internet = int(input("Введите количество израсходованных Мб интернета: "))

print("Тарифный план мобильной связи за 24,99 руб. в месяц\n"
    "-60 минут разговоров\n"
    "-30 смс сообщений\n"
    "-1ГБ интернет-трафика")

total_sum = 24.99

if minut>60:
    dop_minut = (minut-60)*0.89
    print(f"Плата за дополнительные минуты: {dop_minut:.2f} руб.")
    total_sum=total_sum+dop_minut
if sms>30:
    dop_sms = (sms-30)*0.59
    print(f"Плата за дополнительные sms: {dop_sms:.2f} руб.")
    total_sum=total_sum+dop_sms
if internet>1024:
    dop_internet = (internet-1024)*0.79
    print(f"Плата за дополнительные мегабайты интернета: {dop_internet:.2f} руб.")
    total_sum=total_sum+dop_internet

tax = total_sum*0.02
print(f"Сумма налога(2%): {tax:.2f} руб.")

total_sum=total_sum+tax
print(f"Общая сумма к оплате: {total_sum:.2f} руб.")





