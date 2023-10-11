# #მომხმარებლის ნიშნებისგან გამოანგარიშება საშვალო არითმეტიკული და თუ ცხრაზე მეტი იქნება
# #დაუპრინტეთ გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რისთვისაც შეალიე შენი ცხოვრების წლები
# #თუ ეს იქნება 5ზე ნაკლები დაუპრინტე გილოცავ გაექეცი მატრიცას
# #თუ იქნება 5 იდან 9 მდე დაუპრინტე YOU ARE MID
# #თუ იქნება 10ზე მეტი ან 0ზე ნაკლები დაუპრინტე there is something wrong with you
# ---------------------------
# ----------------------------
# ----------------------------
pirveli=15
meore=9
mesame=4
meotxe=10
mexute=2
meeqvse=3
all= pirveli+meore+mesame+meotxe+mexute+meeqvse
saShualo_aritmetikuli= all/6
if saShualo_aritmetikuli>9:
    print("ილოცავ შენ გადმოგეცა ტოსტერი")
elif saShualo_aritmetikuli<5:
    print("გილოცავ გაექეცი მატრიცას")
elif saShualo_aritmetikuli>5 and saShualo_aritmetikuli < 9:
    print("YOU ARE MID")
if saShualo_aritmetikuli >10:
    print("here is something wrong with you")  
if saShualo_aritmetikuli <0:
    print("there is something wrong with you")



